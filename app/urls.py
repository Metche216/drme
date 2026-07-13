from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from pages import views


urlpatterns = [
    path('healthz/', lambda request: HttpResponse('OK'), name='healthcheck'),
    path('', views.index, name='index'),
    path('cirugias/', views.surgeries, name='surgeries'),
    path('diagnostico/', views.diagnostic, name='diagnostic'),
    path('acerca/', views.about, name='about'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('turnos/', include('appointments.urls')),
    path('testimonios/', views.testimonials, name='testimonials'),
    path('mod/testimonios/', views.moderator_dashboard, name='moderator_dashboard'),
    path('mod/testimonios/<int:pk>/approve/', views.approve_testimonial, name='approve_testimonial'),
]
