from lunch.models import Shop, Category
from django.core import serializers
from django.http import HttpResponse,Http404
import json

def search(request):
    response = serializers.serialize("json", Shop.objects.all().select_related())

    return createHttpResponse(response)

def createHttpResponse(response):
    httpResponse = HttpResponse(response)
    httpResponse["Access-Control-Allow-Origin"] = "*"
    httpResponse["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    httpResponse["Access-Control-Max-Age"] = "1000"
    httpResponse["Access-Control-Allow-Headers"] = "*"
    return httpResponse
