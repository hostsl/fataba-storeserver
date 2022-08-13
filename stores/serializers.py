from rest_framework import serializers
from .models import Store

class AddStoreSerializer(serializers.ModelSerializer):
    ''' Serializer for adding a store in the database... '''
    class Meta:
        model = Store
        fields = [
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
        read_only_fields = ['created_at']

class ViewStoreSerializer(serializers.ModelSerializer):
    ''' Serializer for viewing a store in the database... '''
    class Meta:
        model = Store
        fields = [
            'id', 
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
            'longitude',]
        read_only_fields = ['id']