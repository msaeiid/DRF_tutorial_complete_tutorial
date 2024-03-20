from rest_framework import generics, mixins
from api.mixins import IsStaffEditorPermissionMixin, UserQuerySetMixin
from .serializers import ProductSerializer
from products.models import Product
from . import client
from rest_framework.response import Response
from rest_framework import status


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


class ProductMixinView(
    # Note permission mixins should be the first mix in same as below
    IsStaffEditorPermissionMixin,
    UserQuerySetMixin,
    generics.GenericAPIView,
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin
):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'
    # UserQuerySetMixin
    user_field = 'user'
    allow_staff_view = True

    # note that permission and authentication are working on generic views

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk', None)
        if pk:
            return self.retrieve(request, *args, **kwargs)
        else:
            return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(self, request, *args, **kwargs)

    def perform_create(self, serializer):
        # if you need to add user when trying to create
        title = serializer.validated_data['title']
        content = serializer.validated_data['content']
        if content:
            content = title
        serializer.save(content=content, user=self.request.user)


# class SearchListView(generics.ListAPIView):
#     queryset=Product.objects.all()
#     serializer_class=ProductSerializer

#     def get_queryset(self):
#         qs= super().get_queryset()
#         q=self.request.GET.get('q')
#         result=Product.objects.none()
#         if q is not None:
#             user=None
#             if self.request.user.is_authenticated:
#                 user=self.request.user
#             result=qs.search(q,user=user)
#         return result


class SearchListView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        user = None
        if request.user.is_authenticated:
            user = request.user.username
        query = request.GET.get('q')
        public = str(request.GET.get('public')) != "0"
        tag = request.GET.get('tag') or None
        print(user, query, public, tag)
        if query:
            result = client.perform_search(
                query, tags=tag, user=user, public=public)
            return Response(result)
        else:
            return Response('', status=status.HTTP_400_BAD_REQUEST)
