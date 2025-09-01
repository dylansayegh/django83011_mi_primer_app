#!/usr/bin/env python
"""
Marcar migración como aplicada manualmente
"""
import sqlite3
import os
from datetime import datetime

# Conectar a la base de datos
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

print("=== APLICANDO MIGRACIÓN MANUALMENTE ===")

try:
    # 1. Verificar qué migraciones están aplicadas
    cursor.execute("SELECT app, name FROM django_migrations WHERE app = 'mi_primer_app' ORDER BY id;")
    applied_migrations = cursor.fetchall()
    
    print("Migraciones aplicadas actualmente:")
    for app, name in applied_migrations:
        print(f"  - {app}.{name}")
    
    # 2. Verificar si la migración 0003 está aplicada
    cursor.execute("SELECT COUNT(*) FROM django_migrations WHERE app = 'mi_primer_app' AND name = '0003_camiseta_activa_camiseta_fecha_creacion_and_more';")
    migration_exists = cursor.fetchone()[0]
    
    if migration_exists == 0:
        print("\n⚠️ Migración 0003 no está marcada como aplicada")
        
        # Verificar si las tablas/columnas ya existen
        cursor.execute("PRAGMA table_info(mi_primer_app_camiseta);")
        columns = [row[1] for row in cursor.fetchall()]
        
        print("Columnas actuales en mi_primer_app_camiseta:")
        for col in columns:
            print(f"  - {col}")
        
        # Verificar si ya existe la tabla Carrito
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='mi_primer_app_carrito';")
        carrito_exists = cursor.fetchone()
        
        if 'activa' in columns and carrito_exists:
            print("\n✓ Las tablas/columnas de la migración ya existen")
            print("Marcando migración como aplicada...")
            
            # Insertar la migración como aplicada
            cursor.execute("""
                INSERT INTO django_migrations (app, name, applied)
                VALUES ('mi_primer_app', '0003_camiseta_activa_camiseta_fecha_creacion_and_more', datetime('now'))
            """)
            
            conn.commit()
            print("✓ Migración marcada como aplicada")
        else:
            print("\n❌ Las tablas/columnas no existen, se necesita aplicar la migración real")
    else:
        print("\n✅ La migración 0003 ya está aplicada")
    
    # 3. Estado final
    cursor.execute("SELECT COUNT(*) FROM django_migrations WHERE app = 'mi_primer_app';")
    total_migrations = cursor.fetchone()[0]
    print(f"\nTotal migraciones aplicadas para mi_primer_app: {total_migrations}")

except Exception as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    conn.close()

print("\n=== PROCESO COMPLETADO ===")
print("Reinicia el servidor Django para verificar el cambio")
