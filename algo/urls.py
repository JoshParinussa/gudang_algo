from django.urls import include, path
from rest_framework import routers

from algo.views.apis import supplier as api_supplier
from algo.views.apis import product as api_product
from algo.views.apis import unit as api_unit
from algo.views.apis import distributor as api_distributor
from algo.views.apis import tracking as api_tracking
from algo.views.apis import report as api_report

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'suppliers', api_supplier.SupplierViewSet)
router.register(r'products', api_product.ProductViewSet)
router.register(r'product_categories', api_product.ProductCategoryViewSet)
router.register(r'units', api_unit.UnitViewSet)
router.register(r'distributors', api_distributor.DistributorViewSet)
router.register(r'trackings', api_tracking.TrackingViewSet)

urlpatterns = [
    path('v1/', include((router.urls, 'api_views'), namespace='v1')),
    path('v1/report', api_report.Report.as_view(), name='api_report'),
]   