#!/usr/bin/env python
import os
import sys

# Agregar el directorio actual al path de Python
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')

import django
django.setup()

from django.contrib.auth.models import User
from mi_primer_app.models import Camiseta

def crear_datos():
    print("=== CREANDO DATOS PARA EL CARRITO ===")
    
    # 1. Crear camisetas
    camisetas_data = [
        {
            'equipo': 'Selección Argentina',
            'temporada': '1986 World Cup',
            'tipo': 'local',
            'talla': 'M',
            'precio': 89.99,
            'precio_oferta': 79.99,
            'stock': 15,
            'activa': True,
            'imagen': 'camisetas/argentina_1986.jpg',
            'descripcion': 'Camiseta retro de Argentina Mundial 1986 - Diego Maradona'
        },
        {
            'equipo': 'Real Madrid CF',
            'temporada': '1998-2000',
            'tipo': 'local',
            'talla': 'L',
            'precio': 94.99,
            'precio_oferta': 84.99,
            'stock': 12,
            'activa': True,
            'imagen': 'camisetas/real_madrid_1998.jpg',
            'descripcion': 'Camiseta histórica Real Madrid era Galácticos'
        },
        {
            'equipo': 'FC Barcelona',
            'temporada': '1992-1995',
            'tipo': 'local',
            'talla': 'L',
            'precio': 99.99,
            'precio_oferta': 89.99,
            'stock': 8,
            'activa': True,
            'imagen': 'camisetas/barcelona_1992.jpg',
            'descripcion': 'Camiseta FC Barcelona Dream Team de Cruyff'
        }
    ]
    
    created_count = 0
    for data in camisetas_data:
        camiseta, created = Camiseta.objects.get_or_create(
            equipo=data['equipo'],
            temporada=data['temporada'],
            defaults=data
        )
        if created:
            created_count += 1
            print(f"✓ Camiseta creada: {camiseta.equipo} {camiseta.temporada} - ${camiseta.precio_final}")
    
    print(f"\n=== RESUMEN ===")
    print(f"Camisetas nuevas creadas: {created_count}")
    print(f"Total camisetas en BD: {Camiseta.objects.count()}")
    print(f"Camisetas activas: {Camiseta.objects.filter(activa=True).count()}")
    
    # 2. Mostrar info del usuario actual
    try:
        user = User.objects.get(username='dylan18')
        print(f"Usuario encontrado: {user.username}")
    except User.DoesNotExist:
        print("Usuario 'dylan18' no encontrado")
    
    print("\n¡Datos creados! Ahora prueba agregar productos al carrito.")
    return True

if __name__ == '__main__':
    try:
        crear_datos()
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
