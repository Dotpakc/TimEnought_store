from django.urls import path

from .views import *

urlpatterns = [
    path('search/', search, name='search'),
    path('random/', random_article, name='random_article'),
    path('', articles_list, name='blog'),
    path('create/', create, name='create'),
    path('<str:slug>/update', update, name='articles_update'),
    path('<str:slug>/delete/', delete, name='articles_delete'),
    path('tag/<str:tag>/', articles_tag_list, name='articles_tag_list'),
    path('<str:slug>/', details, name='details'),
]
