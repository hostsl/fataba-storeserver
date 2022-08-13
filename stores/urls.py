from django.urls import path
from .views import AddStoreView, StoreListView, OwnerStoreView, UpdateStoreView, StoreView, DeleteStoreView

urlpatterns = [
    path('add/', AddStoreView.as_view(), name='add_store'),
    path('list/', StoreListView.as_view(), name='store_list'),
    path('owner/<int:owner_id>/', OwnerStoreView.as_view(), name='owner_store'),
    path('owner/<int:owner_id>/<int:pk>/', StoreView.as_view(), name='owner_store_detail'),
    path('update/<int:owner_id>/<int:pk>/', UpdateStoreView.as_view(), name='update_store'),
    path('delete/<int:owner_id>/<int:pk>/', DeleteStoreView.as_view(), name='delete_store'),
]