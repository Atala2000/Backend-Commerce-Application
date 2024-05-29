import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from ..models import PaymentHistory
from .serializers import PaymentHistorySerializer

class PaymentHistoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        history = PaymentHistory.objects.all()
        serializer = PaymentHistorySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)

    def post(self, request):
        data = json.loads(request.body)
        serializer = PaymentHistorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)
    
class PaymentHistoryDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, transaction_id):
        history = PaymentHistory.objects.filter(transaction_id=transaction_id)
        serializer = PaymentHistorySerializer(history, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    def put(self, request, transaction_id):
        history = PaymentHistory.objects.get(transaction_id=transaction_id)
        data = json.loads(request.body)
        serializer = PaymentHistorySerializer(instance=history, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, safe=False)
        return JsonResponse(serializer.errors, status=400)


    