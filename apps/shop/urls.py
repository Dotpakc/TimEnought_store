from django.urls import path

from .views import *


urlpatterns = [
    path('', ShopList.as_view(), name='product_list'),
    path('<slug:slug>/', ProductDetail.as_view(), name='product_detail'),
]
