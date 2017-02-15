from lunch.models import Shop, Category
from django.http import HttpResponse
import json
import os.path

class Insert():
    def json(self):
        BASE = os.path.dirname(os.path.abspath(__file__))
        data = open(BASE + "/json/shop.json", 'r')
        jsonData = json.load(data)
        data.close()

        for shopData in jsonData:
            shop = Shop()
            shop.name = shopData['name']
            shop.lunch = shopData['lunch']
            shop.dinner = shopData['dinner']
            shop.point = shopData['point'] if shopData['point'] else 0
            shop.review = shopData['review'] if shopData['point'] else 0
            shop.latitude = shopData['latitude']
            shop.longitude = shopData['longitude']
            shop.holiday = shopData['holiday']
            shop.station = shopData['station']
            shop.address = shopData['address']
            shop.url = shopData['url']
            shop.save()

            for categoryData in shopData['type']:
                category = Category()
                category.shop_id = shop
                category.category = categoryData
                category.save()

        return HttpResponse('ok')
