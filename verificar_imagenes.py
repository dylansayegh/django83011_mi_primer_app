#!/usr/bin/env python3
"""
Script para verificar que las imágenes de camisetas funcionan correctamente
"""
import os
from pathlib import Path

def verificar_imagenes():
    print("🔍 VERIFICANDO IMÁGENES DE CAMISETAS")
    print("=" * 50)
    
    # Ruta base
    base_dir = Path(__file__).parent
    images_dir = base_dir / "static" / "images" / "camisetas"
    
    # Imágenes esperadas
    imagenes_esperadas = [
        "argentina_1986.jpg",
        "real_madrid_1998.jpg", 
        "barcelona_1992.jpg"
    ]
    
    print(f"📁 Directorio: {images_dir}")
    print(f"🎯 Verificando {len(imagenes_esperadas)} imágenes...")
    
    resultados = []
    
    for imagen in imagenes_esperadas:
        filepath = images_dir / imagen
        
        if filepath.exists():
            size = filepath.stat().st_size
            size_kb = round(size / 1024, 2)
            
            if size_kb > 0:
                status = "✅ EXISTE"
                if size_kb > 500:
                    status += f" ⚠️ GRANDE ({size_kb}KB)"
                else:
                    status += f" ({size_kb}KB)"
            else:
                status = "❌ VACÍO"
        else:
            status = "❌ FALTA"
        
        print(f"  {imagen}: {status}")
        resultados.append((imagen, filepath.exists(), size_kb if filepath.exists() else 0))
    
    # Resumen
    existentes = sum(1 for _, exists, _ in resultados if exists)
    
    print(f"\n📊 RESUMEN:")
    print(f"✅ Imágenes encontradas: {existentes}/{len(imagenes_esperadas)}")
    
    if existentes == len(imagenes_esperadas):
        print("🎉 ¡TODAS LAS IMÁGENES ESTÁN LISTAS!")
        print("💡 Las imágenes se verán en:")
        print("   - README.md del proyecto")
        print("   - Página web del catálogo")
        print("   - Panel de administración")
    else:
        print("⚠️  Faltan imágenes por agregar")
        print("📋 Consulta: INSTRUCCIONES_IMAGENES_SEGURO.md")
    
    # Verificar si el servidor puede acceder a las imágenes
    print(f"\n🌐 URLs de las imágenes:")
    for imagen in imagenes_esperadas:
        url = f"http://127.0.0.1:8000/static/images/camisetas/{imagen}"
        print(f"   {url}")
    
    print(f"\n🎯 Para ver las imágenes:")
    print(f"   1. Ejecuta: python manage.py runserver")
    print(f"   2. Abre: http://127.0.0.1:8000")

if __name__ == "__main__":
    verificar_imagenes()
