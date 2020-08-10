"""Supplier Api view."""
from algo.models import Unit
from algo.serializers.unit import UnitSerializer
from rest_framework import viewsets


class UnitViewSet(viewsets.ModelViewSet):
    """SupplierViewSet."""
    serializer_class = UnitSerializer
    queryset = Unit.objects.order_by('created_at')