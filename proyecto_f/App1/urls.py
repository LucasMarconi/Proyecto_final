from django.urls import path
from App1 import views


urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('aboutme/', views.aboutme, name="Aboutme"),
]

#Vistas de clientes
urlpatterns += [
    path('listascli/', views.ClienteListView.as_view(), name='ListCli'),
    path('nuevocli/', views.ClienteCreateView.as_view(), name='NewCli'),
    path('editarcli/<int:pk>/', views.ClienteUpdateView.as_view(), name='EditCli'),
]

#Vistas de productos
urlpatterns += [
    path('listasprod/', views.ProdListView.as_view(), name='ListProd'),
    path('nuevoprod/', views.ProdCreateView.as_view(), name='NewProd'),
    path('eliminarprod/<int:pk>/', views.ProductoDeleteView.as_view(), name='BorrarProd'),
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