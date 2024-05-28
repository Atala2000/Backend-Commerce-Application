from rest_framework import serializers
from cart.models import Cart, CartItem
from accounts.models import CustomUser


class CartItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.product_name', read_only=True)
    price = serializers.DecimalField(source='product.price', max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = CartItem
        fields = ['id', 'product', 'product_name', 'price', 'quantity']


class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    user_name = serializers.CharField(source='user.email', read_only=True)
    total_price = serializers.SerializerMethodField()
    ##user_name = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ['id', 'user','user_name', 'created_date', 'items', 'total_price']

    def get_user_name(self, obj):
        return obj.user.last_name

    # def get_total_price(self, obj):
    #     total_price = 0
    #     for item in obj.items.all():
    #         return total_price + item.product.price * item.quantity
    def get_total_price(self, obj):
        total = sum(item.product.price * item.quantity for item in obj.items.all())
        return total

