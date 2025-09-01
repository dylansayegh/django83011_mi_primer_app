from django.contrib.auth.models import User

# Crear superusuario si no existe
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
    print("Superusuario 'admin' creado")
else:
    print("Superusuario 'admin' ya existe")

# Mostrar información de la base de datos
from mi_primer_app.models import Camiseta, Carrito
print(f"Camisetas en BD: {Camiseta.objects.count()}")
print(f"Carritos en BD: {Carrito.objects.count()}")
