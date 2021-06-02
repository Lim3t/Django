from django import forms
from django.forms import ModelForm
from .models import Cliente

class ClienteForm(ModelForm):
    
     class Meta:
        model = Cliente
        #fields =['nombre','apellido','direccion','correo','comuna','edad','comentario']
        fields = '__all__'