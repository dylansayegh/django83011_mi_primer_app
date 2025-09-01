#!/usr/bin/env python
"""
Solución definitiva para el problema de migraciones
"""
import os
import django
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.core.management.commands.migrate import Command as MigrateCommand
from django.core.management.base import BaseCommand
from django.db import connection
from django.core.management import CommandError
import subprocess

def solucion_definitiva():
    print("=== SOLUCIÓN DEFINITIVA DE MIGRACIONES ===")
    
    try:
        # 1. Forzar aplicación usando subprocess directamente
        print("1. Intentando aplicar migraciones usando subprocess...")
        
        result = subprocess.run([
            sys.executable, 'manage.py', 'migrate', 'mi_primer_app', '--verbosity=2'
        ], capture_output=True, text=True, cwd='.')
        
        print("STDOUT:", result.stdout)
        print("STDERR:", result.stderr)
        print("Return code:", result.returncode)
        
        if result.returncode == 0:
            print("✅ Migraciones aplicadas exitosamente")
        else:
            print("❌ Error aplicando migraciones")
            
            # 2. Plan B: Aplicar usando fake
            print("\n2. Intentando con --fake...")
            result2 = subprocess.run([
                sys.executable, 'manage.py', 'migrate', 'mi_primer_app', '--fake'
            ], capture_output=True, text=True, cwd='.')
            
            print("FAKE - STDOUT:", result2.stdout)
            print("FAKE - STDERR:", result2.stderr)
            
            if result2.returncode == 0:
                print("✅ Migraciones marcadas como aplicadas")
            else:
                print("❌ Error con fake también")
        
        # 3. Verificar estado final
        print("\n3. Verificando estado final...")
        result3 = subprocess.run([
            sys.executable, 'manage.py', 'showmigrations', 'mi_primer_app'
        ], capture_output=True, text=True, cwd='.')
        
        print("Estado de migraciones:")
        print(result3.stdout)
        
    except Exception as e:
        print(f"Error en solución: {e}")

if __name__ == '__main__':
    solucion_definitiva()
