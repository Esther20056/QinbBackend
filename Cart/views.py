from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order, OrderItem
from Products.models import Items


@api_view(['POST'])
def checkout(request):
    if request.method == 'POST':
        cart_data = request.data
        total_price = cart_data['total']
        items = cart_data['items']

        # create the order
        order = Order.objects.create(total_price=total_price)

        # Create the order items
        for item in items:
            try:
                product = Items.objects.get(id=item['id'])
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item['quantity']
                )
            except Items.DoesNotExist:
                return Response({'error': 'Product not found'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'order_id': order.id, 'total_price': total_price}, status=status.HTTP_201_CREATED)

