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


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from rest_framework import status
# from Account.models import User
# from django.shortcuts import redirect
# from .models import CartItem, Order
# from .Serializers import OrderSerializer

# @api_view(['POST'])
# def checkout(request):
#     # Extract the order data from the request body
#     data = request.data

#     # Check if the email and phone number already exist in the system
#     email = data.get('email')
#     phone = data.get('phone')

#     if not email or not phone:
#         return Response({"error": "Email and phone number are required."}, status=status.HTTP_400_BAD_REQUEST)

#     # Check if the user already exists by email or phone number
#     try:
#         user = User.objects.get(email=email)
#         if user.profile.phone == phone:
#             # If user exists and phone matches, continue with the order creation
#             pass
#         else:
#             return Response({"error": "Phone number does not match our records."}, status=status.HTTP_400_BAD_REQUEST)
#     except User.DoesNotExist:
#         # If user does not exist, redirect to the login/signup page
#         return Response({"error": "User does not exist. Please login or signup."}, status=status.HTTP_401_UNAUTHORIZED)

#     # Process Cart items and create order
#     cart_items_data = data.get('items', [])
#     cart_items = []
#     for item_data in cart_items_data:
#         cart_item = CartItem.objects.create(**item_data)
#         cart_items.append(cart_item)

#     # Calculate total price and shipping cost
#     total_price = sum(item['price'] * item['quantity'] for item in cart_items_data)
#     shipping_cost = data.get('shipping_cost', 0)
#     total_with_shipping = total_price + shipping_cost

#     # Create the order
#     order_data = {
#         'user': user,
#         'items': cart_items,
#         'total_price': total_price,
#         'shipping_cost': shipping_cost,
#         'shipping_method': data.get('shipping_method'),
#         'billing_address': data.get('billing_address'),
#         'shipping_address': data.get('shipping_address'),
#         'email': email,
#         'phone': phone
#     }

#     order_serializer = OrderSerializer(data=order_data)
#     if order_serializer.is_valid():
#         order = order_serializer.save()
#         return Response(order_serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# views.py
# import json
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import Order, CartItem

# @login_required
# def checkout(request):
#     if request.method == 'POST':
#         # Only logged-in users can access this
#         data = json.loads(request.body)
#         try:
#             # Now, request.user will always be an authenticated User instance
#             order = Order.objects.create(
#                 user=request.user,  # Ensure order is linked to the authenticated user
#                 total_price=data['total_price'],
#                 shipping_cost=data['shipping_cost'],
#                 shipping_method=data['shipping_method'],
#                 billing_address=data['billing_address'],
#                 shipping_address=data['shipping_address'],
#                 email=data['email'],  # You can keep this for email-related notifications
#                 phone=data['phone'],  # Store phone number as well
#             )

#             # Add items to the order
#             for item_data in data['items']:
#                 CartItem.objects.create(
#                     order=order,
#                     product_name=item_data['product_name'],
#                     quantity=item_data['quantity'],
#                     price=item_data['price'],
#                     weight=item_data['weight'],
#                     size=item_data['size'],
#                     image_url=item_data['image_url'],
#                 )

#             return JsonResponse({'message': 'Order created successfully'}, status=201)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)


# import json
# from django.contrib.auth.decorators import login_required
# from django.http import JsonResponse
# from .models import Order, CartItem

# @login_required
# def checkout(request):
#     if request.method == 'POST':
#         # Only logged-in users can access this
#         data = json.loads(request.body)
#         try:
#             #  request.user will always be an authenticated User instance
#             order = Order.objects.create(
#                 user=request.user, 
#                 total_price=data['total_price'],
#                 shipping_cost=data['shipping_cost'],
#                 shipping_method=data['shipping_method'],
#                 billing_address=data['billing_address'],
#                 shipping_address=data['shipping_address'],
#                 email=data['email'], 
#                 phone=data['phone'],  
#             )
#             for item_data in data['items']:
#                 CartItem.objects.create(
#                     order=order,
#                     product_name=item_data['product_name'],
#                     quantity=item_data['quantity'],
#                     price=item_data['price'],
#                     weight=item_data['weight'],
#                     size=item_data['size'],
#                     image_url=item_data['image_url'],
#                 )

#             return JsonResponse({'message': 'Order created successfully'}, status=201)

#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=400)
