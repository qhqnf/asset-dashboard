from django.urls import path
from . import views
from .models import Stock
from .serializers import StockSerializer
from . import views

urlpatterns = [
    path("", views.StockListView.as_view()),
    path("<str:pk>/", views.StockRetrieveAPIView.as_view()),
]

app_name = "stocks"
