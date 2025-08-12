# --- VISTAS DE MENÚ PARA PÁGINAS CON DISEÑO ---
def pagina_inicio(request):
    return render(request, 'mi_primer_app/inicio.html')

def pagina_camisetas(request):
    camisetas = Camiseta.objects.all()
    return render(request, 'mi_primer_app/camisetas.html', {'camisetas': camisetas})

def pagina_login(request):
    return render(request, 'mi_primer_app/login.html')

def pagina_logout(request):
    return render(request, 'mi_primer_app/logout.html')

def pagina_registro(request):
    return render(request, 'mi_primer_app/registro.html')

def pagina_mis_compras(request):
    return render(request, 'mi_primer_app/mis-compras.html')

def pagina_buscar_camisetas(request):
    return render(request, 'mi_primer_app/buscar-camisetas.html')
# --- VISTA DE BÚSQUEDA DE CAMISETAS ---
def buscar_camisetas(request):
    resultados = []
    query = ""
    if request.method == "GET" and "equipo" in request.GET:
        query = request.GET.get("equipo", "")
        resultados = Camiseta.objects.filter(equipo__icontains=query)
    return render(request, 'mi_primer_app/buscar-camisetas.html', {"resultados": resultados, "query": query})

# --- IMPORTS ---
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .models import Camiseta, Cliente, Compra, Carrito, ItemCarrito, Orden, ItemOrden
import json

# --- VISTA DE HISTORIAL DE COMPRAS ---
@login_required
def mis_compras(request):
    compras = Compra.objects.filter(usuario=request.user).select_related('camiseta').order_by('-fecha')
    return render(request, 'mi_primer_app/mis-compras.html', {'compras': compras})

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
    return render(request, 'mi_primer_app/agregar-clientes.html', {"mensaje": mensaje})


# --- OTRAS VISTAS ---
def home(request):
    return render(request, 'mi_primer_app/home.html')

def hola_mundo(request):
    print("¡Hola, mundo!")
    return HttpResponse("¡Hola, mundo!")

# --- VISTAS DEL CARRITO DE COMPRAS ---
def obtener_o_crear_carrito(usuario):
    """Función auxiliar para obtener o crear carrito del usuario"""
    carrito, created = Carrito.objects.get_or_create(usuario=usuario)
    return carrito

@login_required
def ver_carrito(request):
    """Vista para mostrar el contenido del carrito"""
    carrito = obtener_o_crear_carrito(request.user)
    context = {
        'carrito': carrito,
        'items': carrito.items.all(),
        'total_items': carrito.total_items,
        'total_precio': carrito.total_precio,
    }
    return render(request, 'mi_primer_app/carrito.html', context)

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

@login_required
def mis_ordenes(request):
    """Vista para mostrar historial de órdenes del usuario"""
    ordenes = Orden.objects.filter(usuario=request.user).order_by('-fecha_creacion')
    context = {'ordenes': ordenes}
    return render(request, 'mi_primer_app/mis_ordenes.html', context)

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
