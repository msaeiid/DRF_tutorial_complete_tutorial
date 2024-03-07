from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# building a simple API with JsonResponse
# if @api_view doesn't declare on top of method base API it acts like a normal view which needs CSRF token

@api_view(http_method_names=['GET', 'POST'])
def api_home(request: Request):
    """
    DRF API View
    :param request:
    :return: a random product will return
    """
    if request.method == 'GET':
        product = Product.objects.all().last()
        if product:
            serializer = ProductSerializer(product)
            return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.validated_data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
