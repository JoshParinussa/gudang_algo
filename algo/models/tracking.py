from django.db import models

from .base import BaseModel

class Tracking(BaseModel):
    """Supplier model."""
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="product_tracking", blank=True, null=True)
    supplier = models.ForeignKey('Supplier', on_delete=models.CASCADE, blank=True, null=True)
    distributor = models.ForeignKey('Distributor', on_delete=models.CASCADE, blank=True, null=True)
    stock = models.BigIntegerField(blank=True, null=True, verbose_name="stok")

    def __str__(self):
        """String representation."""
        return self.product.name