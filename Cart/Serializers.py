from rest_framework import serializers
from .models import Order, OrderItem, Product

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['product', 'quantity','name']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)

    class Meta:
        model = Order
        fields = ['total_price', 'items']


# from rest_framework import serializers
# from .models import CartItem, Order
# from Account.models import User

# class CartItemSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = CartItem
#         fields = ['product_name', 'product_id', 'quantity', 'price', 'weight', 'size', 'image_url']

# class OrderSerializer(serializers.ModelSerializer):
#     items = CartItemSerializer(many=True)
#     user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

#     class Meta:
#         model = Order
#         fields = ['user', 'items', 'total_price', 'shipping_cost', 'shipping_method', 'billing_address', 'shipping_address', 'email', 'phone', 'status']
