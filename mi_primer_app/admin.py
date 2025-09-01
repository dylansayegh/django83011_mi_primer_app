from django.contrib import admin
from .models import Camiseta, Cliente, Compra, Carrito, ItemCarrito, Orden, ItemOrden

@admin.register(Camiseta)
class CamisetaAdmin(admin.ModelAdmin):
    list_display = ['equipo', 'temporada', 'tipo', 'talla', 'precio', 'precio_oferta', 'stock', 'activa']
    list_filter = ['activa', 'tipo', 'talla', 'temporada']
    search_fields = ['equipo', 'temporada', 'descripcion']
    list_editable = ['precio', 'precio_oferta', 'stock', 'activa']
    ordering = ['equipo', 'temporada']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'email', 'telefono']
    search_fields = ['nombre', 'apellido', 'email']
    ordering = ['apellido', 'nombre']

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'camiseta', 'cantidad', 'fecha']
    list_filter = ['fecha']
    search_fields = ['usuario__username', 'camiseta__equipo']
    ordering = ['-fecha']

class ItemCarritoInline(admin.TabularInline):
    model = ItemCarrito
    extra = 0
    readonly_fields = ['fecha_agregado']

@admin.register(Carrito)
class CarritoAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'cantidad_items', 'calcular_total', 'fecha_creacion']
    search_fields = ['usuario__username']
    readonly_fields = ['fecha_creacion', 'fecha_actualizacion']
    inlines = [ItemCarritoInline]
    ordering = ['-fecha_actualizacion']

class ItemOrdenInline(admin.TabularInline):
    model = ItemOrden
    extra = 0
    readonly_fields = ['camiseta_info', 'subtotal']

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ['numero_orden', 'usuario', 'total', 'estado', 'fecha_creacion']
    list_filter = ['estado', 'fecha_creacion']
    search_fields = ['numero_orden', 'usuario__username']
    readonly_fields = ['numero_orden', 'fecha_creacion', 'fecha_actualizacion']
    inlines = [ItemOrdenInline]
    ordering = ['-fecha_creacion']
