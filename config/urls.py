"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from rest_framework import routers
from apps.api.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls')),
    path('blog/', include('apps.blog.urls')),
    path('members/', include('apps.members.urls')), 
    path('shop/', include('apps.shop.urls')),
    path('catalog/', include('apps.catalog.urls')),
    path('order/', include('apps.order.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/v2/', include('apps.api.urls')),
    path('api/', include(router.urls)),
    path("__debug__/", include("debug_toolbar.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
