from rest_framework.decorators import api_view
from .serializer import loginSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def Signup(request):
 try:
     new_user_serializer = UserSerializer(data=request.data)

     if new_user_serializer.is_valid():
      new_user_serializer.save()
      return Response(new_user_serializer.data, status=status.HTTP_201_CREATED)
     else:
      return Response({"error" :"Input fields can't be empty"}, status=status.HTTP_400_BAD_REQUEST)   
 except BaseException as e: 
      return Response(str(e))

@api_view(['POST'])
def Login(request):
    serializer = loginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data['user']
        user_data = {
            "phone_number": user.phone_number,
            "email": user.email,
            "id": user.id,
        }
        return Response(user_data, status=status.HTTP_200_OK)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
