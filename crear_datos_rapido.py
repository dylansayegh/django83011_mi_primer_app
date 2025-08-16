# Script rápido para crear camisetas
from mi_primer_app.models import Camiseta

# Limpiar datos existentes
Camiseta.objects.all().delete()

# Crear camisetas
camisetas = [
    {'equipo': 'Barcelona', 'temporada': '1992-95', 'tipo': 'local', 'talla': 'M', 'precio': 89.99, 'precio_oferta': 69.99, 'stock': 15, 'imagen': 'https://via.placeholder.com/300x400/004B87/FFD700?text=FCB+92-95', 'descripcion': 'Camiseta retro del FC Barcelona'},
    {'equipo': 'Real Madrid', 'temporada': '1998-00', 'tipo': 'local', 'talla': 'L', 'precio': 79.99, 'stock': 12, 'imagen': 'https://via.placeholder.com/300x400/FFFFFF/000000?text=REAL+98-00', 'descripcion': 'Camiseta del Real Madrid'},
    {'equipo': 'Argentina', 'temporada': '1986', 'tipo': 'local', 'talla': 'M', 'precio': 129.99, 'precio_oferta': 99.99, 'stock': 8, 'imagen': 'https://via.placeholder.com/300x400/75AADB/FFFFFF?text=ARG+86', 'descripcion': 'Camiseta de Argentina Mundial 1986'},
    {'equipo': 'Brasil', 'temporada': '1970', 'tipo': 'local', 'talla': 'L', 'precio': 119.99, 'stock': 10, 'imagen': 'https://via.placeholder.com/300x400/FFFF00/0000FF?text=BRA+70', 'descripcion': 'Camiseta de Brasil Mundial 1970'},
    {'equipo': 'Milan', 'temporada': '1989-90', 'tipo': 'local', 'talla': 'XL', 'precio': 94.99, 'precio_oferta': 74.99, 'stock': 6, 'imagen': 'https://via.placeholder.com/300x400/FF0000/000000?text=ACM+89-90', 'descripcion': 'AC Milan retro'},
    {'equipo': 'Liverpool', 'temporada': '1984', 'tipo': 'local', 'talla': 'S', 'precio': 84.99, 'stock': 20, 'imagen': 'https://via.placeholder.com/300x400/C8102E/FFFFFF?text=LFC+84', 'descripcion': 'Liverpool retro años 80'}
]

for data in camisetas:
    Camiseta.objects.create(**data)

print(f"¡{len(camisetas)} camisetas creadas!")
print("Total en BD:", Camiseta.objects.count())

exit()
