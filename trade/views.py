from rest_framework import generics
from .models import TradeNode
from .serializers import TradeNodeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TradeNodeFilter

class TradeNodeListCreateView(generics.ListCreateAPIView):
    queryset = TradeNode.objects.all()
    serializer_class = TradeNodeSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = TradeNodeFilter

class TradeNodeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradeNode.objects.all()
    serializer_class = TradeNodeSerializer
