from ..models import PaymentHistory
from rest_framework import serializers


class PaymentHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = PaymentHistory
        fields = "__all__"


# Path: backend/history/api/views.py
