from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from pages import views
from django.contrib.sitemaps.views import sitemap
from pages.sitemaps import StaticViewSitemap

sitemaps = {
    'static': StaticViewSitemap,
}

ROBOTS_TXT = """User-agent: *
Disallow: /login/
Disallow: /admin/
Disallow: /gestion-interna-dr/
Sitemap: https://www.matiasetcheverry.com/sitemap.xml
"""


urlpatterns = [
    # Admin portal moved to a non-standard URL for security
    path('gestion-interna-dr/', admin.site.urls),
    path('healthz/', lambda request: HttpResponse('OK'), name='healthcheck'),
    path('robots.txt', lambda r: HttpResponse(ROBOTS_TXT, content_type="text/plain")),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    path('entry.worker.js', lambda r: HttpResponse("self.addEventListener('install', () => { self.skipWaiting(); }); self.addEventListener('activate', () => { self.registration.unregister(); });", content_type='application/javascript')),
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
    path('privacidad/', views.privacidad, name='privacidad'),
    path('terminos/', views.terminos, name='terminos'),
]
