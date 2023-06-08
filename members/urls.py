from django.urls import path

from .views import *

urlpatterns = [
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', logout_view, name='logout'),
    # path('signup/', signup_view, name='signup'),
]
