from django.urls import path, include
from . import views
from .setup_view import setup_datos
from .debug_view import debug_carrito

app_name = 'mi_primer_app'

urlpatterns = [
    path('', views.pagina_inicio, name='home'),
    path('tienda/', views.tienda, name='tienda'),
    path('camisetas/', views.pagina_camisetas, name='camisetas'),
    path('camiseta/<int:camiseta_id>/', views.detalle_camiseta, name='detalle_camiseta'),
    
    # Vista especial para configurar datos
    path('setup-datos/', setup_datos, name='setup_datos'),
    
    # Vista de debugging
    path('debug-carrito/', debug_carrito, name='debug_carrito'),
    
    # Historial de compras
    path('mis-compras/', views.mis_compras, name='mis_compras'),
    
    # Carrito de compras
    path('carrito/', views.ver_carrito, name='ver_carrito'),
    path('carrito/agregar/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('carrito/actualizar/<int:item_id>/', views.actualizar_carrito, name='actualizar_carrito'),
    path('carrito/eliminar/<int:item_id>/', views.eliminar_del_carrito, name='eliminar_del_carrito'),
    path('carrito/cantidad/', views.obtener_cantidad_carrito, name='carrito_cantidad'),
    
    # Checkout y órdenes
    path('checkout/', views.checkout, name='checkout'),
    path('orden/<int:orden_id>/confirmacion/', views.orden_confirmacion, name='orden_confirmacion'),
    
    # Rutas legacy mantenidas para compatibilidad
    path('mis-compras/', views.mis_compras, name='mis-compras'),
    path('buscar-camisetas/', views.buscar_camisetas, name='buscar-camisetas'),
    path('hola-mundo/', views.hola_mundo, name='hola-mundo'),
    path('agregar-cliente/', views.agregar_cliente, name='agregar-cliente'),
    path('comprar-camiseta/<int:camiseta_id>/', views.comprar_camiseta, name='comprar-camiseta'),
]



