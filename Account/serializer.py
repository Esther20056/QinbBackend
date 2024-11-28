from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate
class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'
                
    def validate(self, data):
      if data["first_name"] == "" and data["email"] == "":
         raise ValueError("Input fields cannot be empty")   

      check_existing_user = User.objects.filter(email = data["email"]).first()
      if check_existing_user is not None:
         raise ValueError("Email already exist")

      else:
         return data
    
    def create(self, data):
            pw = data['password']
            encrypted_pwd = make_password(pw, "wedrfghgfcdxsawsedrtyuuj")
            user = User.objects.create(
            email = data['email'], 
            phone_number = data['phone_number'],
            first_name = data['first_name'],
            last_name = data['last_name'],
            password = encrypted_pwd
      )
            return user

class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')

        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError('Invalid credentials provided')

        return {
            'email': email,
            'user': user
        }
