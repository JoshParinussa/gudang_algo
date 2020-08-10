"""Products serializer module."""
from rest_framework import serializers

from algo.models import Distributor

class DistributorSerializer(serializers.ModelSerializer):
    """Supplier Serializer."""

    class Meta:  # noqa D106
        model = Distributor
        name = 'distributor'
        fields = '__all__'
        datatables_always_serialize = ('id','company_name','address','contact_person','office_phone','phone')