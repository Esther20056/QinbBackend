from django.urls import path
from .views import OS_view,RateOurProduct,PaystackData,RetrieveRateOurProduct,shipping,shipping_detail

urlpatterns=[
    path('ordersummary/', OS_view),
    path('rateus/', RateOurProduct),
    path('paystackdata/', PaystackData),
    path('retrieve-rate/', RetrieveRateOurProduct),
    path('shipping/', shipping, name='shipping-list'), # get all the orders to be shipped
    path('shipping/<int:pk>/', shipping_detail, name='shipping-detail'),  # fetch specific shipping order
]

