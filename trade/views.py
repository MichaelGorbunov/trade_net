from rest_framework import generics
from rest_framework.response import Response

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

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        data = request.data.copy()
        if 'debt_to_supplier' in data:
            del data['debt_to_supplier']
        serializer = self.get_serializer(instance, data=data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        return Response(serializer.data)
