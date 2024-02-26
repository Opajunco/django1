from django import forms
from django.core import validators

from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegisterForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','first_name','last_name','password1','password2']
        
        
# ejemplo AJAX https://programadorwebvalencia.com/django-crear-formulario-de-contacto/

# class ContactForm(forms.Form):
#     name = forms.CharField(
#         max_length=200,
#         initial="",
#         required=True,
#     )
#     email = forms.EmailField(
#         max_length=200,
#         initial="",
#         required=True,
#     )
#     message = forms.CharField(
#         max_length=200,
#         initial="",
#         required=True,
#     )
#     files = forms.FileField(
#         widget=forms.ClearableFileInput(attrs={"multiple": True}), required=False
#     )
