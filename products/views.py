from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework import generics, views, status, mixins, authentication, permissions
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response
from djangoProject.authentiction import TokenAuthentication
from .permissions import IsStaffEditorPermission
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


class ProductUpdateAPIViews(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        product = serializer.save()
        if not product.content:
            product.content = product.title
            product.save()


class ProductDestroyAPIViews(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'


class ProductMixinView(generics.GenericAPIView,
                       mixins.ListModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.CreateModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    # note that permission and authentication are working on generic views
    permission_classes = [permissions.IsAdminUser,
                          IsStaffEditorPermission]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        self.update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        self.destroy(self, request, *args, **kwargs)
