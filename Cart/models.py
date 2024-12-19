from django.db import models
from Account.models import User
from Products.models import Items

class Order(models.Model):
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 

    def __str__(self):
        return f"Order {self.id} - Total: {self.total_price}"

class OrderItem(models.Model):
    product = models.ForeignKey(Items, on_delete=models.CASCADE)
    order = models.ForeignKey('Order', related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    image_url = models.URLField() 
    quantity = models.PositiveIntegerField()
    size = models.CharField(max_length=50) 
    category = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.name} (x{self.quantity})"
