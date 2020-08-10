"""Supplier Api view."""
from algo.models import Distributor
from algo.serializers.distributor import DistributorSerializer
from rest_framework import viewsets


class DistributorViewSet(viewsets.ModelViewSet):
    """DistributorViewSet."""
    serializer_class = DistributorSerializer
    queryset = Distributor.objects.order_by('created_at')