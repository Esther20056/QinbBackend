# import random
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from .models import ShippingMethod

# class CalculateShippingPriceView(APIView):
#     def get(self, request, shipping_method_id, weight=None):
#         # Get the shipping method from the database
#         shipping_method = ShippingMethod.objects.get(id=shipping_method_id)
        
#         # Let's say we calculate a base price and adjust based on weight
#         if weight:
#             # Example of weight adjustment, this is just a simple approach:
#             weight_multiplier = 0.1  # price increase per kg, for example
#             price_range = shipping_method.max_price - shipping_method.min_price
#             weight_adjustment = weight * weight_multiplier * price_range
#             price = random.uniform(
#                 shipping_method.min_price + weight_adjustment,
#                 shipping_method.max_price + weight_adjustment
#             )
#         else:
#             # If no weight is provided, just return a random price within the range
#             price = random.uniform(shipping_method.min_price, shipping_method.max_price)
        
#         return Response({
#             'shipping_method': shipping_method.name,
#             'price': round(price, 2),
#             'delivery_time': shipping_method.delivery_time
#         })

