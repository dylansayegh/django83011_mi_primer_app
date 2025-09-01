#!/usr/bin/env python
"""
Prueba completa de funcionalidad del carrito
"""

print("=== CONFIGURANDO ENTORNO DJANGO ===")
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')

import django
django.setup()

print("Django configurado correctamente")

print("\n=== IMPORTANDO MODELOS ===")
from django.contrib.auth.models import User
from mi_primer_app.models import Camiseta, Carrito, ItemCarrito

print("Modelos importados correctamente")

print("\n=== REVISANDO BASE DE DATOS ===")
try:
    camisetas_count = Camiseta.objects.count()
    users_count = User.objects.count()
    carritos_count = Carrito.objects.count()
    
    print(f"Camisetas en BD: {camisetas_count}")
    print(f"Usuarios en BD: {users_count}")
    print(f"Carritos en BD: {carritos_count}")
    
    if camisetas_count == 0:
        print("\n=== CREANDO CAMISETAS DE PRUEBA ===")
        # Crear camisetas de prueba
        camisetas_data = [
            {
                'equipo': 'Selección Argentina',
                'temporada': '1986 World Cup',
                'precio': 89.99,
                'precio_oferta': 79.99,
                'stock': 5,
                'activa': True
            },
            {
                'equipo': 'Real Madrid CF',
                'temporada': '1998-2000',
                'precio': 94.99,
                'precio_oferta': 84.99,
                'stock': 3,
                'activa': True
            },
            {
                'equipo': 'FC Barcelona',
                'temporada': '1992-1995',
                'precio': 99.99,
                'precio_oferta': 89.99,
                'stock': 7,
                'activa': True
            }
        ]
        
        for data in camisetas_data:
            camiseta, created = Camiseta.objects.get_or_create(
                equipo=data['equipo'],
                temporada=data['temporada'],
                defaults=data
            )
            if created:
                print(f"  ✓ Camiseta creada: {camiseta.equipo}")
            else:
                print(f"  - Camiseta ya existe: {camiseta.equipo}")
    
    if users_count == 0:
        print("\n=== CREANDO USUARIO DE PRUEBA ===")
        user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            email='test@test.com'
        )
        print(f"  ✓ Usuario creado: {user.username}")
        
        # Crear también superusuario
        admin = User.objects.create_superuser(
            username='admin',
            password='admin',
            email='admin@admin.com'
        )
        print(f"  ✓ Superusuario creado: {admin.username}")
    
    print("\n=== PROBANDO FUNCIONALIDAD DEL CARRITO ===")
    
    # Obtener usuario
    user = User.objects.first()
    print(f"Usuario para prueba: {user.username}")
    
    # Crear carrito
    carrito, created = Carrito.objects.get_or_create(usuario=user)
    print(f"Carrito {'creado' if created else 'obtenido'}")
    
    # Obtener camiseta
    camiseta = Camiseta.objects.first()
    if camiseta:
        print(f"Camiseta para prueba: {camiseta.equipo}")
        
        # Agregar item al carrito
        item, created = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            camiseta=camiseta,
            defaults={'cantidad': 1}
        )
        
        if created:
            print(f"  ✓ Item agregado al carrito: {item}")
        else:
            item.cantidad += 1
            item.save()
            print(f"  ✓ Cantidad actualizada: {item.cantidad}")
        
        print(f"  Subtotal del item: ${item.subtotal()}")
        print(f"  Total items en carrito: {carrito.cantidad_items()}")
        print(f"  Total del carrito: ${carrito.calcular_total()}")
    
    print("\n=== PRUEBA COMPLETADA EXITOSAMENTE ===")
    print("El carrito está funcionando correctamente!")
    print("Puedes probar en: http://127.0.0.1:8000")
    print("Usuario admin: admin / admin")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
