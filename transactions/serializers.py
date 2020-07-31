from rest_framework import serializers
from .models import StockTransaction, CashTransaction
from users.serializers import UserSerializer
from stocks.serializers import StockSerializer


class StockTransactionsSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)
    stock = StockSerializer

    class Meta:
        model = StockTransaction
        fields = (
            "user",
            "transaction_type",
            "date",
            "stock",
            "price",
            "quantity",
        )

    def create(self, validated_data):
        request = self.context.get("request")
        s_transaction = StockTransaction.objects.create(
            **validated_data, shareholder=request.user
        )
        return s_transaction
