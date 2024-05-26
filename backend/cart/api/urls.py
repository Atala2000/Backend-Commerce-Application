from django.urls import path

from cart.api.views import CartItemViews, CartViews
#from .views import CartView, CartItemView


urlpatterns = [
	path('cart/', CartViews.as_view(), name='cart_view'),
	path('cart-items/', CartItemViews.as_view(), name='cart_item_view')
]
