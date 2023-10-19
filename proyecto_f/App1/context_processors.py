from django.contrib.auth.context_processors import auth
from Users.models import Imagen

def custom_user(request):
    context = auth(request)
    user = context['user']

    if user.is_authenticated:
        imagen = Imagen.objects.filter(user=request.user.id)
        cant = len(imagen)
        if cant > 0:
            context['avatar'] = imagen[cant-1]
        else:
            context['avatar'] = ""

    return context