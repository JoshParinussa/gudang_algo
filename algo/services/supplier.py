"""ProductServices module."""
from algo.models import Product, Tracking


class SupplierServices:
    """ProductServices."""
    def update_product(self, product, updated_stock):
        product = Product.objects.get(id=product.id)
        product.stock += updated_stock
        product.save()
        return product

    def supplier_avg_product(self, supplier):
        products = Product.objects.filter(supplier=supplier)
        tracking = Tracking.objects.filter(product__in=products)
        return tracking

supplier_services = SupplierServices()
