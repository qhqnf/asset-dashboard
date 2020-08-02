# Generated by Django 2.2.13 on 2020-07-31 10:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('transactions', '0001_initial'),
        ('stocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stocktransaction',
            name='shareholder',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='stocktransaction',
            name='stock',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transactions', to='stocks.Stock'),
        ),
    ]