from django.db import models
import datetime


class StockTransaction(models.Model):

    S_TYPE_BUY = "buy"
    S_TYPE_SELL = "sell"

    S_TYPE_CHOICES = (
        (S_TYPE_BUY, "Buy"),
        (S_TYPE_SELL, "Sell"),
    )

    transaction_type = models.CharField(
        choices=S_TYPE_CHOICES, max_length=9, default=S_TYPE_BUY
    )
    date = models.DateField(default=datetime.datetime.now)
    shareholder = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="s_transactions"
    )
    stock = models.ForeignKey(
        "stocks.Stock", on_delete=models.CASCADE, related_name="s_transactions"
    )
    price = models.IntegerField(blank=False)
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity} shares of {self.stock}"


class CashTransaction(models.Model):

    C_TYPE_DEPOSIT = "deposit"
    C_TYPE_WITHDRAW = "withdraw"

    C_TYPE_CHOICES = (
        (C_TYPE_DEPOSIT, "Deposit"),
        (C_TYPE_WITHDRAW, "Withdraw"),
    )

    transaction_type = models.CharField(choices=C_TYPE_CHOICES, max_length=10)
    date = models.DateField(default=datetime.datetime.now)
    account_holder = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="c_transactions"
    )
    quantity = models.IntegerField(blank=False)

    def __str__(self):
        return f"{self.transaction_type} {self.quantity}won"

