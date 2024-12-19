from django.contrib import admin
from .models import Rating,Shipping

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('user', 'star', 'message', 'active', 'created_at')
    list_filter = ('active', 'created_at') 
    search_fields = ('user__first_name', 'message') 
    actions = ['activate_ratings'] 

    def activate_ratings(self, request, queryset):
        queryset.update(active=True)
        self.message_user(request, f'{queryset.count()} rating(s) have been activated.')
    
    activate_ratings.short_description = "Activate selected ratings"

@admin.register(Shipping)
class ShippingAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'dispatchRiderFullName', 'dispatchRiderPhone', 'total_amount', 'payment_status', 'shipping_status', 'tracking_number', 'estimated_delivery_date')
    list_editable = ('payment_status', 'shipping_status', 'tracking_number') 