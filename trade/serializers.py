from rest_framework import serializers

from .models import TradeNode


class TradeNodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TradeNode
        fields = [
            "id",
            "name",
            "email",
            "country",
            "city",
            "street",
            "house_number",
            "debt_to_supplier",
            "supplier",
            "created_at",
            "products"]
        read_only_fields = ['id',"created_at"]