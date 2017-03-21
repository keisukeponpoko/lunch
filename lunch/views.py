# coding: utf-8

import django_filters
from rest_framework import viewsets, generics

from .models import Shop, Category, Comment, Point, ShopPoint
from .serializer import ShopSerializer, PointSerializer, CommentSerializer, ShoppointSerializer

class ShopViewSet(viewsets.ModelViewSet):
    serializer_class = ShopSerializer
    queryset = Shop.objects.filter(lunch__in = [1000, 2000]).all()

class PointViewSet(viewsets.ModelViewSet):
    serializer_class = PointSerializer
    queryset = Point.objects.all()

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

class ShopPointViewSet(viewsets.ModelViewSet):
    serializer_class = ShoppointSerializer
    queryset = ShopPoint.objects.all()

class CategoryFilterViewSet(generics.ListAPIView):
    serializer_class = ShopSerializer
    def get_queryset(self):
        categoryList = ['ラーメン', 'イタリアン', 'カレー', '中華料理', '寿司', 'カフェ', '和食', '日本料理', 'そば', 'うどん', 'とんかつ', 'パスタ'];

        categoryId = self.kwargs['category']
        return Shop.objects.filter(id__in = Category.objects.filter(category__contains = categoryList[int(categoryId)]).values('shop_id')).filter(lunch__in = [1000, 2000]).distinct()

class PointFilterViewSet(generics.ListAPIView):
    serializer_class = ShopSerializer
    def get_queryset(self):
        pointId = self.kwargs['point']
        return Shop.objects.filter(id__in = ShopPoint.objects.filter(point_id = pointId).values('shop_id')).filter(lunch__in = [1000, 2000]).distinct()
