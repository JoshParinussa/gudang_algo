"""Products serializer module."""
from rest_framework import serializers

from algo.models import Unit

class UnitSerializer(serializers.ModelSerializer):
    """Supplier Serializer."""

    class Meta:  # noqa D106
        model = Unit
        name = 'unit'
        fields = '__all__'
        datatables_always_serialize = ('id')