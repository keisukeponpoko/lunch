from django.shortcuts import render
from lunch.models import Shop, Category
from django.core import serializers

# Create your views here.
def map(request):
    return render(request, 'lunch.html')

def getShop(request):
    import json
    from django.http import HttpResponse,Http404

    response = serializers.serialize("json", Shop.objects.all().select_related())
    return HttpResponse(response)
