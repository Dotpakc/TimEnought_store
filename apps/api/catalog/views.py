from rest_framework import generics, permissions, viewsets
from apps.catalog.models import Category, Product, Image

from .serializers import ProductReadSerializer, ProductWriteSerializer, ImageSerializer, CategorySerializer


class ProductListView(generics.ListAPIView):
    serializer_class = ProductReadSerializer
    
    def get_queryset(self):
        queryset = Product.objects.filter(is_checked=True)
        
        if self.request.query_params.get('category'):
            queryset = queryset.filter(category=self.request.query_params.get('category'))
        
        if self.request.query_params.get('name'):
            queryset = queryset.filter(name__icontains=self.request.query_params.get('name'))
        
        return queryset

class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductReadSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
class ProductCreateView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class ProductUpdateView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductWriteSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class ProductDeleteView(generics.DestroyAPIView):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Product.objects.all()
    
class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    permission_classes = (permissions.IsAdminUser,)
    
class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    serializer_class = CategorySerializer
    queryset = Category.objects.all()