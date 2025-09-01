#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3
import os

# Conectar a la base de datos
db_path = 'db.sqlite3'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

print("=== INSERTANDO DATOS DIRECTAMENTE EN SQLITE ===")

try:
    # 1. Primero, verificar estructura de tablas
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE '%camiseta%';")
    tables = cursor.fetchall()
    print("Tablas encontradas:", tables)
    
    # 2. Verificar si hay camisetas
    cursor.execute("SELECT COUNT(*) FROM mi_primer_app_camiseta;")
    count = cursor.fetchone()[0]
    print(f"Camisetas existentes: {count}")
    
    if count == 0:
        print("Insertando camisetas...")
        
        # Insertar camisetas de prueba
        camisetas = [
            ('Selección Argentina', '1986 World Cup', 'local', 'M', 89.99, 79.99, 15, 1, 
             'camisetas/argentina_1986.jpg', 'Camiseta retro Argentina Mundial 1986'),
            ('Real Madrid CF', '1998-2000', 'local', 'L', 94.99, 84.99, 12, 1,
             'camisetas/real_madrid_1998.jpg', 'Camiseta Real Madrid era Galácticos'),
            ('FC Barcelona', '1992-1995', 'local', 'L', 99.99, 89.99, 8, 1,
             'camisetas/barcelona_1992.jpg', 'Camiseta FC Barcelona Dream Team')
        ]
        
        for camiseta in camisetas:
            cursor.execute("""
                INSERT INTO mi_primer_app_camiseta 
                (equipo, temporada, tipo, talla, precio, precio_oferta, stock, activa, 
                 imagen, descripcion, fecha_creacion, fecha_actualizacion)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, datetime('now'), datetime('now'))
            """, camiseta)
        
        conn.commit()
        print("✓ Camisetas insertadas")
    
    # 3. Verificar usuarios
    cursor.execute("SELECT COUNT(*) FROM auth_user WHERE username='admin';")
    admin_count = cursor.fetchone()[0]
    
    if admin_count == 0:
        print("Creando usuario admin...")
        # Insertar usuario admin (contraseña: admin)
        cursor.execute("""
            INSERT INTO auth_user 
            (username, first_name, last_name, email, is_staff, is_active, is_superuser, 
             date_joined, password)
            VALUES ('admin', '', '', 'admin@admin.com', 1, 1, 1, 
                    datetime('now'), 'pbkdf2_sha256$600000$admin$admin')
        """)
        conn.commit()
        print("✓ Usuario admin creado")
    
    # 4. Mostrar resumen final
    cursor.execute("SELECT COUNT(*) FROM mi_primer_app_camiseta;")
    camisetas_count = cursor.fetchone()[0]
    
    cursor.execute("SELECT COUNT(*) FROM auth_user;")
    users_count = cursor.fetchone()[0]
    
    print(f"\n=== RESUMEN FINAL ===")
    print(f"Total camisetas: {camisetas_count}")
    print(f"Total usuarios: {users_count}")
    
    if camisetas_count > 0:
        print("\n=== CAMISETAS DISPONIBLES ===")
        cursor.execute("SELECT id, equipo, temporada, precio, precio_oferta FROM mi_primer_app_camiseta;")
        for row in cursor.fetchall():
            print(f"ID: {row[0]} - {row[1]} {row[2]} - ${row[4] if row[4] else row[3]}")
    
    print("\n¡Datos insertados! Recarga la página web.")

except Exception as e:
    print(f"Error: {e}")
    conn.rollback()

finally:
    conn.close()
