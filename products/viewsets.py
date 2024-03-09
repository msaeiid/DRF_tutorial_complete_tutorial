from rest_framework import viewsets,mixins
from .models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    """
    get -> List ->Queryset
    get -> Retrieve -> Products Instance Detail View
    post -> Create -> New Instance
    put -> Update ->
    patch -> Partial Update
    delete -> Destroy
    """
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

# for Clearity we can seprate the viewsets...
class ProductListRetrieveViewSet(viewsets.GenericViewSet,
                                 mixins.ListModelMixin,
                                 mixins.RetrieveModelMixin):
    """
    get -> List ->Queryset
    get -> Retrieve -> Products Instance Detail View
    """
    
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    lookup_field='pk'

#also for clearity we can seprate urls
#product_list=ProductViewSet.as_view({'get':'list'})
#product_retrieve=ProductViewSet.as_view({'get':'retrieve'})

    