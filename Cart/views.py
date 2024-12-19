from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from Products.models import Items
from Account.models import User

@api_view(['POST'])
def CartItemStorage(request):
    if request.method == 'POST':
        cart_data = request.data
        total_price = cart_data['total']
        items = cart_data['items']
        user_id = cart_data.get('user')
        try:
            user = User.objects.get(id=user_id)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_400_BAD_REQUEST)
        
        order = Order.objects.create(total_price=total_price, user=user)
        for item in items:
            try:
                product = Items.objects.get(id=item['id'])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    name=product.name,
                    quantity=item['quantity']
                )
            except Items.DoesNotExist:
                return Response({'error': f"Product with id {item['id']} not found"}, status=status.HTTP_400_BAD_REQUEST)
        order_items = [
            {
                'product_name': item.product.name,
                'quantity': item.quantity,
            }
            for item in order.items.all()  
        ]

        return Response({
            'order_id': order.id,
            'total_price': total_price,
            'order_items': order_items
        }, status=status.HTTP_201_CREATED)
