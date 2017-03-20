# coding: utf-8

import django_filters
from rest_framework import viewsets, generics

from .models import Shop, Category
from .serializer import ShopSerializer

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter(lunch__in = [1000, 2000]).all()

class CategoryFilterViewSet(generics.ListAPIView):
    serializer_class = ShopSerializer
    def get_queryset(self):
        categoryName = self.kwargs['category']
        return Shop.objects.filter(id__in = Category.objects.filter(category__contains = categoryName).values('shop_id')).filter(lunch__in = [1000, 2000]).distinct()
