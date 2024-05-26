from django.urls import path
from .views import CategoryView, ProductView, UpdateProductView ,ProductSearchView


urlpatterns = [
	path('category/', CategoryView.as_view(), name='category_view'),
	path('products/', ProductView.as_view(), name='products_list'),
	path('products/<int:pk>/', UpdateProductView.as_view(), name='update_product'),
	path('search/', ProductSearchView.as_view(), name='product_search'),
]