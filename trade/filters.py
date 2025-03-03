import django_filters

from .models import TradeNode


class TradeNodeFilter(django_filters.FilterSet):
    """фильтр по полю country"""

    country = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = TradeNode
        fields = ["country"]
