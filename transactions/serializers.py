from rest_framework import serializers
from .models import StockTransaction, MoneyTransaction
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
        return StockTransaction.objects.create(**validated_data)
