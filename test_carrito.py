#!/usr/bin/env python
"""
Script para probar la funcionalidad del carrito
"""

import os
import django
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.contrib.auth.models import User
from mi_primer_app.models import Camiseta, Carrito, ItemCarrito

def test_carrito():
    """Prueba la funcionalidad básica del carrito"""
    print("=== TEST CARRITO ===")
    
    # 1. Verificar que hay camisetas
    print("\n1. Verificando camisetas...")
    camisetas = Camiseta.objects.filter(activa=True)
    print(f"Camisetas disponibles: {camisetas.count()}")
    for c in camisetas:
        print(f"  - {c.equipo} ({c.temporada}) - Stock: {c.stock} - Precio: ${c.precio_final}")
    
    # 2. Obtener o crear usuario de prueba
    print("\n2. Obteniendo usuario de prueba...")
    user, created = User.objects.get_or_create(
        username='test_user',
        defaults={
            'email': 'test@test.com',
            'first_name': 'Test',
            'last_name': 'User'
        }
    )
    if created:
        user.set_password('testpass123')
        user.save()
        print("  Usuario de prueba creado")
    else:
        print("  Usuario de prueba ya existe")
    
    # 3. Probar creación de carrito
    print("\n3. Probando carrito...")
    carrito, created = Carrito.objects.get_or_create(usuario=user)
    if created:
        print("  Carrito creado")
    else:
        print("  Carrito ya existe")
    
    print(f"  Items en carrito: {carrito.cantidad_items()}")
    print(f"  Total carrito: ${carrito.calcular_total()}")
    
    # 4. Agregar item al carrito si hay camisetas
    if camisetas.exists():
        print("\n4. Agregando item al carrito...")
        camiseta = camisetas.first()
        
        item, created = ItemCarrito.objects.get_or_create(
            carrito=carrito,
            camiseta=camiseta,
            defaults={'cantidad': 1}
        )
        
        if created:
            print(f"  Item agregado: {item}")
        else:
            item.cantidad += 1
            item.save()
            print(f"  Cantidad actualizada: {item}")
        
        print(f"  Subtotal del item: ${item.subtotal()}")
        print(f"  Items totales en carrito: {carrito.cantidad_items()}")
        print(f"  Total carrito: ${carrito.calcular_total()}")
    
    print("\n=== TEST COMPLETADO ===")

if __name__ == '__main__':
    test_carrito()
