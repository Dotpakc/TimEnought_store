from rest_framework import generics, permissions, viewsets, serializers
from apps.order.models import Favorite

from .serializers import FavoriteSerialisers


        
class FavoritesViewSet(viewsets.ModelViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerialisers
    permission_classes = (permissions.IsAuthenticated,)
    
    
    def get_queryset(self):
        return Favorite.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        fav = Favorite.objects.filter(user=self.request.user, product=serializer.validated_data['product'])
        if fav.exists():
            fav.delete()
        else:
            serializer.save(user=self.request.user)
        
        
    def perform_update(self, serializer):
        if Favorite.objects.filter(user=self.request.user, product=serializer.validated_data['product']).exists():
            raise serializers.ValidationError('Товар вже додано до обраного')
        serializer.save(user=self.request.user)
        
    def perform_destroy(self, serializer):
        print(serializer)
        if Favorite.objects.filter(user=self.request.user, product=serializer.product).exists():
            serializer.delete()
        else:
            raise serializers.ValidationError('Товар не знайдено в обраному')
    