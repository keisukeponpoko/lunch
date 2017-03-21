# coding: utf-8

from rest_framework import serializers

from .models import Shop, Category, Comment, Point, ShopPoint

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('shop_id', 'category')

class ShoppointSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopPoint
        fields = ('shop_id', 'point_id')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('shop_id', 'comment')

class ShopSerializer(serializers.ModelSerializer):
    category = CategorySerializer(source='category_set', many=True)
    point = ShoppointSerializer(source='shoppoint_set', many=True)
    comment = CommentSerializer(source='comment_set', many=True)

    class Meta:
        model = Shop
        fields = ('id', 'name', 'lunch', 'dinner', 'point', 'review', 'latitude', 'longitude', 'holiday', 'station', 'address', 'url', 'category', 'point', 'comment')

class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = Point
        fields = ('id', 'name')
