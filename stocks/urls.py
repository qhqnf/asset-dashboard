from django.urls import path
from . import views
from .models import Stock
from .serializers import StockSerializer

urlpatterns = [
    path(
        "",
        views.ListAPIView.as_view(
            queryset=Stock.objects.all(), serializer_class=StockSerializer
        ),
    ),
]

app_name = "stocks"
