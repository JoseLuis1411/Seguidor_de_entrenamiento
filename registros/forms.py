from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *

class crearUsuario(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = (
            'username', 
            'first_name', 
            'last_name', 
            'email',
            'edad',
            'sexo',
            'altura',
            'telefono', 
            'password1', 
            'password2'
            )

    def save(self, commit=True):
        user = super().save(commit=False)

        if commit:
            user.save()
        return user
    
class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Nombre de usuario')
    password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')