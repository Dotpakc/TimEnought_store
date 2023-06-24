from django.urls import path
from .views import *


urlpatterns = [
    path('', CatalogIndexView.as_view(), name='catalog'),
    path('<slug:slug>/', ProductByCategoryView.as_view(), name='category'),
]
