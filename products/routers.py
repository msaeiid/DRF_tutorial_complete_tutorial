from rest_framework.routers import DefaultRouter
from .viewsets import ProductViewSet,ProductListRetrieveViewSet

router=DefaultRouter()
router.register('products',ProductListRetrieveViewSet,basename='products')

urlpatterns =router.urls