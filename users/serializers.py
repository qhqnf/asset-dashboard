from rest_framework import serializers
from .models import User
from stocks.serializers import StockSerializer
from .price_crawler import get_current_price


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
        )
        read_only_fields = ("id",)

    def create(self, validated_data):
        password = validated_data.get("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        return user


class RelatedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username",)


class AssetSerializer(serializers.Serializer):

    stock = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=10)
    total_quantity = serializers.IntegerField()
    avg_price = serializers.DecimalField(
        max_digits=None, decimal_places=1, coerce_to_string=True
    )
    price = serializers.SerializerMethodField()

    def get_price(self, obj):
        code = obj["stock"]
        return get_current_price(code)
