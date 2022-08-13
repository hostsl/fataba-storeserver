from django.contrib import admin

from .models import Store

class CustomStoresAdmin(admin.ModelAdmin):
    model = Store
    list_display = [
        'owner_id', 
        'name', 
        'address', 
        'description', 
        'category', 
        'email', 
        'phone_number', 
        'open_hour', 
        'close_hour', 
        'site_url', 
        'latitude', 
        'longitude', 
        'created_at']
    list_filter = ['owner_id', 'name', 'category',]
    search_fields = ['owner_id', 'name', 'category',]
    ordering = ['owner_id', 'name', 'category',]

admin.site.register(Store, CustomStoresAdmin)

