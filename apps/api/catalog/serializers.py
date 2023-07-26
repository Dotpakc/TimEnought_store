from rest_framework import serializers

from apps.catalog.models import Category, Image, Product


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.CharField(write_only=True) # додаємо поле slug для запису в БД
    
    class Meta:
        model = Category
        fields=(
            'id',
            'name',
            'slug',
            'description',
            'parent',
            'image',
            'meta_title',
            'meta_description',
            'meta_keywords',
        )
        
class ProductWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price'
        )
        
class ProductReadSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True)
    image_main = serializers.SerializerMethodField(read_only=True)
    images = serializers.SerializerMethodField(read_only=True)
    
    def get_image_main(self, obj):
        serializer = ImageSerializer(obj.main_image(), context=self.context) 
        # context=self.context - передаємо контекст для відображення великих зображень
        # obj.main_image() - викликаємо метод main_image() з моделі Product
        return serializer.data
    
    def get_images(self, obj):
        try:
            images = obj.images().exclude(id = obj.main_image().id)
            serializers = ImageSerializer(images, many=True, context=self.context)
            return serializers.data
        except AttributeError:
            return None
        

    
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'description',
            'quantity',
            'price',
            'category',
            'image_main',
            'images'
        )
 
         
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = (
            'id',
            'image',
            'product',
            'is_main'
        )