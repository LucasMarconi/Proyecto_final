from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('clientes/', views.clienteFormulario, name="Clientes"),
    path('productos/', views.productosFormulario, name="Productos"),
    path('sucursales/', views.sucursalesFormulario, name="Sucursales"),
    path('buscarform/', views.buscarCli, name="Buscar"),
    path('borrarprod/<int:prod_id>/', views.borrarproducto, name="BorrarProd"),
]

#Vistas basadas en clases
urlpatterns += [
    path('clases/listascli/', views.ClienteListView.as_view(), name='ListCli'),
    path('clases/nuevocli/', views.ClienteCreateView.as_view(), name='NewCli'),
    path('clases/editarcli/<int:pk>/', views.ClienteUpdateView.as_view(), name='EditCli'),
    #path('clases/eliminarcli/<int:pk>/', views.CliDeleteView.as_view(), name='DeleteCli'),
    path('clases/eliminar/<int:pk>/', views.ProdDeleteView.as_view(), name='DeleteProd'),
    path('clases/detalle/<int:pk>/', views.ProdDetalleView.as_view(), name='DetailProd'),
]