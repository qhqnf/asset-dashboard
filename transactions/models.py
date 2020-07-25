from django.db import models


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
    date = models.DateField()
    shareholder = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="s_transactions"
    )
    stock = models.ForeignKey(
        "stocks.Stock", on_delete=models.CASCADE, related_name="s_transactions"
    )
    qunatitiy = models.IntegerField()


class MoneyTransaction(models.Model):

    M_TYPE_DEPOSIT = "deposit"
    M_TYPE_WITHDRAW = "withdraw"

    M_TYPE_CHOICES = (
        (M_TYPE_DEPOSIT, "Deposit"),
        (M_TYPE_WITHDRAW, "Withdraw"),
    )

    transaction_type = models.CharField(choices=M_TYPE_CHOICES)
    date = models.DateField()
    account_holder = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="m_transactions"
    )
    quantitiy = models.IntegerField()
