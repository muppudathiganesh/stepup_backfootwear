from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, ContactMessage

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
    #------------------- product-------------------------
from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    #  image = serializers.ImageField(use_url=True)
     class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'price', 'mrp', 'image', 'category', 'style', 'color']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug']
# -------------contact-------------------------
class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = '__all__'
