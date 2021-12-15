from django.contrib.auth.models import User
from django import forms
from django.forms.widgets import NumberInput, PasswordInput
from .fields import EEmailInput
from django.contrib.auth.forms import UserCreationForm

from .models import Perfil

class UsuariosForm(UserCreationForm):
    empresa = forms.CharField(max_length=75)
    ubicacion = forms.CharField(max_length=150)
    mercado = forms.CharField(max_length=50)
    telefono = forms.CharField(max_length=12)

    def save(self, commit=True):
        instance = super().save(commit=commit)
        Perfil.objects.create(usuario=instance, empresa=self.cleaned_data["empresa"], ubicacion=self.cleaned_data["ubicacion"], mercado=self.cleaned_data["mercado"], telefono=self.cleaned_data["telefono"])
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

        widgets = {
            'email': EEmailInput(),
            'password': PasswordInput(),
            'telefono': NumberInput(
                attrs={
                    'maxlength':'4',
                },
            ),
        }
