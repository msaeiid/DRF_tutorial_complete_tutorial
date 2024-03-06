from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.utils import json


# building a simple API with JsonResponse
def api_home(request: Request):
    body = request.body
    try:
        data = json.loads(body)
    except:
        pass
    print(request.GET)
    data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    print(data)
    return JsonResponse({"message": "Hi there, this is your Django API response"})
