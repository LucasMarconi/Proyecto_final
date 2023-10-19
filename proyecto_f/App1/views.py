from django.shortcuts import render
from App1.forms import *
from App1.models import Cliente, Sucursal, Producto
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from Users.models import Imagen


def inicio(request):
    suc = Sucursal.objects.all()
    
    try:
        url = Imagen.objects.filter(user=request.user.id)[0]
    except IndexError:
        url = None
    
    return render(request, "App1/base.html", {"sucursales": suc, "url": url})

@login_required
def productosFormulario(request):
    
    if request.method == 'POST':
 
            miFormulario = ProductoFormulario(request.POST )
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  prod = Producto(nombre=informacion['nombre'], precio=informacion['precio'])
                  prod.save()
                  return inicio(request)
    else:
            miFormulario = ProductoFormulario()
 
    return render(request, "App1/ProductoFormulario.html", {"miFormulario": miFormulario})

@login_required
def sucursalesFormulario(request):
    
    if request.method == 'POST':
 
            miFormulario = SucursalFormulario(request.POST ) 
 
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  suc = Sucursal(calle=informacion['calle'], altura=informacion['altura'])
                  suc.save()
                  return inicio(request)
    else:
            miFormulario = SucursalFormulario()
 
    return render(request, "App1/SucursalFormulario.html", {"miFormulario": miFormulario})

def buscarProd(request):
    
    if request.method == 'POST':
         
            miFormulario = BusquedaCliente(request.POST ) 
 
            if miFormulario.is_valid():
                informacion = miFormulario.cleaned_data
                productos = Producto.objects.filter(nombre__icontains=informacion["nombre"])
                return render(request, "App1/prodResultado.html", {"productos": productos})
    else:
        miFormulario = BusquedaCliente()
 
    return render(request, "App1/prodBuscar.html", {"miFormulario": miFormulario})

@login_required
def borrarproducto(request, prod_id):
    
    try:
        producto = Producto.objects.get(id=int(prod_id))
        
        producto.delete()
        return inicio(request)
    except:
        return inicio(request)

class ClienteListView(ListView):
    model=Cliente
    template_name= "App1/cliLista.html"
    
class  ClienteCreateView(LoginRequiredMixin, CreateView):
    model=Cliente
    template_name= "App1/clienteFormulario.html"
    success_url = reverse_lazy("ListCli")
    fields=["nombre", "email", "edad"]
    
class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model=Cliente
    template_name= "App1/clienteEdit.html"
    success_url = reverse_lazy("ListCli")
    fields = ["nombre", "email", "edad"]

class ProdListView(ListView):
    model=Producto
    template_name= "App1/prodLista.html"
    
class  ProdCreateView(LoginRequiredMixin, CreateView):
    model=Producto
    template_name= "App1/prodFormulario.html"
    success_url = reverse_lazy("ListProd")
    fields=["nombre", "precio"]

class ProdDetalleView(DetailView):
    model=Producto
    template_name= "App1/Prod_detalle.html"


