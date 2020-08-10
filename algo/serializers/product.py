"""Products serializer module."""
from rest_framework import serializers

from algo.models import Product, ProductCategory

class ProductSerializer(serializers.ModelSerializer):
    """Supplier Serializer."""
    category = serializers.CharField(source='category.name', read_only=True)
    unit = serializers.CharField(source='unit.name', read_only=True)
    supplier = serializers.CharField(source='supplier.kode', read_only=True)

    class Meta:  # noqa D106
        model = Product
        name = 'product'
        fields = '__all__'
        datatables_always_serialize = ('id')

class ProductCategorySerializer(serializers.ModelSerializer):
    """Supplier Serializer."""

    class Meta:  # noqa D106
        model = ProductCategory
        name = 'product_category'
        fields = '__all__'
        datatables_always_serialize = ('id')