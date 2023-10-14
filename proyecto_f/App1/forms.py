from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ClienteFormulario(forms.Form):
    
    nombre = forms.CharField()
    edad = forms.IntegerField()
    email = forms.EmailField()
    
class ProductoFormulario(forms.Form):
    
    nombre = forms.CharField()
    precio = forms.FloatField()

class SucursalFormulario(forms.Form):   
     
    calle = forms.CharField()
    altura = forms.IntegerField()
    
class BusquedaCliente(forms.Form):
    
    nombre = forms.CharField()
    
    
    