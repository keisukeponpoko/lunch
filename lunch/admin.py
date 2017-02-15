from django.contrib import admin

# Register your models here.
from lunch.models import Shop, Category


class ShopAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'lunch', 'point', 'review', 'latitude', 'longitude')  # 一覧に出したい項目
    list_display_links = ('name',)  # 修正リンクでクリックできる項目
admin.site.register(Shop, ShopAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'shop_id', 'category')  # 一覧に出したい項目
    list_display_links = ('category',)  # 修正リンクでクリックできる項目
admin.site.register(Category, CategoryAdmin)
