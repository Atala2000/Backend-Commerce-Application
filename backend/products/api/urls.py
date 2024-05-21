from django.urls import path
from .views import CategoryView, ProductView


urlpatterns = [
	path('category/', CategoryView.as_view(), name='category_view'),
	path('products/', ProductView.as_view(), name='products_list')
]