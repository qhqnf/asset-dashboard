from django.test import TestCase
import datetime
from transactions.models import StockTransaction
from stocks.models import Stock
from stocks.management.commands import crawler
from users.models import User

# Create your tests here.


class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        data = crawler.get_stock_data()
        for i in range(0, len(data)):
            Stock.objects.create(
                code=data.iloc[i, 0], name=data.iloc[i, 1],
            )
        User.objects.create(
            username="yhc", password="123",
        )
        StockTransaction.objects.create(
            transaction_type="buy",
            date=datetime.datetime.today(),
            shareholder=User.objects.get(pk=1),
            stock=Stock.objects.get(pk="088980"),
            price=10000,
            quantity=100,
        )

    def setUp(self):
        print(" ")
        pass

    def test_stock_name(self):
        transaction = StockTransaction.objects.get(id=1)
        stock_name = transaction.stock.name
        self.assertEquals(stock_name, "맥쿼리인프라")

