from django.db import models
import datetime


class StockTransaction(models.Model):

    TYPE_BUY = "buy"
    TYPE_SELL = "sell"

    TYPE_CHOICES = (
        (TYPE_BUY, "Buy"),
        (TYPE_SELL, "Sell"),
    )

    transaction_type = models.CharField(
        choices=TYPE_CHOICES, max_length=9, default=TYPE_BUY
    )
    date = models.DateField(default=datetime.datetime.now)
    shareholder = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="transactions"
    )
    stock = models.ForeignKey(
        "stocks.Stock", on_delete=models.CASCADE, related_name="transactions"
    )
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.shareholder} {self.transaction_type} {self.quantity} shares of {self.stock}"

    def total_price(self):
        return self.price * self.quantity
