from rest_framework import serializers
from .models import Stock
from .price_crawler import get_current_price


class StockSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stock
        fields = "__all__"


class StockDetailSerializer(serializers.Serializer):

    code = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        code = obj.code
        return get_current_price(code)

