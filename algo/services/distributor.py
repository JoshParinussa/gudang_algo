"""ProductServices module."""
from algo.models import Distributor, Product


class DistributorServices:
    """ProductServices."""
    def update_product(self, product, updated_stock):
        product = Product.objects.get(id=product.id)
        product.stock -= updated_stock
        product.save()
        return product

distributor_services = DistributorServices()
