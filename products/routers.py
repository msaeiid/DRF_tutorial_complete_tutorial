from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet,ProductListRetrieveViewSet,product_list,product_retrieve

router=DefaultRouter()
router.register('products',ProductListRetrieveViewSet,basename='products')

urlpatterns =router.urls