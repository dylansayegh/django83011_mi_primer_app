from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),
    path('crear-familiar/', views.crear_familiar, name='crear-familiar'),
    path('crear-familiar/<str:nombre>/', views.crear_familiar, name='crear-familiar-param'),
    path('listar-familiares/', views.listar_familiares, name="listar-familiares"),
    path('agregar-cliente/', views.agregar_cliente, name='agregar-cliente'),
    path('camisetas/', views.listar_camisetas, name='listar-camisetas'),
    path('registro/', views.registro_usuario, name='registro'),
    path('buscar-camisetas/', views.buscar_camisetas, name='buscar-camisetas'),
    path('login/', auth_views.LoginView.as_view(template_name='mi_primer_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
    path('comprar-camiseta/<int:camiseta_id>/', views.comprar_camiseta, name='comprar-camiseta'),
    path('mis-compras/', views.mis_compras, name='mis-compras'),
]



