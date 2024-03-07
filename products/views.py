from rest_framework import generics
from .serializers import ProductSerializer

from products.models import Product


class ProductCreateAPIViews(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
        if content:
            content = title
            serializer.save(content=content)
        # simple way to add aditional data to serializer
        # instead above send a django signal is possible


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'
