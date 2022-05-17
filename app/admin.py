from django.contrib import admin
from .models import *


# Register your models here.

class ProductosAdmin(admin.ModelAdmin):
    list_display = ['codigo','nombre','marca','precio','stock','tipo','imagen']



class UsuariosAdmin(admin.ModelAdmin):
    list_display = ['nombre','apellido','rut','direccion','correo','contrasenia']

admin.site.register(TipoProducto)
admin.site.register(Producto,ProductosAdmin)
admin.site.register(Usuarios,UsuariosAdmin)
admin.site.register(Items_Carrito)