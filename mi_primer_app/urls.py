from django.urls import path
from . import views

urlpatterns = [
    path('', views.pagina_inicio, name='inicio'),
    path('camisetas/', views.pagina_camisetas, name='camisetas'),
    path('login/', views.pagina_login, name='login'),
    path('logout/', views.pagina_logout, name='logout'),
    path('registro/', views.pagina_registro, name='registro'),
    path('mis-compras/', views.pagina_mis_compras, name='mis-compras'),
    path('buscar-camisetas/', views.pagina_buscar_camisetas, name='buscar-camisetas'),
    # Rutas originales para funcionalidad completa
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar-cliente'),
    path('comprar-camiseta/<int:camiseta_id>/', views.comprar_camiseta, name='comprar-camiseta'),
]



