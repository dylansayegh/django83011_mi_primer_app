#!/usr/bin/env python
"""
Crear superusuario y datos de prueba
"""
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')

import django
django.setup()

from django.contrib.auth.models import User

# Crear superusuario
try:
    if not User.objects.filter(username='admin').exists():
        admin_user = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        print("Superusuario 'admin' creado")
        print("Usuario: admin")
        print("Contraseña: admin")
    else:
        print("Superusuario 'admin' ya existe")
        
    print(f"Total usuarios: {User.objects.count()}")
    for user in User.objects.all():
        print(f"- {user.username} ({'superuser' if user.is_superuser else 'user'})")
        
except Exception as e:
    print(f"Error: {e}")
