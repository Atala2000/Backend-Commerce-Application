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

class ProductSearchView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Product.objects.filter(product_name__icontains=query)
        return Product.objects.all()
