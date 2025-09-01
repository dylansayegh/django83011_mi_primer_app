#!/usr/bin/env python
import os
import sqlite3

# Conectar a la base de datos
conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

print("=== VERIFICANDO ESTADO DE MIGRACIONES ===")

try:
    # Ver migraciones aplicadas
    cursor.execute("SELECT app, name FROM django_migrations WHERE app = 'mi_primer_app' ORDER BY id;")
    migrations = cursor.fetchall()
    
    print("Migraciones aplicadas:")
    for app, name in migrations:
        print(f"  ✓ {app}.{name}")
    
    print(f"\nTotal migraciones aplicadas: {len(migrations)}")
    
    # Ver archivos de migración que existen
    import os
    migration_files = []
    migrations_dir = 'mi_primer_app/migrations'
    if os.path.exists(migrations_dir):
        for file in os.listdir(migrations_dir):
            if file.endswith('.py') and file != '__init__.py':
                migration_files.append(file)
    
    migration_files.sort()
    print(f"\nArchivos de migración encontrados:")
    for file in migration_files:
        print(f"  - {file}")
    
    print(f"\nTotal archivos: {len(migration_files)}")
    
    # Comparar
    if len(migration_files) > len(migrations):
        print(f"\n⚠️ HAY {len(migration_files) - len(migrations)} MIGRACIÓN(ES) PENDIENTE(S)")
    else:
        print("\n✅ TODAS LAS MIGRACIONES ESTÁN APLICADAS")

except Exception as e:
    print(f"Error: {e}")

finally:
    conn.close()
