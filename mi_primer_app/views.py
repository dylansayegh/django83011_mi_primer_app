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
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from .models import Camiseta, Cliente, Compra

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
