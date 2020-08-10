"""Supplier Api view."""
from algo.models import Tracking
from algo.serializers.tracking import TrackingSerializer
from rest_framework import viewsets


class TrackingViewSet(viewsets.ModelViewSet):
    """SupplierViewSet."""
    serializer_class = TrackingSerializer
    queryset = Tracking.objects.order_by('created_at')
    