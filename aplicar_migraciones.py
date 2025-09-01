#!/usr/bin/env python
"""
Aplicar migraciones manualmente
"""
import os
import sys
import django

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.core.management import execute_from_command_line
from django.core.management.commands.migrate import Command
from django.db import connection

def aplicar_migraciones():
    print("=== APLICANDO MIGRACIONES MANUALMENTE ===")
    
    try:
        # Ejecutar migrate usando Django internamente
        from django.core.management import call_command
        
        print("Aplicando migraciones...")
        call_command('migrate', verbosity=2)
        print("✓ Migraciones aplicadas")
        
        # Verificar estado
        call_command('showmigrations', 'mi_primer_app')
        
    except Exception as e:
        print(f"Error: {e}")
        
        # Si falla, intentar aplicar manualmente la migración específica
        try:
            print("Intentando aplicar migración específica...")
            call_command('migrate', 'mi_primer_app', '0003')
            print("✓ Migración específica aplicada")
        except Exception as e2:
            print(f"Error en migración específica: {e2}")

if __name__ == '__main__':
    aplicar_migraciones()
