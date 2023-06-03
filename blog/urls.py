from django.urls import path

from .views import *

urlpatterns = [
    path('<str:slug>/', details, name='details'),
    path('random/', random_article, name='random_article'),
    path('', articles_list, name='blog'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag_list'),
]
