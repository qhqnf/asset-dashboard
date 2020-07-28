from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, ListAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
from .permissions import IsOwner
from transactions.serializers import StockTransactionsSerializer


class UserListView(ListAPIView):

    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserTransactionView(ListCreateAPIView):

    serializer_class = StockTransactionsSerializer
    permission_classes = [IsOwner]

    def get_queryset(self):
        user = get_object_or_404(User, pk=self.kwargs["pk"])
        return user.s_transactions.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )

