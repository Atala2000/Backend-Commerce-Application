import json
import requests
from django.conf import settings
import logging

PAYPAL_API_BASE = (
    "https://api-m.sandbox.paypal.com"
    if settings.PAYPAL_MODE == "sandbox"
    else "https://api-m.paypal.com"
)

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)


def get_paypal_token():
    url = f"{PAYPAL_API_BASE}/v1/oauth2/token"
    headers = {"Accept": "application/json", "Accept-Language": "en_US"}
    data = {"grant_type": "client_credentials"}
    response = requests.post(
        url,
        headers=headers,
        data=data,
        auth=(settings.PAYPAL_CLIENT_ID, settings.PAYPAL_CLIENT_SECRET),
    )
    response.raise_for_status()
    return response.json()["access_token"]


def create_payment(cart, return_url, cancel_url):
    token = get_paypal_token()
    url = f"{PAYPAL_API_BASE}/v1/payments/payment"

    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}

    amount = float(cart["total_price"])
    items = [
        {
            "name": item["product_name"],
            "sku": str(item["product"]),
            "price": item["price"],
            "currency": "USD",
            "quantity": item["quantity"],
        }
        for item in cart["items"]
    ]

    payload = {
        "intent": "sale",
        "payer": {"payment_method": "paypal"},
        "transactions": [
            {
                "amount": {
                    "total": f"{amount:.2f}",
                    "currency": "USD",
                    "details": {"subtotal": f"{amount:.2f}"},
                },
                "item_list": {"items": items},
                "description": "Purchase from cart",
            }
        ],
        "redirect_urls": {"return_url": return_url, "cancel_url": cancel_url},
    }

    # Log the payload for debugging
    logger.debug("PayPal Payment Payload: %s", json.dumps(payload, indent=2))

    response = requests.post(url, headers=headers, json=payload)

    # Log the response for debugging
    logger.debug("PayPal Response: %s", response.text)

    response.raise_for_status()
    return response.json()


def execute_payment(payment_id, payer_id):
    token = get_paypal_token()
    url = f"{PAYPAL_API_BASE}/v1/payments/payment/{payment_id}/execute"
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}
    payload = {"payer_id": payer_id}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()
