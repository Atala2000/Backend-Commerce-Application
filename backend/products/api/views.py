from rest_framework import generics, permissions
from ..models import Category, Product
from .serializer import CategorySerializer, ProductSerializer


class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer