from django.urls import path
from .views import getALLBlogPosts, getBlogPost

urlpatterns =[
   path('blogposts/', getALLBlogPosts, name='blog_list'),
   path('blogposts/<int:pk>/', getBlogPost,  name='blog_detail'),
]