from rest_framework import serializers
from ..models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_id', 'category_name', 'created_date']


class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.ReadOnlyField(source='category.category_name')

    class Meta:
        model = Product
        fields = ['product_id', 'product_name', 'description', 'price', 'availability', 'category_name', 'images' ]
