from django.db import models
from products.models import Product


# Create your models here.
class Order(models.Model):
    user = models.ForeignKey('accounts.CustomUser', on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f' Order #{self.pk} - User: {self.user.email} - Total Price: {self.total_price}' ## to be updated to user.username

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self) -> str:
        return f'Order Item #{self.pk} - Order: {self.order.pk} - Product: {self.product.name} - Quantity: {self.quantity} - Price: {self.price}'

