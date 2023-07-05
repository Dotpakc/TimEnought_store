from django.urls import path
from .views import *


urlpatterns = [
    path('add/', add_to_cart, name='add_to_cart')

]
