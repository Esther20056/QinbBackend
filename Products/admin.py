from django.contrib import admin
from .models import Items

class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'image', 'price', 'size', 'category', 'warranty', 'subcategory',  'productCategoryIdentifier', 'description',]  

admin.site.register(Items, ItemsAdmin)