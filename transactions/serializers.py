from django.db.models import Sum, F, Case, When
from rest_framework import serializers
from .models import StockTransaction
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
        transaction = StockTransaction.objects.create(
            **validated_data, shareholder=request.user
        )
        return transaction

    def validate(self, data):
        # get data
        user = self.context.get("request").user
        if self.instance:
            transaction_type = data.get(
                "transaction_type", self.instance.transaction_type
            )
            stock_pk = data.get("stock", self.instance.stock).pk
            quantity = data.get("quantity", self.instance.quantity)
            price = data.get("price", self.instance.price)
        else:
            transaction_type = data.get("transaction_type")
            stock_pk = data.get("stock").pk
            quantity = data.get("quantity")
            price = data.get("price")
        # check negative value
        if quantity < 0 or price < 0:
            raise serializers.ValidationError(
                "Quantity or price should not be negative"
            )
        # check action that sell more than they have
        stocks = user.transactions.filter(stock=stock_pk).annotate(
            Quantity=Case(
                When(transaction_type="buy", then=F("quantity")),
                When(transaction_type="sell", then=-1 * F("quantity")),
            ),
        )
        print(stocks.count())
        if stocks.count() != 0:
            result = stocks.aggregate(total_quantity=Sum("Quantity"))
            total_quantity = result["total_quantity"]
        else:
            total_quantity = 0
        if transaction_type == "sell" and total_quantity < quantity:
            raise serializers.ValidationError("You can't sell more than you have")
        return data
