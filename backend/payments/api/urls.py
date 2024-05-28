# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('payment/process/', views.payment_process, name='payment_process'),
    path('payment/execute/', views.payment_execute, name='payment_execute'),
    path('payment/cancel/', views.payment_cancel, name='payment_cancel'),
]
