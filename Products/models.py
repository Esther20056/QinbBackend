from django.db import models


class Items(models.Model):
    name =models.CharField(max_length=50)
    image=models.ImageField(upload_to="ProductImages")
    size=models.CharField(max_length=20, blank=True, null=True)
    promo_price=models.DecimalField(decimal_places=2, max_digits=12, default="1")
    price=models.DecimalField(decimal_places=2, max_digits=12)
    warranty=models.CharField(max_length=60, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    productCategoryIdentifier = models.CharField(max_length=20, blank=True, null=True)
    subcategory = models.CharField(max_length=20, blank=True, null=True) 
    weight = models.CharField(max_length=8,null=True, blank=True)  
    color = models.CharField(max_length=20, default='color')

