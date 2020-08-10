"""Config admin.py."""
from django.contrib import admin

# Register your models here.
from algo.models import Product, ProductCategory


class ProductAdmin(admin.ModelAdmin):
    """Config admin."""
    list_display = ('name',
                    'category',
                    'stock',
                    'selling_price',
                    'supplier',
                    'status', )

class ProductCategoryAdmin(admin.ModelAdmin):
    """Config admin."""
    list_display = ('name', )


admin.site.register(Product, ProductAdmin)
admin.site.register(ProductCategory, ProductCategoryAdmin)