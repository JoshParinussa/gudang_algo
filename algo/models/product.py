from django.db import models

from .base import BaseModel

class ProductCategory(BaseModel):
    """ProductCategory model."""
    name = models.CharField(max_length=128, db_index=True, verbose_name="nama kategori")

    def __str__(self):
        """String representation."""
        return self.name

class Product(BaseModel):
    """Product model."""
    class ProductStatus(models.IntegerChoices):
        """StoreTier choice."""
        ACTIVE = 0
        INACTIVE = 1
    name = models.CharField(max_length=128, verbose_name="nama produk")
    barcode = models.CharField(max_length=128, blank=False, null=False, unique=True)
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE, verbose_name="kategori", blank=True, null=True)
    unit = models.ForeignKey('Unit', on_delete=models.CASCADE, null=True, verbose_name="satuan")
    stock = models.BigIntegerField(blank=True, null=True, verbose_name="stok")
    minimal_stock = models.BigIntegerField(blank=True, null=True, verbose_name="batas minimal")
    purchase_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, verbose_name="harga beli")
    selling_price = models.DecimalField(max_digits=9, decimal_places=0, null=True, verbose_name="eceran")

    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=True, null=True)

    status = models.PositiveSmallIntegerField(choices=ProductStatus.choices, default=ProductStatus.ACTIVE, db_index=True)

    def __str__(self):
        """String representation."""
        return self.name