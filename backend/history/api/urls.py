# urls.py

from django.urls import path
from . import views

urlpatterns = [
    path("history/", views.PaymentHistoryView.as_view(), name="history"),
    path("history/<str:transaction_id>/", views.PaymentHistoryDetailView.as_view(), name="history_detail"),
]