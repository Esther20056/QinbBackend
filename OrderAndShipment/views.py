from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Serializer import OrderSummarySerializer,RatingRetrieveSerializer,RatingSerializer,PaystackInfoSerializer,ShippingSerializer
from django.contrib.auth import get_user_model
from .models import Rating, PaystackInfo, Shipping
import requests 


@api_view(['POST'])
def OS_view(request):
    if request.method == 'POST':
        data = request.data.copy()
        data['user'] = request.user.id  
        
        serializer = OrderSummarySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Order placed successfully!'}, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 #For Rating

@api_view(['POST'])
def RateOurProduct(request):
   serializer= RatingSerializer(data=request.data)

   if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_200_OK)
   
   else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def RetrieveRateOurProduct(request):
    ratings = Rating.objects.filter(active=True).all().order_by('-created_at')
    serializer = RatingRetrieveSerializer(ratings, many=True)
    return Response(serializer.data)

def verify_paystack_payment(reference):
    url = f'https://api.paystack.co/transaction/verify/{reference}'
    headers = {
        'Authorization': 'Bearer sk_test_27890b8692296de13aef5a838c7d2d3a360a150a', 
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        transaction_data = response.json()  
        if transaction_data['data']['status'] == 'success': 
            return True, transaction_data['data']
    return False, response.json()

@api_view(['POST'])
def PaystackData(request):
    user_id = request.data.get('user')  
    email = request.data.get('email')  
    amount = request.data.get('amount') 
    reference = request.data.get('reference') 
    User = get_user_model()  
    try:
        user = User.objects.get(id=user_id) 
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=400)

    try:
      
        amount = float(amount) 
    except ValueError:
        return Response({'error': 'Invalid amount format'}, status=400)

    transaction = PaystackInfo.objects.create(
        user=user, 
        email=email,
        amount=amount / 100, 
        reference=reference,
        status='success',  
    )
    serializer = PaystackInfoSerializer(transaction)

    return Response({'message': 'Payment successful', 'transaction_data': serializer.data})

@api_view(['GET'])
def shipping(request):
    shipping_orders = Shipping.objects.all()
    serializer = ShippingSerializer(shipping_orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def shipping_detail(request, pk):
    try:
        order = Shipping.objects.get(pk=pk)
    except Shipping.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = ShippingSerializer(order)
    return Response(serializer.data)


