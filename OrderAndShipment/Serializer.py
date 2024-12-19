from rest_framework import serializers
from .models import OrderSummary, Rating, PaystackInfo, Shipping
from Account.models import User


class OrderSummarySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderSummary
        fields = [
            'billing_firstName', 'billing_secondName', 'email', 'phone_number',
            'billing_country', 'billing_state', 'billing_homeaddress', 'billing_postalcode',
            'billing_ordernote', 'delivery_firstName', 'delivery_secondName', 'delivery_email',
            'delivery_phoneNumber', 'delivery_country', 'delivery_state', 'delivery_homeaddress',
            'delivery_postalcode', 'shippingMethod', 'duties', 'paymentMethod'
        ]

    def validate(self, validated_data):
        if not User.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"email": "Email does not exist."})
        

        if not User.objects.filter(phone_number=validated_data['phone_number']).exists():
            raise serializers.ValidationError({"phone": "Phone number does not exist."})
        
        return validated_data

    def create(self, validated_data):
        email = validated_data['email']
        phone_number = validated_data['phone_number']
        try:
            user_instance = User.objects.get(email=email, phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "non_field_errors": "No user found with the provided email and phone number."
            })
        validated_data['user'] = user_instance

        summary = OrderSummary.objects.create(
            paymentMethod = validated_data['paymentMethod'],
            billing_firstName=validated_data['billing_firstName'],
            billing_secondName=validated_data['billing_secondName'],
            email=validated_data['email'],
            phone_number=validated_data['phone_number'],
            billing_country=validated_data['billing_country'],
            billing_state=validated_data['billing_state'],
            billing_homeaddress=validated_data['billing_homeaddress'],
            billing_postalcode=validated_data['billing_postalcode'],
            billing_ordernote=validated_data.get('billing_ordernote', ''),
            delivery_firstName=validated_data['delivery_firstName'],
            delivery_secondName=validated_data['delivery_secondName'],
            delivery_email=validated_data['delivery_email'],
            delivery_phoneNumber=validated_data['delivery_phoneNumber'],
            delivery_country=validated_data['delivery_country'],
            delivery_state=validated_data['delivery_state'],
            delivery_homeaddress=validated_data['delivery_homeaddress'],
            delivery_postalcode=validated_data['delivery_postalcode'],
            shippingMethod=validated_data['shippingMethod'],
            duties=validated_data.get('duties', ''),
            user=user_instance
        )
        return summary 
    
class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'

class RatingRetrieveSerializer(serializers.ModelSerializer):
    user_first_name = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = Rating
        fields = ['user_first_name', 'star', 'created_at', 'message', 'active']

class PaystackInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PaystackInfo
        fields = ['user', 'email', 'amount', 'reference', 'status']

class ShippingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipping
        fields = ['id', 'full_name', 'shipping_status', 'tracking_number', 'estimated_delivery_date']
