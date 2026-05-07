from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('cancel/<int:appointment_id>/', views.cancel_appointment, name='cancel_appointment'),
    path('api/sync/', views.api_sync_appointments, name='api_sync_appointments'),
    path('api/slots/', views.api_available_slots, name='api_available_slots'),
    path('api/book/', views.api_book_appointment, name='api_book_appointment'),
    path('api/profile/', views.api_save_profile, name='api_save_profile'),
]