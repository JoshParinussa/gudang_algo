"""Supplier Api view."""
from algo.models import Supplier
from algo.serializers.supplier import SupplierSerializer
from rest_framework import viewsets
from algo.services.supplier import supplier_services
from rest_framework.decorators import action
from django.http import HttpResponse


class SupplierViewSet(viewsets.ModelViewSet):
    """SupplierViewSet."""
    serializer_class = SupplierSerializer
    queryset = Supplier.objects.order_by('created_at')
    
    @action(detail=False, methods=['POST'])
    def report(self, request):
        """get_by_invoice."""
        supplier = request.POST.get('supplier')
        print("# SUPP", request.POST.get)
        # supplier = Supplier.objects.get(id=supplier)

        # supplier_products = supplier_services.supplier_avg_product(supplier)
        # print("# SUPP PRODUCTS", supplier_products)
        
        return HttpResponse(status=200)