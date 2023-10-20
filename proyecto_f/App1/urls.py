from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('sucursales/', views.sucursalesFormulario, name="Sucursales"),
]

#Vistas de clientes
urlpatterns += [
    path('listascli/', views.ClienteListView.as_view(), name='ListCli'),
    path('nuevocli/', views.ClienteCreateView.as_view(), name='NewCli'),
    path('editarcli/<int:pk>/', views.ClienteUpdateView.as_view(), name='EditCli'),
    #path('clases/eliminarcli/<int:pk>/', views.CliDeleteView.as_view(), name='DeleteCli'),
]

#Vistas de productos
urlpatterns += [
    path('listasprod/', views.ProdListView.as_view(), name='ListProd'),
    path('nuevoprod/', views.ProdCreateView.as_view(), name='NewProd'),
    path('borrarprod/<int:prod_id>/', views.borrarproducto, name="BorrarProd"),
    path('detalle/<int:pk>/', views.ProdDetalleView.as_view(), name='DetailProd'),
    path('buscarform/', views.buscarProd, name="Buscar"),
    path('editarprod/<int:pk>/', views.ProductoUpdateView.as_view(), name='EditProd'),
]

#Vistas de sucursales
urlpatterns += [
    path('listassuc/', views.SucListView.as_view(), name='ListSuc'),
    path('nuevosuc/', views.SucCreateView.as_view(), name='NewSuc'),
    path('editarsuc/<int:pk>/', views.SucUpdateView.as_view(), name='EditSuc'),
]