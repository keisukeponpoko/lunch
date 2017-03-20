# coding: utf-8

from rest_framework import serializers

from .models import Shop, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('shop_id', 'category')

class ShopSerializer(serializers.ModelSerializer):
    category = CategorySerializer(source='category_set', many=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'lunch', 'dinner', 'point', 'review', 'latitude', 'longitude', 'holiday', 'station', 'address', 'url', 'category')
