from django.contrib import admin
from django.urls import path, include
from pages import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("callback", views.callback, name="callback"),
    path('turnos/', include('appointments.urls')),

]
