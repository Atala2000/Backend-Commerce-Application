from django.db import models
from accounts.models import CustomUser

class PaymentHistory(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    transaction_id = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)

    def __str__(self):
        return f"Payment ID: {self.id}, Transaction ID: {self.transaction_id}, Amount: {self.amount}, Status: {self.status}"
