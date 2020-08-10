"""Config admin.py."""
from django.contrib import admin

# Register your models here.
from algo.models import Tracking, Supplier, Distributor, Product
from algo.services.supplier import supplier_services
from algo.services.distributor import distributor_services


class TrackingAdmin(admin.ModelAdmin):
    """Config admin."""
    list_display = ('product',
                    'supplier',
                    'distributor',
                    'stock',)

    def save_model(self, request, obj, form, change):
        supplier = form.cleaned_data.get('supplier')
        distributor = form.cleaned_data.get('distributor')
        product = form.cleaned_data.get('product')
        stock = form.cleaned_data.get('stock')
        if supplier:
            supplier_services.update_product(product, stock)
        if distributor:
            distributor_services.update_product(product, stock)
        super(TrackingAdmin, self).save_model(request, obj, form, change)


admin.site.register(Tracking, TrackingAdmin)
