"""Supplier Api view."""
from algo.models import Product, ProductCategory
from algo.serializers.product import ProductSerializer, ProductCategorySerializer
from rest_framework import viewsets


class ProductViewSet(viewsets.ModelViewSet):
    """SupplierViewSet."""
    serializer_class = ProductSerializer
    queryset = Product.objects.order_by('created_at')


class ProductCategoryViewSet(viewsets.ModelViewSet):
    """SupplierViewSet."""
    serializer_class = ProductCategorySerializer
    queryset = ProductCategory.objects.order_by('created_at')