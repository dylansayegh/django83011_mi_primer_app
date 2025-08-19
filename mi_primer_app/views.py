# --- IMPORTS ---
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Sum
from .models import Camiseta, Cliente, Compra, Carrito, ItemCarrito, Orden, ItemOrden
import json
import uuid

# --- VISTAS PRINCIPALES ---
def pagina_inicio(request):
    """Vista de la página de inicio - con camisetas destacadas"""
    # Camisetas destacadas para mostrar en la página principal
    camisetas_destacadas = [
        {
            'id': 1,
            'equipo': 'Selección Argentina',
            'temporada': '1986 World Cup',
            'precio': 89.99,
            'precio_oferta': 79.99,
            'imagen': 'images/camisetas/argentina_1986.jpg',
            'descripcion': 'Camiseta icónica usada por Maradona en el Mundial de México 1986',
            'jugador': 'MARADONA #10',
            'marca': 'Le Coq Sportif',
            'disponible': True
        },
        {
            'id': 2,
            'equipo': 'Real Madrid CF',
            'temporada': '1998-2000',
            'precio': 94.99,
            'precio_oferta': 84.99,
            'imagen': 'images/camisetas/real_madrid_1998.jpg',
            'descripcion': 'Camiseta clásica del Real Madrid era pre-galácticos',
            'jugador': 'RAÚL #7',
            'marca': 'Adidas',
            'disponible': True
        },
        {
            'id': 3,
            'equipo': 'FC Barcelona',
            'temporada': '1992-1995',
            'precio': 99.99,
            'precio_oferta': 89.99,
            'imagen': 'images/camisetas/barcelona_1992.jpg',
            'descripcion': 'Camiseta histórica del Dream Team de Johan Cruyff',
            'jugador': 'ROMÁRIO #11',
            'marca': 'Kappa',
            'disponible': True
        }
    ]
    
    context = {
        'camisetas_destacadas': camisetas_destacadas,
        'titulo': 'Camisetas Retro DS - Lo Mejor del Fútbol Clásico'
    }
    
    return render(request, 'mi_primer_app/inicio.html', context)

def pagina_camisetas(request):
    """Vista del catálogo de camisetas - con imágenes reales"""
    # Catálogo completo de camisetas retro
    camisetas_catalogo = [
        {
            'id': 1,
            'equipo': 'Selección Argentina',
            'temporada': '1986 World Cup',
            'tipo': 'Local',
            'precio': 89.99,
            'precio_oferta': 79.99,
            'imagen': 'images/camisetas/argentina_1986.jpg',
            'descripcion': 'Camiseta icónica usada por Maradona en el Mundial de México 1986. La Mano de Dios y el Gol del Siglo.',
            'jugador': 'MARADONA #10',
            'marca': 'Le Coq Sportif',
            'año': 1986,
            'tallas': ['S', 'M', 'L', 'XL'],
            'stock': 15,
            'destacada': True,
            'colores': 'Celeste y Azul',
            'caracteristicas': [
                'Rayas verticales icónicas',
                'Cuello en V característico',
                'Material 100% poliéster',
                'Réplica oficial'
            ]
        },
        {
            'id': 2,
            'equipo': 'Real Madrid CF',
            'temporada': '1998-2000',
            'tipo': 'Local',
            'precio': 94.99,
            'precio_oferta': 84.99,
            'imagen': 'images/camisetas/real_madrid_1998.jpg',
            'descripcion': 'Camiseta clásica del Real Madrid de la era pre-galácticos con el patrocinio histórico de Teka.',
            'jugador': 'RAÚL #7',
            'marca': 'Adidas',
            'año': 1998,
            'tallas': ['S', 'M', 'L', 'XL'],
            'stock': 12,
            'destacada': True,
            'colores': 'Blanco',
            'caracteristicas': [
                'Diseño clásico madridista',
                'Patrocinio Teka histórico',
                'Tres rayas Adidas',
                'Era Raúl y Roberto Carlos'
            ]
        },
        {
            'id': 3,
            'equipo': 'FC Barcelona',
            'temporada': '1992-1995',
            'tipo': 'Local',
            'precio': 99.99,
            'precio_oferta': 89.99,
            'imagen': 'images/camisetas/barcelona_1992.jpg',
            'descripcion': 'Camiseta histórica del legendario Dream Team de Johan Cruyff que revolucionó el fútbol mundial.',
            'jugador': 'ROMÁRIO #11',
            'marca': 'Kappa',
            'año': 1992,
            'tallas': ['S', 'M', 'L', 'XL'],
            'stock': 8,
            'destacada': True,
            'colores': 'Azul y Rojo (Blaugrana)',
            'caracteristicas': [
                'Rayas blaugrana clásicas',
                'Era del Dream Team',
                'Marca Kappa vintage',
                'Romário, Stoichkov, Guardiola'
            ]
        }
    ]
    
    # Filtros disponibles
    equipos = list(set([c['equipo'] for c in camisetas_catalogo]))
    marcas = list(set([c['marca'] for c in camisetas_catalogo]))
    años = list(set([c['año'] for c in camisetas_catalogo]))
    
    context = {
        'camisetas': camisetas_catalogo,
        'equipos': equipos,
        'marcas': marcas,
        'años': sorted(años),
        'total_camisetas': len(camisetas_catalogo),
        'titulo': 'Catálogo de Camisetas Retro'
    }
    
    return render(request, 'mi_primer_app/camisetas_basico.html', context)

def detalle_camiseta(request, camiseta_id):
    """Vista de detalle de una camiseta específica"""
    camiseta = get_object_or_404(Camiseta, id=camiseta_id, activa=True)
    return render(request, 'mi_primer_app/detalle_camiseta.html', {'camiseta': camiseta})

@login_required
def mis_compras(request):
    """Vista de historial de compras del usuario - versión básica"""
    
    # Calcular total de camisetas compradas por el usuario
    try:
        total_camisetas = Compra.objects.filter(usuario=request.user).aggregate(
            total=Sum('cantidad')
        )['total'] or 0
    except:
        total_camisetas = 0
    
    context = {
        'total_camisetas': total_camisetas
    }
    
    return render(request, 'mi_primer_app/mis_compras.html', context)

# --- UTILIDAD PARA CARRITO ---
def obtener_o_crear_carrito(usuario):
    """Obtiene o crea un carrito para el usuario"""
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    return carrito

# --- VISTA DE COMPRA DE CAMISETAS ---
@login_required
def comprar_camiseta(request, camiseta_id):
    camiseta = Camiseta.objects.get(id=camiseta_id)
    mensaje = ""
    if request.method == "POST":
        cantidad = int(request.POST.get("cantidad", 1))
        Compra.procesar_compra(usuario=request.user, camiseta=camiseta, cantidad=cantidad)
        mensaje = f"¡Compra realizada! Has comprado {cantidad} x {camiseta.equipo} {camiseta.temporada}."
    return render(request, 'mi_primer_app/compra-exitosa.html', {"camiseta": camiseta, "mensaje": mensaje})

# --- VISTAS DE AUTENTICACIÓN Y USUARIO ---
def registro_usuario(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = UserCreationForm()
    return render(request, 'mi_primer_app/registro.html', {'form': form})

# --- VISTAS DE TIENDA ---
def listar_camisetas(request):
    camisetas = Camiseta.objects.all()
    return render(request, 'mi_primer_app/listar-camisetas.html', {'camisetas': camisetas})


# --- VISTAS DE CLIENTES Y FAMILIARES ---
def agregar_cliente(request):
    mensaje = ""
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        if nombre and apellido and email:
            Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            mensaje = f"Cliente {nombre} {apellido} agregado con éxito."
        else:
            mensaje = "Por favor complete todos los campos requeridos."
    return render(request, 'mi_primer_app/agregar-cliente.html', {"mensaje": mensaje})


# --- OTRAS VISTAS ---
def home(request):
    """Vista alternativa para la página de inicio"""
    return render(request, 'mi_primer_app/inicio.html')

def hola_mundo(request):
    print("¡Hola, mundo!")
    return HttpResponse("¡Hola, mundo!")

# --- VISTAS DEL CARRITO DE COMPRAS ---
def obtener_o_crear_carrito(usuario):
    """Función auxiliar para obtener o crear carrito del usuario"""
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    return carrito

def ver_carrito(request):
    """Vista para mostrar el contenido del carrito - versión básica"""
    # Template básico sin usar la base de datos por ahora
    return render(request, 'mi_primer_app/carrito_simple.html')

@login_required
@require_POST
def agregar_al_carrito(request, camiseta_id):
    """Vista para agregar camiseta al carrito"""
    camiseta = get_object_or_404(Camiseta, id=camiseta_id, activa=True)
    carrito = obtener_o_crear_carrito(request.user)
    cantidad = int(request.POST.get('cantidad', 1))
    
    if cantidad > camiseta.stock:
        messages.error(request, f'No hay suficiente stock. Stock disponible: {camiseta.stock}')
        return redirect('mi_primer_app:detalle_camiseta', camiseta_id=camiseta_id)
    
    item, created = ItemCarrito.objects.get_or_create(
        carrito=carrito,
        camiseta=camiseta,
        defaults={'cantidad': cantidad}
    )
    
    if not created:
        nueva_cantidad = item.cantidad + cantidad
        if nueva_cantidad > camiseta.stock:
            messages.error(request, f'No hay suficiente stock. Stock disponible: {camiseta.stock}')
            return redirect('mi_primer_app:detalle_camiseta', camiseta_id=camiseta_id)
        item.cantidad = nueva_cantidad
        item.save()
        messages.success(request, f'Cantidad actualizada en el carrito: {item.cantidad} x {camiseta.equipo}')
    else:
        messages.success(request, f'Camiseta agregada al carrito: {cantidad} x {camiseta.equipo}')
    
    return redirect('mi_primer_app:ver_carrito')

@login_required
@require_POST
def actualizar_carrito(request, item_id):
    """Vista para actualizar cantidad de item en carrito"""
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    
    if nueva_cantidad <= 0:
        item.delete()
        messages.success(request, 'Producto eliminado del carrito')
    elif nueva_cantidad > item.camiseta.stock:
        messages.error(request, f'No hay suficiente stock. Stock disponible: {item.camiseta.stock}')
    else:
        item.cantidad = nueva_cantidad
        item.save()
        messages.success(request, 'Carrito actualizado')
    
    return redirect('mi_primer_app:ver_carrito')

@login_required
@require_POST
def eliminar_del_carrito(request, item_id):
    """Vista para eliminar item del carrito"""
    item = get_object_or_404(ItemCarrito, id=item_id, carrito__usuario=request.user)
    item.delete()
    messages.success(request, 'Producto eliminado del carrito')
    return redirect('mi_primer_app:ver_carrito')

@login_required
def checkout(request):
    """Vista para procesar la orden de compra"""
    carrito = obtener_o_crear_carrito(request.user)
    
    if not carrito.items.exists():
        messages.error(request, 'Tu carrito está vacío')
        return redirect('mi_primer_app:ver_carrito')
    
    if request.method == 'POST':
        # Crear orden
        orden = Orden.objects.create(
            usuario=request.user,
            total=carrito.total_precio,
            direccion_envio=request.POST.get('direccion'),
            ciudad=request.POST.get('ciudad'),
            codigo_postal=request.POST.get('codigo_postal'),
            telefono=request.POST.get('telefono'),
        )
        
        # Crear items de la orden
        for item in carrito.items.all():
            ItemOrden.objects.create(
                orden=orden,
                camiseta_info={
                    'equipo': item.camiseta.equipo,
                    'temporada': item.camiseta.temporada,
                    'tipo': item.camiseta.tipo,
                    'talla': item.camiseta.talla,
                },
                cantidad=item.cantidad,
                precio_unitario=item.camiseta.precio_final,
                subtotal=item.subtotal
            )
            
            # Reducir stock
            item.camiseta.stock -= item.cantidad
            item.camiseta.save()
        
        # Limpiar carrito
        carrito.limpiar()
        
        messages.success(request, f'¡Orden creada exitosamente! Número de orden: {orden.numero_orden}')
        return redirect('mi_primer_app:orden_confirmacion', orden_id=orden.id)
    
    context = {
        'carrito': carrito,
        'items': carrito.items.all(),
        'total_precio': carrito.total_precio,
    }
    return render(request, 'mi_primer_app/checkout.html', context)

@login_required
def orden_confirmacion(request, orden_id):
    """Vista para mostrar confirmación de orden"""
    orden = get_object_or_404(Orden, id=orden_id, usuario=request.user)
    context = {'orden': orden}
    return render(request, 'mi_primer_app/orden_confirmacion.html', context)

def detalle_camiseta(request, camiseta_id):
    """Vista para mostrar detalle de una camiseta"""
    camiseta = get_object_or_404(Camiseta, id=camiseta_id, activa=True)
    context = {'camiseta': camiseta}
    return render(request, 'mi_primer_app/detalle_camiseta.html', context)

# AJAX views para carrito
@login_required
def carrito_cantidad(request):
    """Vista AJAX para obtener cantidad de items en carrito"""
    carrito = obtener_o_crear_carrito(request.user)
    return JsonResponse({'cantidad': carrito.total_items})

# Vistas legacy y de compatibilidad
def buscar_camisetas(request):
    """Vista de búsqueda de camisetas"""
    resultados = []
    query = ""
    if request.method == "GET" and "equipo" in request.GET:
        query = request.GET.get("equipo", "")
        resultados = Camiseta.objects.filter(equipo__icontains=query, activa=True)
    return render(request, 'mi_primer_app/buscar-camisetas.html', {"resultados": resultados, "query": query})

def agregar_cliente(request):
    """Vista para agregar cliente"""
    mensaje = ""
    if request.method == "POST":
        nombre = request.POST.get("nombre")
        apellido = request.POST.get("apellido")
        email = request.POST.get("email", "")
        telefono = request.POST.get("telefono", "")
        if nombre and apellido and email:
            Cliente.objects.create(nombre=nombre, apellido=apellido, email=email, telefono=telefono)
            mensaje = f"Cliente {nombre} {apellido} agregado con éxito."
        else:
            mensaje = "Por favor complete todos los campos requeridos."
    return render(request, 'mi_primer_app/agregar-cliente.html', {"mensaje": mensaje})

def hola_mundo(request):
    """Vista simple de prueba"""
    return HttpResponse("¡Hola Mundo desde Django!")
