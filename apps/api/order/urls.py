from django.urls import path, include
from .views import FavoritesViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    

]

router = DefaultRouter()
router.register(r'favorites', FavoritesViewSet, basename='favorites')
urlpatterns += router.urls


