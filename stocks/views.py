from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from .models import Stock
from .serializers import StockSerializer, StockDetailSerializer


class StockListView(ListAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockRetrieveAPIView(RetrieveAPIView):

    queryset = Stock.objects.all()
    serializer_class = StockDetailSerializer

    def retrieve(self, requset, *args, **kwargs):
        instance = self.get_object()
        serializer = StockDetailSerializer(instance)
        return Response(serializer.data)
