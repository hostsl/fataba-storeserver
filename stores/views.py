from rest_framework import generics, status
from rest_framework.response import Response

from .models import Store, Categories
from .serializers import AddStoreSerializer, ViewStoreSerializer

class AddStoreView(generics.CreateAPIView):
    ''' View for adding a store... '''
    queryset = Store.objects.all()
    serializer_class = AddStoreSerializer
    # permission_classes = [IsOwnerOrReadOnly,]
    # authentication_classes = (TokenAuthentication, SessionAuthentication)

    # Check if store exists for user and create if not.
    def post(self, request, *args, **kwargs):
        owner_id=request.data.get('owner_id')
        name=request.data.get('name')
        address=request.data.get('address')
        description=request.data.get('description')
        category=request.data.get('category')
        email=request.data.get('email')
        phone_number=request.data.get('phone_number')
        open_hour=request.data.get('open_hour')
        close_hour=request.data.get('close_hour')
        site_url=request.data.get('site_url')
        latitude=request.data.get('latitude')
        longitude=request.data.get('longitude')
        created_at=request.data.get('created_at')

        try:
            store = Store.objects.get(name=name)
            return Response({"error": "Store already exists"}, status=status.HTTP_400_BAD_REQUEST)
                
        except Store.DoesNotExist:
            store = Store.objects.create(
                owner_id=owner_id, name=name, 
                address=address, description=description, 
                category=category, email=email, 
                phone_number=phone_number, open_hour=open_hour, 
                close_hour=close_hour, site_url=site_url, 
                latitude=latitude, longitude=longitude, created_at=created_at)
            return Response({"message": "Store created successfully"}, status=status.HTTP_201_CREATED)

class StoreListView(generics.ListAPIView):
    ''' View for listing all stores. '''
    queryset = Store.objects.all()
    serializer_class = ViewStoreSerializer
    # permission_classes = [IsAuthenticated,]
    # authentication_classes = (SessionAuthentication,)

    # def get_queryset(self):
    #     queryset = Store.objects.all()
    #     owner_id = self.request.owner_id
    #     if owner_id.is_anonymous:
    #         return queryset
    #     else:
    #         return queryset.filter(owner_id=owner_id)

# Retrieve the owner_id from the url and return the stores.
class OwnerStoreView(generics.ListAPIView):
    ''' View for listing stores by owner. '''
    serializer_class = ViewStoreSerializer

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        return Store.objects.filter(owner_id=owner_id)

# List store by its id and owner_id from the url.
class StoreView(generics.ListAPIView):
    ''' View for listing a store by id. '''
    serializer_class = ViewStoreSerializer

    def get_queryset(self):
        owner_id = self.kwargs['owner_id']
        store_id = self.kwargs['pk']
        return Store.objects.filter(owner_id=owner_id, id=store_id)
        
# Update store by its id and owner_id from the url.
class UpdateStoreView(generics.UpdateAPIView):
    ''' View for updating a store by id. '''
    queryset = Store.objects.all()
    serializer_class = AddStoreSerializer

    def put(self, request, *args, **kwargs):
        owner_id = self.kwargs['owner_id']
        store_id = self.kwargs['pk']
        name = request.data.get('name')
        address = request.data.get('address')
        description = request.data.get('description')
        category = request.data.get('category')
        email = request.data.get('email')
        phone_number = request.data.get('phone_number')
        open_hour = request.data.get('open_hour')
        close_hour = request.data.get('close_hour')
        site_url = request.data.get('site_url')
        latitude = request.data.get('latitude')
        longitude = request.data.get('longitude')

        try:
            store = Store.objects.get(owner_id=owner_id, id=store_id)
            store.name = name
            store.address = address
            store.description = description
            store.category = category
            store.email = email
            store.phone_number = phone_number
            store.open_hour = open_hour
            store.close_hour = close_hour
            store.site_url = site_url
            store.latitude = latitude
            store.longitude = longitude
            store.save()
            return Response({"message": "Store updated successfully"}, status=status.HTTP_200_OK)
        except Store.DoesNotExist:
            return Response({"error": "Store does not exist"}, status=status.HTTP_400_BAD_REQUEST)

# Delete store by its id and owner_id from the url.
class DeleteStoreView(generics.DestroyAPIView):
    ''' View for deleting a store by id. '''
    queryset = Store.objects.all()
    serializer_class = AddStoreSerializer

    def delete(self, request, *args, **kwargs):
        owner_id = self.kwargs['owner_id']
        store_id = self.kwargs['pk']

        try:
            store = Store.objects.get(owner_id=owner_id, id=store_id)
            store.delete()
            return Response({"message": "Store deleted successfully"}, status=status.HTTP_200_OK)
        except Store.DoesNotExist:
            return Response({"error": "Store does not exist"}, status=status.HTTP_400_BAD_REQUEST)