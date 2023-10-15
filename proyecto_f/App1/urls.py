from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('productos/', views.productosFormulario, name="Productos"),
    path('sucursales/', views.sucursalesFormulario, name="Sucursales"),
    path('buscarform/', views.buscarCli, name="Buscar"),
]

#Vistas de clientes
urlpatterns += [
    path('clases/listascli/', views.ClienteListView.as_view(), name='ListCli'),
    path('clases/nuevocli/', views.ClienteCreateView.as_view(), name='NewCli'),
    path('clases/editarcli/<int:pk>/', views.ClienteUpdateView.as_view(), name='EditCli'),
    #path('clases/eliminarcli/<int:pk>/', views.CliDeleteView.as_view(), name='DeleteCli'),
]

#Vistas de productos
urlpatterns += [
    path('borrarprod/<int:prod_id>/', views.borrarproducto, name="BorrarProd"),
    path('clases/detalle/<int:pk>/', views.ProdDetalleView.as_view(), name='DetailProd'),
]