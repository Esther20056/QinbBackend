from django.db import models
from Account.models import User
from Cart.models import Order

class OrderSummary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    created_at = models.DateTimeField(auto_now_add=True)
    order  = models.ForeignKey(Order,related_name="order_items", on_delete=models.CASCADE) 
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
    delivery_homeaddress = models.CharField(max_length=20)
    delivery_postalcode = models.CharField(max_length=6)
    SHIPPINGMETHOD_CHOICES =[
        ("Air Courier", "Air Courier"),
        ("Land Courier", "Land Courier"),
    ]
    shippingMethod = models.CharField(max_length=20, choices=SHIPPINGMETHOD_CHOICES)
    duties = models.DecimalField(max_digits=10, decimal_places=2, null=True,blank=True)