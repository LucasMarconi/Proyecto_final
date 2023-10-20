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
    
    try:
        url = Imagen.objects.filter(user=request.user.id)[0]
    except IndexError:
        url = None
    
    return render(request, "App1/base.html", {"url": url})

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

def borrarproducto(request, prod_id):
    
    try:
        producto = Producto.objects.get(id=int(prod_id))
        
        producto.delete()
        return render(request, "ListSuc")
    except:
        return render(request, "ListSuc")


class ClienteListView(LoginRequiredMixin, ListView):
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

class ProdListView(LoginRequiredMixin, ListView):
    model=Producto
    template_name= "App1/prodLista.html"
    
class  ProdCreateView(LoginRequiredMixin, CreateView):
    model=Producto
    template_name= "App1/prodFormulario.html"
    success_url = reverse_lazy("ListProd")
    fields=["nombre", "precio"]

class ProductoDeleteView(DeleteView):
    model = Producto
    success_url = reverse_lazy("ListProd")
    template_name = 'App1/confirmardelete.html'

class ProductoUpdateView(LoginRequiredMixin, UpdateView):
    model=Producto
    template_name= "App1/prodEdit.html"
    success_url = reverse_lazy("ListProd")
    fields = ["nombre", "precio"]

class ProdDetalleView(LoginRequiredMixin, DetailView):
    
    model=Producto
    template_name= "App1/prodDetalle.html"

class SucListView(LoginRequiredMixin, ListView):
    model=Sucursal
    template_name= "App1/sucLista.html"
    
class SucCreateView(LoginRequiredMixin, CreateView):
    model=Sucursal
    template_name= "App1/sucFormulario.html"
    success_url = reverse_lazy("ListSuc")
    fields = ["calle", "altura"]
    
class SucUpdateView(LoginRequiredMixin, UpdateView):
    model=Sucursal
    template_name= "App1/sucEdit.html"
    success_url = reverse_lazy("ListSuc")
    fields = ["calle", "altura"]