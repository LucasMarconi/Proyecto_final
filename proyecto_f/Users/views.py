from django.shortcuts import render

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from Users.forms import UserEditForm, UserRegisterForm
from Users.models import Imagen
from App1.views import inicio


# Create your views here.
def login_request(request):
    msg_login = ""
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return inicio(request)

        msg_login = "Usuario o contraseña incorrectos"

    form = AuthenticationForm()
    return render(request, "Users/login.html", {"form": form, "msg_login": msg_login})

# Vista de registro
def register(request):
    msg_register = ""
    if request.method == 'POST':

        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return inicio(request)
        
        msg_register = "Error en los datos ingresados"

    form = UserRegisterForm()     
    return render(request,"Users/registro.html" ,  {"form":form, "msg_register": msg_register})
