from django.urls import path
from .views import CategoryView, ProductView, ProductSearchView


urlpatterns = [
	path('category/', CategoryView.as_view(), name='category_view'),
	path('products/', ProductView.as_view(), name='products_list'),
	path('search/', ProductSearchView.as_view(), name='product_search'),
]