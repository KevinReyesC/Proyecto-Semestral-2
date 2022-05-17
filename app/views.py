from django.shortcuts import redirect, render, redirect

from .forms import *
from .models import *

# Create your views here.


def index(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    return render(request, 'app/index.html', datos)

def perrito(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }   
    return render(request, 'app/perrito.html', datos)
    

def gato(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/gato.html', datos)

def pajaros(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/pajaros.html', datos)

def suscripcion(request):
    return render(request, 'app/Suscripcion.html')

def ayuda(request):
    return render(request, 'app/paginaAyuda.html')

def todos(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }    
    return render(request, 'app/todos.html', datos)

def registro(request):
    return render(request, 'app/registro.html')
    
def conf_pago(request):
    carrito = Items_Carrito.objects.all()
    carrito.delete()
    return render(request, 'app/conf_pago.html')



def usuario_iniciado(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    
    return render(request, 'app/Usuario_Iniciado.html', datos)
    








def perrito_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/perrito_iniciado.html', datos)  

def gato_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    return render(request, 'app/gato_iniciado.html', datos)

def pajaros_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    
    return render(request, 'app/pajaros_iniciado.html', datos)






def suscripcion_ini(request):
    return render(request, 'app/Suscripcion_iniciado.html')

def ayuda_ini(request):
    return render(request, 'app/paginaAyuda_iniciado.html')   

def carrito(request):
    carrito = Items_Carrito.objects.all()
    datos = {
        'listaCarrito' : carrito 
    }
    return render(request, 'app/carrito.html',datos)   








def todo_ini(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll  }

    if request.method == 'POST' :
        carrito = Items_Carrito()
        carrito.nombre_producto = request.POST.get('nombre_producto')
        carrito.precio_producto = request.POST.get('precio_producto')
        carrito.imagen = request.POST.get('imagen_producto')
        carrito.save()
    
    return render(request, 'app/todos_iniciado.html', datos)  






    
      

def cuenta(request):
    return render(request, 'app/cuenta.html')

def historial(request):
    return render(request, 'app/historial.html')   

def pago(request):
    return render(request, 'app/pago.html')   

def seguimiento(request):
    return render(request, 'app/Seguimiento.html')    

def seguimiento2(request):
    return render(request, 'app/seguimiento2.html')

def codigo2(request):
    return render(request, 'app/codigo2.html')

def desuscripcion(request):
    return render(request, 'app/desuscripcion.html')

def agregar_p(request):
    datos = {
        'form' : ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto guardado correctamente"
    return render(request, 'app/agregar_producto.html', datos)    

def modificar_producto(request, codigo):
    producto = Producto.objects.get(codigo=codigo)
    datos = {
        'form' : ProductoForm(instance=producto)
    }
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, files=request.FILES,instance=producto)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Producto modificado correctamente"
            datos['form'] = formulario

    return render(request, 'app/modificar_producto.html', datos)    

def listar_producto(request):
    productosAll = Producto.objects.all()
    datos = {
        'listaProductos' : productosAll
    }
    return render(request, 'app/listar_producto.html', datos)  
    

def eliminar_producto(request,codigo):
    producto = Producto.objects.get(codigo=codigo)
    producto.delete()

    return redirect(to="listar_producto")



def usuarios(request):
    datos = {
        'forms' : ProductoForms()
    }
    if request.method == 'POST':
        formulario = ProductoForms(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            datos['mensajito'] = "Usuario guardado correctamente"
    return render(request, 'app/usuarios.html', datos) 

def listar_usuarios(request):
    UsuariosAll = Usuarios.objects.all()
    datos = {
        'listausuarios' : UsuariosAll
    }
    return render(request, 'app/listar_usuarios.html', datos)  

def modificar_usuarios(request, rut):
    usuarios = Usuarios.objects.get(rut=rut)
    datos = {
        'forms' : ProductoForms(instance=usuarios)
    }
    if request.method == 'POST':
        formulario = ProductoForms(request.POST, files=request.FILES,instance=usuarios)
        if formulario.is_valid():
            formulario.save()
            datos['mensaje'] = "Usuario modificado correctamente"
            datos['forms'] = formulario

    return render(request, 'app/modificar_usuarios.html', datos)    

def eliminar_usuarios(request,rut):
    usuarios = Usuarios.objects.get(rut=rut)
    usuarios.delete()

    return redirect(to="listar_producto")
    