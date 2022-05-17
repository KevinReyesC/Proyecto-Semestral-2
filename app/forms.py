from django import forms
from django.forms import ModelForm
from .models import *

class ProductoForm(ModelForm):
    nombre = forms.CharField(min_length=10,max_length=20)
    precio = forms.IntegerField(min_value=400)


    class Meta:
        model = Producto
        fields = ['codigo','nombre','marca','precio','stock','tipo','imagen']

        widgets = {
            'fecha_ingreso' : forms.SelectDateWidget(years=range(2020,2023))
        }

class ProductoForms(ModelForm):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    rut = models.CharField(max_length=200)
    direccion = models.CharField(max_length=200)
    correo = models.CharField(max_length=200)
    contrasenia = models.CharField(max_length=200)
    class Meta:
        model = Usuarios
        fields = ['nombre','apellido','rut','direccion','correo','contrasenia']    