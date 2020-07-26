from django.core.management.base import BaseCommand
from .crawler import get_stock_data
from stocks import models


class Command(BaseCommand):

    help = "This command put all stock's name and serial number into database"

    def handle(self, *args, **options):

        models.Stock.objects.all().delete()

        data = get_stock_data()

        for i in range(0, len(data)):
            models.Stock.objects.create(
                code=data.iloc[i, 0], name=data.iloc[i, 1],
            )
        self.stdout.write(self.style.SUCCESS(f"{len(data)} stocks data updated"))
