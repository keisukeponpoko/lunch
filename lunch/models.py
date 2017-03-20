from django.db import models

class Shop(models.Model):
    name = models.CharField('書籍名', max_length=255)
    lunch = models.IntegerField('昼予算', blank=True, default=0)
    dinner = models.IntegerField('夜予算', blank=True, default=0)
    point = models.FloatField('点数', blank=True, default=0)
    review = models.IntegerField('口コミ', blank=True, default=0)
    latitude = models.DecimalField('緯度', max_digits=9, decimal_places=6, default=0)
    longitude = models.DecimalField('経度', max_digits=9, decimal_places=6, default=0)
    holiday = models.CharField('休日', max_length=255)
    station = models.CharField('最寄駅', max_length=255)
    address = models.CharField('住所', max_length=255)
    url = models.CharField('URL', max_length=255)

class Category(models.Model):
    shop_id = models.ForeignKey(Shop, on_delete=models.CASCADE)
    category = models.CharField('カテゴリ', max_length=255)
