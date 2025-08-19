#!/usr/bin/env python3
"""
Script para integrar las imágenes de camisetas en el proyecto Django
"""

import os
import shutil

def setup_camisetas_images():
    """
    Configurar las imágenes de camisetas para el proyecto
    """
    print("📸 CONFIGURANDO IMÁGENES DE CAMISETAS")
    print("=" * 50)
    
    # Rutas
    static_images = "static/images"
    camisetas_dir = os.path.join(static_images, "camisetas")
    
    # Crear directorios si no existen
    os.makedirs(camisetas_dir, exist_ok=True)
    
    # Información de las camisetas mostradas
    camisetas_info = [
        {
            "filename": "argentina_1986.jpg",
            "nombre": "Argentina 1986 Le Coq Sportif",
            "descripcion": "Camiseta icónica de Argentina Mundial 1986 con Maradona",
            "equipo": "Selección Argentina",
            "año": "1986",
            "marca": "Le Coq Sportif",
            "precio": 89.99,
            "colores": "Azul y Celeste",
            "talla": ["S", "M", "L", "XL"]
        },
        {
            "filename": "real_madrid_1998.jpg", 
            "nombre": "Real Madrid 1998-2000 Teka",
            "descripcion": "Camiseta clásica del Real Madrid temporada 1998-2000",
            "equipo": "Real Madrid CF",
            "año": "1998-2000", 
            "marca": "Adidas",
            "precio": 94.99,
            "colores": "Blanco",
            "talla": ["S", "M", "L", "XL"]
        },
        {
            "filename": "barcelona_1992.jpg",
            "nombre": "Barcelona 1992-1995 Dream Team", 
            "descripcion": "Camiseta histórica del Dream Team de Cruyff",
            "equipo": "FC Barcelona",
            "año": "1992-1995",
            "marca": "Kappa", 
            "precio": 99.99,
            "colores": "Azul y Rojo",
            "talla": ["S", "M", "L", "XL"]
        }
    ]
    
    print(f"📁 Directorio creado: {camisetas_dir}")
    
    # Crear archivos de información para cada camiseta
    for camiseta in camisetas_info:
        info_file = os.path.join(camisetas_dir, f"{camiseta['filename'].replace('.jpg', '_info.txt')}")
        
        with open(info_file, 'w', encoding='utf-8') as f:
            f.write(f"# {camiseta['nombre']}\n\n")
            f.write(f"**Equipo:** {camiseta['equipo']}\n")
            f.write(f"**Año:** {camiseta['año']}\n")
            f.write(f"**Marca:** {camiseta['marca']}\n")
            f.write(f"**Precio:** ${camiseta['precio']}\n")
            f.write(f"**Colores:** {camiseta['colores']}\n")
            f.write(f"**Tallas:** {', '.join(camiseta['talla'])}\n\n")
            f.write(f"**Descripción:** {camiseta['descripcion']}\n")
        
        print(f"✅ Info creada: {info_file}")
    
    # Crear placeholder images hasta que se suban las reales
    placeholder_note = os.path.join(camisetas_dir, "README_IMAGENES.md")
    with open(placeholder_note, 'w', encoding='utf-8') as f:
        f.write("# 📸 INSTRUCCIONES PARA LAS IMÁGENES\n\n")
        f.write("Para que las imágenes aparezcan correctamente:\n\n")
        f.write("1. **Guarda las imágenes aquí** con estos nombres:\n")
        for camiseta in camisetas_info:
            f.write(f"   - `{camiseta['filename']}`\n")
        f.write("\n2. **Formatos recomendados:**\n")
        f.write("   - JPG o PNG\n")
        f.write("   - Resolución: 800x800px mínimo\n") 
        f.write("   - Fondo transparente o blanco preferible\n")
        f.write("\n3. **Las imágenes se verán:**\n")
        f.write("   - En el README del proyecto\n")
        f.write("   - En la página web del catálogo\n")
        f.write("   - En las tarjetas de productos\n")
    
    print(f"📝 Instrucciones creadas: {placeholder_note}")
    print("\n🎯 CONFIGURACIÓN COMPLETADA")
    print(f"📁 Coloca las imágenes en: {os.path.abspath(camisetas_dir)}")

if __name__ == "__main__":
    setup_camisetas_images()
