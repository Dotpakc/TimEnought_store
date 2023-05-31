from django.urls import path

from .views import details, random_article, articles_list

urlpatterns = [
    path('<int:id>/', details, name='details'),
    path('random/', random_article, name='random_article'),
    path('', articles_list, name='blog'),
]
