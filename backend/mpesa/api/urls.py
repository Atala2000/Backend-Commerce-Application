from django.urls import path
from .views import OrderHistoryView, initiate_payment, mpesa_callback

urlpatterns = [
    path('mpesa/', initiate_payment, name='initiate_payment'), ##post method
    path('mpesa/callback/', mpesa_callback, name='mpesa_callback'), ##post method
    path('orders/history/', OrderHistoryView.as_view(), name='order_history'), ##get method
]
## callback on possible if the app is hosted on a live server, not on localhost
# Compare this snippet from backend/mpesa/api/serializers.py: