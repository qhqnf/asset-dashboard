import jwt
from django.conf import settings
from django.db.models import Sum, F, Case, When
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser, AllowAny
from rest_framework.decorators import action
from .models import User
from .serializers import UserSerializer, AssetSerializer
from .permissions import IsSelf
from transactions.serializers import StockTransactionsSerializer


class UsersViewSet(ModelViewSet):

    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            permission_classes = [AllowAny]
        elif (
            self.action == "update"
            or self.action == "retrieve"
            or self.action == "delete"
            or self.action == "stocks"
            or self.action == "cash"
        ):
            permission_classes = [IsSelf]
        else:
            permission_classes = [IsSelf]

        return [permission() for permission in permission_classes]

    @action(detail=False, methods=["post"])
    def login(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        if not username or not password:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        user = authenticate(username=username, password=password)
        if user is not None:
            encoded_jwt = jwt.encode(
                {"pk": user.pk}, settings.SECRET_KEY, algorithm="HS256"
            )
            return Response(data={"token": encoded_jwt, "id": user.pk})
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

    @action(detail=True, methods=["get"])
    def transactions(self, request, pk):
        user = self.get_object()
        serializer = StockTransactionsSerializer(
            user.transactions.all(), many=True
        ).data
        return Response(serializer, status=status.HTTP_200_OK)

    @action(detail=True, methods=["get"])
    def asset(self, request, pk):
        user = self.get_object()
        if user.transactions.all() is not None:
            stocks = user.transactions.all().annotate(
                total_price=Case(
                    When(transaction_type="buy", then=F("price") * F("quantity")),
                    When(transaction_type="sell", then=-1 * F("price") * F("quantity")),
                ),
                Quantity=Case(
                    When(transaction_type="buy", then=F("quantity")),
                    When(transaction_type="sell", then=-1 * F("quantity")),
                ),
            )
            result = stocks.values("stock").annotate(
                total_quantity=Sum("Quantity"),
                avg_price=(Sum("total_price") / F("total_quantity")),
            )
            serializer = AssetSerializer(result, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

