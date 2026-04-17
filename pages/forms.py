from django import forms
from core.models import Testimonio

class TestimonioForm(forms.ModelForm):
    class Meta:
        model = Testimonio
        fields = ['name', 'content', 'rating']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tu nombre'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Cuéntanos tu experiencia...'}),
            'rating': forms.Select(choices=[(i, f"{i} Estrellas") for i in range(1, 6)], attrs={'class': 'form-select'})
        }
        labels = {
            'name': 'Nombre',
            'content': 'Mensaje',
            'rating': 'Calificación'
        }
