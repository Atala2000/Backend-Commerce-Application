import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from cart.api.serializer import CartSerializer
from cart.models import Cart, CartItem
from mpesa.models import Order, OrderItem
from accounts.models import CustomUser
from .utils import lipa_na_mpesa_online
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from .serializers import OrderSerializer
from decimal import Decimal
import logging

#user = get_user_model()

@csrf_exempt
@login_required
def initiate_payment(request):
    cart = Cart.objects.get(user=request.user)
    cart_items = CartItem.objects.filter(cart=cart)
    total_price = CartSerializer(cart).data['total_price']
    phone_number = request.user.phone  ##later change it to request.user.phone_number
    total_price = float(total_price) #converting to float
    response = lipa_na_mpesa_online(phone_number, total_price, f'Cart-{cart.id}', 'Payment for cart items')
    #print(response)
    return JsonResponse(response)


@csrf_exempt
def mpesa_callback(request):
    #print(request.body)

    try:
        print("Mpesa Callback")

        # Check if the request body is empty
        if not request.body:
            print("Empty request body")
            return JsonResponse({'error': 'Empty request body'}, status=400)

        body_unicode = request.body.decode('utf-8')
        data = json.loads(body_unicode)

        print(f"Rceived data: {data}")

        if data['Body']['stkCallback']['ResultCode'] == 0:
            phone_number = data['Body']['stkCallback']['CallbackMetadata']['Item'][4]['Value']

            print(f"Phone number: {phone_number}")

            try:
                user = CustomUser.objects.get(phone=phone_number)

                print(f"User: {user}")

                cart = Cart.objects.get(user=user)
                cart_items = CartItem.objects.filter(cart=cart)

                print(f"Cart items: {cart_items}")

                total_price = sum(item.product.price * item.quantity for item in cart_items)

                order = Order.objects.create(user=user, total_price=total_price)

                for item in cart_items:
                    OrderItem.objects.create(
                        order=order,
                        product=item.product,
                        quantity=item.quantity,
                        price=item.product.price
                    )

                cart_items.delete()

                return JsonResponse({'message': 'Payment completed successfully, order created.'})
            except user.DoesNotExist:
                return JsonResponse({'error': 'User not found.'}, status=404)
            except Cart.DoesNotExist:
                return JsonResponse({'error': 'Cart not found.'}, status=404)
            except Exception as e:
                print(e)
                return JsonResponse({'error': 'An error occurred.'}, status=500)
        else:
            print(f"Payment failed: {data['Body']['stkCallback']['ResultDesc']}")
            return JsonResponse({'error': 'Payment failed.'}, status=400)
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {str(e)}")
        return JsonResponse({'error': 'Invalid JSON.'}, status=400)
    except KeyError as e:
        return JsonResponse({'error': f'KeyError: {e}'}, status=400)
    except Exception as e:
        return JsonResponse({'error': f'An error occurred: {e}'}, status=500)

class OrderHistoryView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        #print(user)
        return Order.objects.select_related('user').filter(user=user).prefetch_related('items').order_by('-created_at')
