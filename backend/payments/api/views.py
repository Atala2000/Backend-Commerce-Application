import json
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .utils import create_payment, execute_payment
from history.models import PaymentHistory
from cart.models import CartItem
from accounts.models import CustomUser
import logging

# Configure logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(level=logging.DEBUG)


@csrf_exempt
@api_view(["POST"])  # Ensure only POST requests are allowed
@permission_classes([IsAuthenticated])
def payment_process(request):
    user = request.user  # Assuming the user is authenticated
    try:
        cart = get_cart_data(user)
        return_url = "http://localhost:8000/payment/execute/"
        cancel_url = "http://localhost:8000/payment/cancel/"
        payment = create_payment(cart, return_url, cancel_url)
        for link in payment["links"]:
            if link["rel"] == "approval_url":
                approval_url = link["href"]
                return JsonResponse({"approval_url": approval_url})
        return JsonResponse({"error": "Approval URL not found in PayPal response."})
    except Exception as e:
        # logger.error("Payment process error: %s", str(e))
        return JsonResponse({"error": str(e)})


@api_view(["GET"])
def payment_execute(request):
    payment_id = request.GET.get("paymentId")
    payer_id = request.GET.get("PayerID")
    try:
        payment = execute_payment(payment_id, payer_id)
        # Create a new payment history entry
        response = create_history(payment)
        return JsonResponse(
            {
                "response": payment,
            }
        )
    except Exception as e:
        # logger.error("Payment execute error: %s", str(e))
        return JsonResponse({"error": str(e)})


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def payment_cancel(request):
    return JsonResponse({"status": "Payment cancelled"})


def get_cart_data(user):
    # Fetch the cart and cart items for the user
    cart_items = CartItem.objects.filter(cart__user=user)
    items = [
        {
            "id": item.id,
            "product": item.product.product_id,  # Adjusted to use product_id
            "product_name": item.product.product_name,  # Adjusted to use product_name
            "price": f"{item.product.price:.2f}",
            "quantity": item.quantity,
        }
        for item in cart_items
    ]
    total_price = sum(item["quantity"] * float(item["price"]) for item in items)

    return {"items": items, "total_price": total_price}



def create_history(response):
    try:
        # Extract payment details
        payment_id = response["id"]
        transaction_amount = response["transactions"][0]["amount"]["total"]
        payer_email = response["payer"]["payer_info"]["email"]

        # Process payer shipping address (if available)
        shipping_address = response["payer"]["payer_info"].get("shipping_address", {})

        # Process payment status
        payment_status = response["state"]

        user = CustomUser.objects.get(email=payer_email)

        # Create a new payment history entry
        payment = PaymentHistory.objects.create(
            user=user,
            transaction_id=payment_id,
            amount=transaction_amount,
            status=payment_status
            # You can add more attributes as needed
        )

        # Return a success response
        return JsonResponse({"success": True})

    except KeyError as e:
        # Handle missing keys in the response
        print("Error:", e)
        return JsonResponse({"error": str(e)}, status=400)

    except Exception as e:
        # Handle other exceptions
        print("Error:", e)
        return JsonResponse({"error": "Internal server error"}, status=500)

