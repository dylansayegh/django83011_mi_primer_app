
from django.db import models
from django.contrib.auth.models import User

# Modelo para registrar compras de camisetas
class Compra(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    camiseta = models.ForeignKey('Camiseta', on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.usuario.username} compró {self.cantidad} x {self.camiseta} el {self.fecha.strftime('%Y-%m-%d')}"

    @classmethod
    def procesar_compra(cls, usuario, camiseta, cantidad=1):
        # Aquí puedes agregar lógica extra, como validar stock, aplicar descuentos, etc.
        compra = cls.objects.create(usuario=usuario, camiseta=camiseta, cantidad=cantidad)
        return compra

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


# Create your models here.

# es para la base de datos 
#una vez realizado el modelo, se debe ejecutar el comando: python manage.py makemigrations
# y luego python manage.py migrate para aplicar los cambios a la base de datos



# Create your models here.


class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    parentesco = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.edad} años) - {self.parentesco}"


class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion_semanas = models.IntegerField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    edad = models.IntegerField()
    fecha_inscripcion = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Auto(models.Model):
    modelo = models.CharField(max_length=20)
    marca = models.CharField(max_length=20)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.marca} {self.modelo}'
  