import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from mi_primer_app.models import Camiseta

# Crear camisetas básicas
camisetas = [
    {'equipo': 'Barcelona', 'temporada': '1992-95', 'tipo': 'local', 'talla': 'M', 'precio': 89.99, 'precio_oferta': 69.99, 'stock': 15},
    {'equipo': 'Real Madrid', 'temporada': '1998-00', 'tipo': 'local', 'talla': 'L', 'precio': 79.99, 'stock': 12},
    {'equipo': 'Argentina', 'temporada': '1986', 'tipo': 'local', 'talla': 'M', 'precio': 129.99, 'precio_oferta': 99.99, 'stock': 8},
    {'equipo': 'Brasil', 'temporada': '1970', 'tipo': 'local', 'talla': 'L', 'precio': 119.99, 'stock': 10},
    {'equipo': 'Milan', 'temporada': '1989-90', 'tipo': 'local', 'talla': 'XL', 'precio': 94.99, 'stock': 6},
    {'equipo': 'Liverpool', 'temporada': '1984', 'tipo': 'local', 'talla': 'S', 'precio': 84.99, 'stock': 20}
]

for data in camisetas:
    Camiseta.objects.create(**data)

print(f"¡{len(camisetas)} camisetas creadas!")
