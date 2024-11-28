from django.urls import path
from .views import Login, Signup

urlpatterns =[
      path('login/', Login),
      path('signup/', Signup),
]