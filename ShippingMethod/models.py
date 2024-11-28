# from django.db import models

# class ShippingMethod(models.Model):
#     # Define shipping choices with both value and display name
#     SHIPPING_CHOICES = (
#         ('land_courier', 'Land Courier'),
#         ('air_courier', 'Air Courier'),
#     )

#     name = models.CharField(
#         max_length=100,
#         choices=SHIPPING_CHOICES,  # This links the choices to the `name` field
#         default='land_courier',     # Default value can be set (if needed)
#     )
#     description = models.CharField(max_length=255)
#     min_price = models.DecimalField(max_digits=10, decimal_places=2)
#     max_price = models.DecimalField(max_digits=10, decimal_places=2)
#     delivery_time = models.CharField(max_length=50)

#     def __str__(self):
#         return self.name


