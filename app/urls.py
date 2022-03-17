from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.conf import settings
from django.conf.urls.static import static 
from. import views

urlpatterns = [
    path('', views.app, name='app'),
    path('userNew/', views.usuario_new, name='newUser'),
    #path('login/', LoginView.as_view(template_name='app/login.html'), name='login'),
    path('login/', views.Login.as_view(), name='login'),
	path('logout/', LogoutView.as_view(), name='logout'),
    path('myaccount/', views.myaccount, name='myaccount'),
    path('Edit/', views.User_edit.as_view(), name='Edit_User'),
    path('UploadImageU/', views.upload_image_User_view, name='UploadImageUser'),
    path('CreateHabili/', views.Create_habili.as_view(), name='CreateHabili'),
    path('HabilidadEdit/<int:id>/', views.Habili_edit, name='Habili_edit'),
    path('HabilidadDelete/<int:id>/', views.Habili_delete, name='Habili_delete'),
    path('Perfil/<int:id>/', views.Busquedaanuncio, name='Perfil_list'),
    path('Resultado/', views.Busqueda.as_view(), name='busqueda'),
    path('Favorito/', views.Favorito, name='Favorite'),
    path('SolicitudPedido/', views.Realizar_Pedido, name='SoliPedidos'),
    path('Pedidos/', views.Pedidos.as_view(), name='Pedidos'),
    path('Aceptar_Solicitud/', views.AceptarSolicitud, name='AceptarSolicitud'),
    path('Cancelar_Solicitud/', views.CancelarSolicitud, name='CancelarSolicitud'),
    path('DetallePedido/<int:id>/', views.Detalle_Pedido, name='Detalle_Pedido'),
    
    path('Valoracion_Solicitud/<int:id>/', views.Valorizacion_Pedido, name='Valorizacion_Pedido'),

    ] 
