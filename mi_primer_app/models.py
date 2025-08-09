
from django.db import models
from django.contrib.auth.models import User

# Modelo para camisetas de fútbol retro
class Camiseta(models.Model):
    equipo = models.CharField(max_length=100)
    temporada = models.CharField(max_length=50)
    talla = models.CharField(max_length=10)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    imagen = models.URLField(blank=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return f"{self.equipo} {self.temporada} ({self.talla})"

# Modelo para registrar compras de camisetas
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    camiseta = models.ForeignKey(Camiseta, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} compró {self.cantidad} x {self.camiseta} el {self.fecha.strftime('%Y-%m-%d')}"

    @classmethod
    def procesar_compra(cls, usuario, camiseta, cantidad=1):
        # Aquí puedes agregar lógica extra, como validar stock, aplicar descuentos, etc.
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
  