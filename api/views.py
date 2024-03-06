from django.forms import model_to_dict
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer


# building a simple API with JsonResponse
@api_view(http_method_names=['GET'])
def api_home(request: Request):
    """
    DRF API View
    :param request:
    :return: a random product will return
    """
    product = Product.objects.all().last()
    if product:
        serializer = ProductSerializer(product)
        return Response(serializer.data)
