from django.contrib import admin
from . import models


@admin.register(models.StockTransaction)
class StockTransactionAdmin(admin.ModelAdmin):
    pass


@admin.register(models.MoneyTransaction)
class MoneyTransactionAdmin(admin.ModelAdmin):
    pass
