from rest_framework import generics
from .serializers import ProductSerializer

from products.models import Product


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
