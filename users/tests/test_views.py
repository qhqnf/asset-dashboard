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
        User.objects.create(username="guest", password="123")

    def test_create_account(self):
        response = client.post(
            "/api/v1/users/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )
        response1 = client.post(
            "/api/v1/users/login/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )
        print(response1)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        client.post(
            "/api/v1/users/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )
        response = client.post(
            "/api/v1/users/login/",
            data=json.dumps(self.payload),
            content_type="application/json",
        )
        print(response.content)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

