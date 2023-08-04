from django.urls import path
from .views import *


urlpatterns = [
    path('', frontpage, name='index'),
    path('about/', about, name='about'),
    path('page/<slug:slug>/', PageDetailView.as_view(), name='page'),
    path('autocomplete/', autocomplete , name='autocomplete'),
]
