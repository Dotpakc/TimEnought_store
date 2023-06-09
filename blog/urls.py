from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('create/', create, name='create'),
    path('update/<str:slug>/', update, name='article_update'),
    path('random/', random_article, name='random_article'),
    path('', articles_list, name='blog'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag_list'),
    path('<str:slug>/', details, name='details'),
]
