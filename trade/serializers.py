from rest_framework import serializers
from .models import TradeNode

class TradeNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeNode
        fields = '__all__'