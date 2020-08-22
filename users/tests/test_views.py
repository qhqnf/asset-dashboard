import json
from rest_framework import status
from django.test import TestCase
from rest_framework.test import APIClient
from django.db import models
from stocks.models import Stock
from stocks.management.commands import crawler
from users.models import User

client = APIClient()


class YourTestClass(TestCase):
    """
    @classmethod
    def setUpTestData(cls):
        data = crawler.get_stock_data()
        for i in range(0, len(data)):
            Stock.objects.create(
                code=data.iloc[i, 0], name=data.iloc[i, 1],
            )
    """

    def setUp(self):
        self.payload = {"username": "yhc", "password": "123"}
        self.payload2 = {"username": "guest", "password": "123"}
        client.post(
            "/api/v1/users/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )

    def test_login(self):
        response1 = client.post(
            "/api/v1/users/login/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )
        token = response1.data.get("token")
        token = str(token)[2:-1]
        client.credentials(HTTP_AUTHORIZATION="jwt " + token)
        response2 = client.get(
            f"/api/v1/users/1/asset/", content_type="application/json",
        )
        print(response2.data)
        self.assertEqual(response2.status_code, status.HTTP_200_OK)
