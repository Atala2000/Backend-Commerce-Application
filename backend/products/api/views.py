from rest_framework import generics, permissions
from ..models import Category, Product
from .serializer import CategorySerializer, ProductSerializer

## Category View
class CategoryView(generics.ListAPIView):
    queryset = Category.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = CategorySerializer

## Product View
class ProductView(generics.ListAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

## Product Updtate View by admin only
class UpdateProductView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    permission_classes = [permissions.IsAdminUser]
    serializer_class = ProductSerializer

## Search View
class ProductSearchView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ProductSerializer

    def get_queryset(self):
        query = self.request.query_params.get('q')
        if query:
            return Product.objects.filter(product_name__icontains=query)
        return Product.objects.all()
