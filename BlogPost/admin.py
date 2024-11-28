from django.contrib import admin
from .models import BlogPost, BlogPostImage

admin.site.register(BlogPost)
admin.site.register(BlogPostImage)
