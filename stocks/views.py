from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer


class StockListView(ListAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer

