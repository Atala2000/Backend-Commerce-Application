from rest_framework.response import Response
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from cart.api.serializer import CartItemSerializer, CartSerializer
from cart.models import Cart, CartItem
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from django.http import JsonResponse

## create a view for the cart and cart items
class CartViews(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

## create a view for the cart items
class CartItemViews(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        return CartItem.objects.filter(cart=cart)

    def perform_create(self, serializer):
        cart, created = Cart.objects.get_or_create(user=self.request.user)
        serializer.save(cart=cart)

## clearing the cart
@csrf_exempt
def ClearCart(request):
    if request.method == 'POST':
        try:
            # Get the user's cart
            cart, created = Cart.objects.get_or_create(user=request.user)
            # Delete all items in the cart
            cart.items.all().delete()
            return JsonResponse({'message': 'Cart cleared successfully'}, status=204)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)
