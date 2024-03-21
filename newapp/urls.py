# rental_system/urls.py
from django.urls import path
from .views import AddDataView, UpdateDataView, DeleteDataView

urlpatterns = [
    path('add/', AddDataView.as_view(), name='add_data'),
    path('update/<int:user_id>/', UpdateDataView.as_view(), name='update_data'),
    path('delete/<int:user_id>/', DeleteDataView.as_view(), name='delete_data'),
]
