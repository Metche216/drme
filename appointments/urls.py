from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_appointments, name='list_appointments'),
    path('api/appointments/', views.api_fetch_appointments, name='api_get_appointments'),
]