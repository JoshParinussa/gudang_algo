"""Config admin.py."""
from django.contrib import admin

# Register your models here.
from algo.models import Supplier


class SupplierAdmin(admin.ModelAdmin):
    """Config admin."""
    list_display = ('kode',
                    'company_name',
                    'address',
                    'contact_person',
                    'office_phone',
                    'phone',)


admin.site.register(Supplier, SupplierAdmin)
