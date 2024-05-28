import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import create_payment, execute_payment
from cart.models import Cart, CartItem
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@csrf_exempt
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def payment_process(request):
    user = request.user  # Assuming the user is authenticated
    try:
        cart = get_cart_data(user)
        return_url = 'http://localhost:8000/payment/execute/'
        cancel_url = 'http://localhost:8000/payment/cancel/'
        payment = create_payment(cart, return_url, cancel_url)
        for link in payment['links']:
            if link['rel'] == 'approval_url':
                approval_url = link['href']
                return JsonResponse({'approval_url': approval_url})
        return JsonResponse({'error': 'Approval URL not found in PayPal response.'})
    except Exception as e:
        return JsonResponse({'error': str(e)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    try:
        payment = execute_payment(payment_id, payer_id)
        return JsonResponse({'status': 'Payment executed successfully', 'payment': payment})
    except Exception as e:
        return JsonResponse({'error': str(e)})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def payment_cancel(request):
    return JsonResponse({'status': 'Payment cancelled'})

def get_cart_data(user):
    # Fetch the cart and cart items for the user
    cart_items = CartItem.objects.filter(cart__user=user)
    items = [
        {
            "id": item.id,
            "product": item.product.id,
            "product_name": item.product.name,
            "price": f"{item.product.price:.2f}",
            "quantity": item.quantity
        }
        for item in cart_items
    ]
    total_price = sum(item['quantity'] * float(item['price']) for item in items)
    
    return {
        "items": items,
        "total_price": total_price
    }
