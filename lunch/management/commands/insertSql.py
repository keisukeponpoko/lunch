# -*- coding:utf-8 -*-

from django.core.management.base import BaseCommand
from lunch.models import Shop, Category


# BaseCommandを継承して作成
class Command(BaseCommand):
    # python manage.py help insertSqlで表示されるメッセージ
    help = 'Insert Data to MySql'

    # コマンドライン引数を指定します。(argparseモジュール https://docs.python.org/2.7/library/argparse.html)
    def add_arguments(self, parser):
        parser.add_argument('type', nargs='?', type=int)

    # コマンドが実行された際に呼ばれるメソッド
    def handle(self, *args, **options):
        self.insertData()

    def insertData(self):
        for shopData in self.getJson('shop'):
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

        print('finish')

    def getJson(self, filename):
        import json
        import os.path

        base = os.path.dirname(os.path.abspath(__file__))
        name = os.path.normpath(os.path.join(base, '../../json/' + filename + '.json'))
        data = open(name, 'r')
        jsonData = json.load(data)
        data.close()
        return jsonData
