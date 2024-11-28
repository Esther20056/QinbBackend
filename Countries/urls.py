
from django.urls import path
from .views import saveCountry

urlpatterns = [
    path('save-country/', saveCountry, name='save-country'),
]