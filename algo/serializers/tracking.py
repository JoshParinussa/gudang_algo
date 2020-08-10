"""Products serializer module."""
from rest_framework import serializers

from algo.models import Tracking

class TrackingSerializer(serializers.ModelSerializer):
    """Supplier Serializer."""

    class Meta:  # noqa D106
        model = Tracking
        name = 'tracking'
        fields = '__all__'
        datatables_always_serialize = ('product', 'supplier', 'distributor', 'stock',)