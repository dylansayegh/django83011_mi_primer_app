"""
Script para poblar la base de datos con camisetas de prueba
"""

import os
import django
import sys

# Configurar Django
sys.path.append('c:\\Users\\Dylan\\Downloads\\mi_primer_app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from mi_primer_app.models import Camiseta

def crear_camisetas():
    camisetas_data = [
        {
            'equipo': 'Barcelona',
            'temporada': '2008-09',
            'tipo': 'local',
            'talla': 'M',
            'precio': 89.99,
            'precio_oferta': 69.99,
            'stock': 15,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta histórica del Barcelona temporada 2008-09, época dorada del club.'
        },
        {
            'equipo': 'Real Madrid',
            'temporada': '2000-01',
            'tipo': 'local',
            'talla': 'L',
            'precio': 84.99,
            'stock': 8,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta clásica blanca del Real Madrid de los Galácticos.'
        },
        {
            'equipo': 'Argentina',
            'temporada': '1986',
            'tipo': 'local',
            'talla': 'M',
            'precio': 129.99,
            'precio_oferta': 99.99,
            'stock': 5,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta histórica de Argentina del Mundial México 86, época de Maradona.'
        },
        {
            'equipo': 'Brasil',
            'temporada': '1970',
            'tipo': 'local',
            'talla': 'L',
            'precio': 119.99,
            'stock': 12,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta legendaria de Brasil del Mundial México 70, la Canarinha de Pelé.'
        },
        {
            'equipo': 'AC Milan',
            'temporada': '1989-90',
            'tipo': 'local',
            'talla': 'M',
            'precio': 94.99,
            'precio_oferta': 79.99,
            'stock': 7,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta del AC Milan de los holandeses Van Basten, Gullit y Rijkaard.'
        },
        {
            'equipo': 'Manchester United',
            'temporada': '1998-99',
            'tipo': 'local',
            'talla': 'L',
            'precio': 89.99,
            'stock': 10,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta del Manchester United del triplete histórico 1998-99.'
        },
        {
            'equipo': 'Liverpool',
            'temporada': '2004-05',
            'tipo': 'local',
            'talla': 'M',
            'precio': 79.99,
            'precio_oferta': 59.99,
            'stock': 6,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta del Liverpool de la remontada histórica en Estambul.'
        },
        {
            'equipo': 'Inter de Milán',
            'temporada': '2009-10',
            'tipo': 'local',
            'talla': 'L',
            'precio': 84.99,
            'stock': 9,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta del Inter de Milán del triplete con Mourinho.'
        },
        {
            'equipo': 'Alemania',
            'temporada': '1990',
            'tipo': 'local',
            'talla': 'M',
            'precio': 109.99,
            'precio_oferta': 89.99,
            'stock': 4,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta de Alemania campeona del Mundial Italia 90.'
        },
        {
            'equipo': 'Juventus',
            'temporada': '1995-96',
            'tipo': 'local',
            'talla': 'L',
            'precio': 79.99,
            'stock': 11,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta de la Juventus de la época de Roberto Baggio y Del Piero.'
        },
        {
            'equipo': 'Francia',
            'temporada': '1998',
            'tipo': 'local',
            'talla': 'M',
            'precio': 99.99,
            'precio_oferta': 79.99,
            'stock': 8,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta de Francia campeona del Mundial 1998 en casa.'
        },
        {
            'equipo': 'Chelsea',
            'temporada': '2004-05',
            'tipo': 'local',
            'talla': 'L',
            'precio': 74.99,
            'stock': 13,
            'imagen': 'https://images.unsplash.com/photo-1551698618-1dfe5d97d256?w=400',
            'descripcion': 'Camiseta del Chelsea de la primera Premier League con Mourinho.'
        }
    ]

    print("Creando camisetas de prueba...")
    
    for data in camisetas_data:
        camiseta, created = Camiseta.objects.get_or_create(
            equipo=data['equipo'],
            temporada=data['temporada'],
            tipo=data['tipo'],
            talla=data['talla'],
            defaults=data
        )
        if created:
            print(f"✓ Creada: {camiseta}")
        else:
            print(f"- Ya existe: {camiseta}")
    
    print(f"\nTotal de camisetas en la base de datos: {Camiseta.objects.count()}")

if __name__ == "__main__":
    crear_camisetas()
