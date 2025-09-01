
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# Modelo para camisetas de fútbol retro
class Camiseta(models.Model):
    TALLAS = [
        ('XS', 'Extra Small'),
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
        ('XXL', 'Double Extra Large'),
    ]
    
    TIPOS = [
        ('local', 'Local'),
        ('visitante', 'Visitante'),
        ('alternativa', 'Alternativa'),
        ('arquero', 'Arquero'),
    ]
    
    equipo = models.CharField(max_length=100)
    temporada = models.CharField(max_length=50)
    tipo = models.CharField(max_length=20, choices=TIPOS, default='local')
    talla = models.CharField(max_length=10, choices=TALLAS)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    precio_oferta = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    stock = models.PositiveIntegerField(default=0)
    imagen = models.URLField(blank=True)
    descripcion = models.TextField(blank=True)
    activa = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.equipo} {self.temporada} {self.tipo} ({self.talla})"
    
    @property
    def precio_final(self):
        return self.precio_oferta if self.precio_oferta else self.precio
    
    @property
    def tiene_oferta(self):
        return self.precio_oferta is not None
    
    @property
    def descuento_porcentaje(self):
        if self.tiene_oferta:
            return int(((self.precio - self.precio_oferta) / self.precio) * 100)
        return 0

# Modelo para órdenes de compra
class Orden(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('pagada', 'Pagada'),
        ('enviada', 'Enviada'),
        ('entregada', 'Entregada'),
        ('cancelada', 'Cancelada'),
    ]
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    numero_orden = models.CharField(max_length=20, unique=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    # Información de envío
    direccion_envio = models.TextField()
    ciudad = models.CharField(max_length=100)
    codigo_postal = models.CharField(max_length=10)
    telefono = models.CharField(max_length=15)

    def __str__(self):
        return f"Orden {self.numero_orden} - {self.usuario.username}"
    
    def save(self, *args, **kwargs):
        if not self.numero_orden:
            import uuid
            self.numero_orden = f"ORD-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)

# Modelo para items de la orden
class ItemOrden(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    camiseta_info = models.JSONField()  # Guardar info de la camiseta por si cambia
    cantidad = models.PositiveIntegerField()
    precio_unitario = models.DecimalField(max_digits=8, decimal_places=2)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.cantidad} x {self.camiseta_info['equipo']} en orden {self.orden.numero_orden}"

# Modelo para registrar compras (legacy - mantenido para compatibilidad)
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    camiseta = models.ForeignKey(Camiseta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} compró {self.cantidad} x {self.camiseta} el {self.fecha.strftime('%Y-%m-%d')}"

    @classmethod
    def procesar_compra(cls, usuario, camiseta, cantidad=1):
        compra = cls.objects.create(usuario=usuario, camiseta=camiseta, cantidad=cantidad)
        return compra

# Modelo para clientes
class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# Modelo para carrito de compras
class Carrito(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE, related_name='carrito')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_actualizacion = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Carrito de {self.usuario.username}"
    
    def calcular_total(self):
        return sum(item.subtotal() for item in self.items.all())
    
    def cantidad_items(self):
        return sum(item.cantidad for item in self.items.all())
    
    def esta_vacio(self):
        return self.items.count() == 0
    
    def limpiar(self):
        """Elimina todos los items del carrito"""
        self.items.all().delete()

# Modelo para items del carrito
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE, related_name='items')
    camiseta = models.ForeignKey(Camiseta, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    fecha_agregado = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.cantidad} x {self.camiseta.equipo} en carrito de {self.carrito.usuario.username}"
    
    def subtotal(self):
        return self.cantidad * self.camiseta.precio_final
    
    class Meta:
        unique_together = ('carrito', 'camiseta')
  