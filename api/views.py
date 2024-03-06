from django.http import JsonResponse
from rest_framework.request import Request


# building a simple API with JsonResponse
def api_home(request: Request):
    return JsonResponse({"message": "Hi there, this is your Django API response"})
