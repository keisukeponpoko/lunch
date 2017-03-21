# coding: utf-8

from rest_framework import routers
from .views import ShopViewSet, PointViewSet, CommentViewSet, ShopPointViewSet

router = routers.DefaultRouter()
router.register(r'shops', ShopViewSet)
router.register(r'points', PointViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'shoppoints', ShopPointViewSet)
