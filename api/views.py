from django.forms import model_to_dict
from django.http import JsonResponse, HttpResponse
from rest_framework.request import Request
from rest_framework.utils import json

from products.models import Product


# building a simple API with JsonResponse
def api_home(request: Request):
    product = Product.objects.all().order_by("?").first()
    data = model_to_dict(product, fields=["id", "title", "price"])
    # json_data = json.dumps(data)
    return JsonResponse(data)
    # return HttpResponse(json_data, content_type="application/json")
