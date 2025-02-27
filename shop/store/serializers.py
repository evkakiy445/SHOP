from rest_framework import serializers
from .models import Category, Product, ProductImage
from django.conf import settings

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductImageSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=True)
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'image_url', 'product']

    def get_image_url(self, obj):
        if obj.image:
            return settings.MEDIA_URL + str(obj.image)
        return None

    def create(self, validated_data):
        product = validated_data.get('product')
        if not product:
            raise serializers.ValidationError("Product is required for ProductImage.")

        return super().create(validated_data)

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'
