from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .Serializer import OrderSummarySerializer


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
