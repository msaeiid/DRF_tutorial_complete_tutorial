from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, views, status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from .serializers import ProductSerializer
from products.models import Product


class ProductListCreateAPIViews(generics.ListCreateAPIView):
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


@api_view(http_method_names=['POST', 'GET'])
def product_alt_view(request: Request, pk=None, *args, **kwargs):
    if request.method == "GET":
        products = get_list_or_404(Product)
        if pk:
            product = get_object_or_404(Product, pk=pk)
            serializer = ProductSerializer(product, many=False)
        else:
            serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "POST":
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data['title']
            content = serializer.validated_data['content']
            if content:
                content = title
                serializer.save(content=content)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # this is why generic views are good
