from django.db import models


class Stock(models.Model):

    code = models.CharField(max_length=10, primary_key=True, verbose_name="주식 코드")
    name = models.CharField(max_length=40)

    class Meta:
        ordering = ['code']

    def __str__(self):
        return self.name
