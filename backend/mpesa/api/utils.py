import requests
from django.conf import settings
from requests.auth import HTTPBasicAuth
import base64
from datetime import datetime
import logging
from decimal import Decimal


logger = logging.getLogger(__name__)

def get_mpesa_access_token():
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    api_URL = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    r = requests.get(api_URL, auth=HTTPBasicAuth(consumer_key, consumer_secret))
    mpesa_access_token = r.json()["access_token"]
    #logger.debug(f"Access_token: {mpesa_access_token}")
    return mpesa_access_token

def lipa_na_mpesa_online(phone_number, amount, reference, callback_url):
    #logger.debug(f"Initiating M-Pesa payment for phone number: {phone_number}, amount: {amount}")

    access_token = get_mpesa_access_token()
    api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {
		"Authorization": f"Bearer {access_token}",
		"Content-Type": "application/json"
	}
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    business_short_code = settings.MPESA_SHORTCODE
    passkey = settings.MPESA_PASSKEY
    password = base64.b64encode(f"{business_short_code}{passkey}{timestamp}".encode()).decode('utf-8')

    #logger.debug(f"Password: {password}, Timestamp: {timestamp}")

    request = {
		"BusinessShortCode": 174379,
		"Password": password,
		"Timestamp": timestamp,
		"TransactionType": "CustomerPayBillOnline",
		"Amount": amount,
		"PartyA": phone_number,
		"PartyB": 174379,
		"PhoneNumber": phone_number,
		"CallBackURL": "https://mydomain.com/path",
		"AccountReference": "CompanyXLTD",
		"TransactionDesc": "Payment of X"
	}
    response = requests.post(api_url, json=request, headers=headers)
    return response.json()

    # access_token = get_mpesa_access_token()
    # api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
    # headers = {
	# 	"Authorization": f"Bearer {access_token}",
	# 	"Content-Type": "application/json"
	# }

    # # register_url_payload = {
	# # 	"shortCode": settings.MPESA_SHORTCODE,
	# # 	"responseType": "Completed",
	# # 	"confirmURL": settings.MPESA_CONFIRMATION_URL,
	# # 	"validationURL": settings.MPESA_VALIDATION_URL
	# # }
    # # response = requests.post(api_url, json=register_url_payload,headers=headers)
    # # response.raise_for_status()


    # simulate_payload = {
	# 	"shortCode": settings.MPESA_SHORTCODE,
	# 	"commandID": "CustomerBuyGoodsOnline",
	# 	"amount": amount,
	# 	"msisdn": phone_number,
	# 	"billRefNumber": reference
	# }

    # simulate_response = requests.post(api_url, json=simulate_payload, headers=headers)
    # return simulate_response.json()
