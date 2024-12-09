from django.urls import path
from .views import OS_view

urlpatterns=[
    path('ordersummary/', OS_view)
]