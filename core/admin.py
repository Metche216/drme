from django.contrib import admin
from .models import User, Testimonio, Appointment

class TestimonioAdmin(admin.ModelAdmin):
    list_display = ('name', 'rating', 'published', 'date')
    list_editable = ('published',)
    list_filter = ('published',)
    search_fields = ('name', 'content')

admin.site.register(User)
admin.site.register(Testimonio, TestimonioAdmin)
admin.site.register(Appointment)
