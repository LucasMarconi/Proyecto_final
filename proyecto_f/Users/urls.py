from django.urls import path
from Users import views
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', views.login_request, name="Login"),
    path('register/', views.register, name="Register"),
    path('logout/', LogoutView.as_view(template_name='App1/base.html'), name="Logout"),
    #path('edit/', views.edit, name="Edit")
]