from django.conf import settings
from django.db import models
from Account.models import User
from Cart.models import Order
from Products.models import Items

class OrderSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    billing_firstName = models.CharField(max_length=30)
    billing_secondName = models.CharField(max_length=30)
    email = models.EmailField()
    phone_number = models.CharField(max_length=13)
    billing_country = models.CharField(max_length=20)
    billing_state = models.CharField(max_length=20)
    billing_homeaddress = models.CharField(max_length=50)
    billing_postalcode = models.CharField(max_length=6)
    billing_ordernote = models.CharField(max_length=255,null=True, blank=True)
    delivery_firstName = models.CharField(max_length=30)
    delivery_secondName = models.CharField(max_length=30)
    delivery_email = models.EmailField()
    delivery_phoneNumber = models.CharField(max_length=13)
    delivery_country = models.CharField(max_length=20)
    delivery_state = models.CharField(max_length=50)
    delivery_homeaddress = models.CharField(max_length=50)
    delivery_postalcode = models.CharField(max_length=6)
    SHIPPINGMETHOD_CHOICES =[
        ("Air Courier", "Air Courier"),
        ("Land Courier", "Land Courier"),
    ]
    shippingMethod = models.CharField(max_length=20, choices=SHIPPINGMETHOD_CHOICES)
    duties = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)
    PAYMENTMETHOD_CHOICES =[
        ("paystack", "paystack"),
        ("Bank Transfer", "Bank Transfer"),
    ]
    paymentMethod =models.CharField(max_length=20, choices=PAYMENTMETHOD_CHOICES)

    # For Ratings 

class Rating(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    star = models.PositiveIntegerField(choices=[(i, i) for i in range(1, 6)])
    created_at = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255)
    active = models.BooleanField(default= False)

# For Paystack Information    
class PaystackInfo(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    email = models.EmailField()  
    amount = models.DecimalField(max_digits=10, decimal_places=2) 
    reference = models.CharField(max_length=255, unique=True)
    status = models.CharField(max_length=50, default='pending') 
    created_at = models.DateTimeField(auto_now_add=True)  
    updated_at = models.DateTimeField(auto_now=True) 

class Shipping(models.Model):
    ORDER_STATUS = [
        ('Pending', 'Pending'),
        ('Shipped', 'Shipped'),
        ('Delivered', 'Delivered'),
        ('In Transit', 'In Transit'),
    ]
    full_name =models.CharField(max_length=40, default='1')
    dispatchRiderFullName = models.CharField(max_length=50,blank=True, null=True)
    dispatchRiderPhone = models.CharField(max_length=14,blank=True, null=True)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20)
    shipping_status = models.CharField(max_length=20, choices=ORDER_STATUS, default='Pending')
    tracking_number = models.CharField(max_length=100, blank=True, null=True)
    estimated_delivery_date = models.DateField()
