from django.contrib.auth import get_user_model
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['url','id', 'username', 'email', 'groups', 'image', 'phone']
   

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=255)
    
    class Meta:
        fields = ('username', 'password')
        

class TokenSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    
    class Meta:
        fields = ('token',)