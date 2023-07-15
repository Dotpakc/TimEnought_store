from django.contrib.auth import get_user_model,authenticate
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed

from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import UserSerializer, LoginSerializer, TokenSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = get_user_model().objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

