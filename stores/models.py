from django.db import models

Categories = (
    ('Arts', 'Arts'),
    ('African Fashion & Fabric', 'African Fashion & Fabric',),
    ('Bars/Lounges', 'Bars/Lounges'),
    ('Beauty Supply', 'Beauty Supply'),
    ('Coffee', 'Coffee'),
    ('Grocery', 'Grocery'),
    ('Information Technology', 'Information Technology',),
    ('Restaurants', 'Restaurants'),
    ('Salons/Barbershops', 'Salons/Barbershops'),
    ('Others', 'Others'),

)

class Store(models.Model):
    ''' Stores database modelling... '''
    owner_id = models.IntegerField()
    name = models.CharField(max_length=100, blank=False)
    address = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    category = models.CharField(max_length=100, choices=Categories, default='Restaurants')
    email = models.EmailField(max_length=100)
    phone_number = models.CharField(max_length=100)
    open_hour = models.TimeField(blank=False)
    close_hour = models.TimeField(blank=False)
    site_url = models.URLField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)