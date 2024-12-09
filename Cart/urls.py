from django.urls import path
from .views import CartItemStorage

urlpatterns = [
    path('cartItemStorage/', CartItemStorage, name='checkout'),
]
