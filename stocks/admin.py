from django.contrib import admin
from . import models


@admin.register(models.Stock)
class StockAdmin(admin.ModelAdmin):

    list_display = ["code", "name"]