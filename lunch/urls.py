from django.conf.urls import url
from lunch.insert import Insert
from lunch import views

urlpatterns = [
    url(r'^$', views.map),
    url(r'^json/insert$', Insert.json),
    url(r'^shop/get$', views.getShop)
]
