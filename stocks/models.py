from django.db import models


class Stock(models.Model):

    code = models.CharField(max_length=10, primary_key=True)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
