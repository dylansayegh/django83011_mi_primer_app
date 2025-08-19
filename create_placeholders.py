#!/usr/bin/env python3
"""
Crear imágenes placeholder para las camisetas hasta que se suban las reales
"""

from PIL import Image, ImageDraw, ImageFont
import os

def create_placeholder_images():
    """
    Crear imágenes placeholder para las camisetas
    """
    print("🖼️ CREANDO IMÁGENES PLACEHOLDER")
    print("=" * 40)
    
    camisetas_dir = "static/images/camisetas"
    
    # Información de las camisetas
    camisetas = [
        {
            "filename": "argentina_1986.jpg",
            "color": "#87CEEB",  # Celeste
            "text": "ARGENTINA\n1986\nLE COQ SPORTIF",
            "description": "Camiseta de Maradona"
        },
        {
            "filename": "real_madrid_1998.jpg", 
            "color": "#FFFFFF",  # Blanco
            "text": "REAL MADRID\n1998-2000\nADIDAS TEKA",
            "description": "Era Galácticos"
        },
        {
            "filename": "barcelona_1992.jpg",
            "color": "#004D98",  # Azul Barcelona
            "text": "FC BARCELONA\n1992-1995\nKAPPA",
            "description": "Dream Team Cruyff"
        }
    ]
    
    for camiseta in camisetas:
        try:
            # Crear imagen 400x400
            img = Image.new('RGB', (400, 400), camiseta["color"])
            draw = ImageDraw.Draw(img)
            
            # Intentar usar una fuente del sistema
            try:
                font = ImageFont.truetype("arial.ttf", 24)
                small_font = ImageFont.truetype("arial.ttf", 16)
            except:
                font = ImageFont.load_default()
                small_font = ImageFont.load_default()
            
            # Dibujar texto principal
            text_color = "#FFFFFF" if camiseta["color"] == "#004D98" else "#000000"
            
            # Calcular posición del texto centrado
            bbox = draw.textbbox((0, 0), camiseta["text"], font=font)
            text_width = bbox[2] - bbox[0]
            text_height = bbox[3] - bbox[1]
            
            x = (400 - text_width) // 2
            y = (400 - text_height) // 2 - 20
            
            draw.multiline_text((x, y), camiseta["text"], 
                              font=font, fill=text_color, align="center")
            
            # Añadir descripción
            desc_y = y + text_height + 30
            desc_bbox = draw.textbbox((0, 0), camiseta["description"], font=small_font)
            desc_width = desc_bbox[2] - desc_bbox[0]
            desc_x = (400 - desc_width) // 2
            
            draw.text((desc_x, desc_y), camiseta["description"], 
                     font=small_font, fill=text_color)
            
            # Guardar imagen
            filepath = os.path.join(camisetas_dir, camiseta["filename"])
            img.save(filepath, "JPEG", quality=95)
            print(f"✅ Placeholder creado: {filepath}")
            
        except Exception as e:
            print(f"❌ Error creando {camiseta['filename']}: {e}")
            # Crear un archivo de texto como fallback
            txt_path = os.path.join(camisetas_dir, camiseta["filename"].replace('.jpg', '.txt'))
            with open(txt_path, 'w') as f:
                f.write(f"Placeholder para: {camiseta['text']}\n{camiseta['description']}")
            print(f"📝 Fallback creado: {txt_path}")

if __name__ == "__main__":
    try:
        create_placeholder_images()
    except ImportError:
        print("⚠️  PIL no disponible, creando archivos de texto como placeholder")
        
        camisetas_dir = "static/images/camisetas"
        placeholders = [
            ("argentina_1986.jpg", "ARGENTINA 1986 - MARADONA"),
            ("real_madrid_1998.jpg", "REAL MADRID 1998-2000 - TEKA"),
            ("barcelona_1992.jpg", "FC BARCELONA 1992-1995 - DREAM TEAM")
        ]
        
        for filename, text in placeholders:
            txt_path = os.path.join(camisetas_dir, filename.replace('.jpg', '_placeholder.txt'))
            with open(txt_path, 'w', encoding='utf-8') as f:
                f.write(f"📸 PLACEHOLDER PARA: {text}\n")
                f.write(f"Archivo esperado: {filename}\n")
                f.write("Reemplazar con la imagen real para ver en el README")
            print(f"📝 Placeholder creado: {txt_path}")
