# views.py

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import create_payment, execute_payment

@csrf_exempt
def payment_process(request):
    if request.method == 'POST':
        amount = request.POST.get('amount')
        return_url = 'http://localhost:8000/payment/execute/'
        cancel_url = 'http://localhost:8000/payment/cancel/'
        try:
            payment = create_payment(amount, return_url, cancel_url)
            for link in payment['links']:
                if link['rel'] == 'approval_url':
                    approval_url = link['href']
                    return JsonResponse({'approval_url': approval_url})
            return JsonResponse({'error': 'Approval URL not found in PayPal response.'})
        except Exception as e:
            return JsonResponse({'error': str(e)})
    return JsonResponse({'error': 'Invalid request method.'})

def payment_execute(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')
    try:
        payment = execute_payment(payment_id, payer_id)
        return JsonResponse({'status': 'Payment executed successfully', 'payment': payment})
    except Exception as e:
        return JsonResponse({'error': str(e)})

def payment_cancel(request):
    return JsonResponse({'status': 'Payment cancelled'})
