from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from .models import StockTransaction
from .serializers import StockTransactionsSerializer
from .permissions import IsSelf


class StockTransactionsView(ModelViewSet):

    queryset = StockTransaction.objects.all()
    serializer_class = StockTransactionsSerializer

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [IsAdminUser]
        elif self.action == "create":
            permission_classes = [IsAuthenticated]
        elif self.action == "retrieve" or self.action == "destroy":
            permission_classes = [IsSelf]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]
