from rest_framework.generics import ListAPIView
from .models import Stock
from .serializers import StockSerializer


class StockListView(ListAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

