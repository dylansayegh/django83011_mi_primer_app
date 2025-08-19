#!/usr/bin/env python3
"""
Script para crear imágenes mejoradas de las camisetas retro
"""
from PIL import Image, ImageDraw, ImageFont
import os

def create_realistic_shirt_images():
    """
    Crear imágenes más realistas de las camisetas basadas en las que me mostraste
    """
    print("🎨 CREANDO IMÁGENES MEJORADAS DE CAMISETAS")
    print("=" * 50)
    
    camisetas_dir = "static/images/camisetas"
    
    # Configuración de camisetas basadas en las imágenes reales que me mostraste
    camisetas = [
        {
            "filename": "argentina_1986.jpg",
            "colors": ["#87CEEB", "#4169E1"],  # Celeste y azul
            "text_main": "ARGENTINA",
            "text_sub": "WORLD CUP 1986",
            "text_brand": "LE COQ SPORTIF",
            "number": "10",
            "player": "MARADONA",
            "description": "Camiseta icónica del Mundial México '86"
        },
        {
            "filename": "real_madrid_1998.jpg", 
            "colors": ["#FFFFFF", "#000080"],  # Blanco con detalles azul marino
            "text_main": "REAL MADRID",
            "text_sub": "1998-2000",
            "text_brand": "adidas",
            "sponsor": "Teka",
            "number": "7",
            "player": "RAÚL",
            "description": "Era pre-galácticos del Real Madrid"
        },
        {
            "filename": "barcelona_1992.jpg",
            "colors": ["#004D98", "#DC143C"],  # Azul Barcelona y rojo
            "text_main": "FC BARCELONA",
            "text_sub": "DREAM TEAM 1992-1995", 
            "text_brand": "Kappa",
            "number": "11",
            "player": "ROMÁRIO",
            "description": "Camiseta del Dream Team de Cruyff"
        }
    ]
    
    for camiseta in camisetas:
        try:
            print(f"🎯 Creando: {camiseta['filename']}")
            
            # Crear imagen más grande y realista
            width, height = 600, 700
            img = Image.new('RGB', (width, height), 'white')
            draw = ImageDraw.Draw(img)
            
            # Simular forma de camiseta
            primary_color = camiseta["colors"][0]
            secondary_color = camiseta["colors"][1] if len(camiseta["colors"]) > 1 else primary_color
            
            # Dibujar la camiseta según el equipo
            if "argentina" in camiseta["filename"]:
                # Rayas verticales celestes y azules como Argentina 1986
                stripe_width = width // 8
                for i in range(8):
                    color = primary_color if i % 2 == 0 else secondary_color
                    draw.rectangle([i * stripe_width, 100, (i + 1) * stripe_width, height - 50], fill=color)
                
                # Cuello en V
                draw.polygon([(width//2 - 40, 100), (width//2 + 40, 100), (width//2, 140)], fill=secondary_color)
                
            elif "real_madrid" in camiseta["filename"]:
                # Fondo blanco con detalles azul marino como Real Madrid 1998
                draw.rectangle([50, 100, width-50, height-50], fill=primary_color)
                
                # Detalles en mangas (azul marino)
                draw.rectangle([50, 100, 100, 200], fill=secondary_color)
                draw.rectangle([width-100, 100, width-50, 200], fill=secondary_color)
                
                # Cuello con detalles
                draw.rectangle([width//2-60, 100, width//2+60, 120], fill=secondary_color)
                
            elif "barcelona" in camiseta["filename"]:
                # Rayas verticales azul y rojo como Barcelona 1992
                stripe_width = width // 6
                for i in range(6):
                    color = primary_color if i % 2 == 0 else secondary_color
                    draw.rectangle([50 + i * stripe_width, 100, 50 + (i + 1) * stripe_width, height - 50], fill=color)
                
                # Cuello especial
                draw.rectangle([width//2-50, 100, width//2+50, 130], fill=primary_color)
            
            # Configurar fuentes
            try:
                font_large = ImageFont.truetype("arial.ttf", 36)
                font_medium = ImageFont.truetype("arial.ttf", 24)
                font_small = ImageFont.truetype("arial.ttf", 18)
                font_number = ImageFont.truetype("arial.ttf", 120)
            except:
                font_large = ImageFont.load_default()
                font_medium = ImageFont.load_default()
                font_small = ImageFont.load_default()
                font_number = ImageFont.load_default()
            
            # Color del texto
            text_color = "white" if primary_color != "#FFFFFF" else "black"
            
            # Texto principal (nombre del equipo)
            text = camiseta["text_main"]
            bbox = draw.textbbox((0, 0), text, font=font_large)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, 150), text, font=font_large, fill=text_color)
            
            # Subtexto (año/temporada)
            text = camiseta["text_sub"]
            bbox = draw.textbbox((0, 0), text, font=font_medium)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, 190), text, font=font_medium, fill=text_color)
            
            # Marca
            text = camiseta["text_brand"]
            bbox = draw.textbbox((0, 0), text, font=font_small)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, 230), text, font=font_small, fill=text_color)
            
            # Patrocinador (solo Real Madrid)
            if "sponsor" in camiseta:
                text = camiseta["sponsor"]
                bbox = draw.textbbox((0, 0), text, font=font_medium)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                draw.text((x, 300), text, font=font_medium, fill="black" if primary_color == "#FFFFFF" else "white")
            
            # Número del jugador
            if "number" in camiseta:
                number = camiseta["number"]
                bbox = draw.textbbox((0, 0), number, font=font_number)
                text_width = bbox[2] - bbox[0]
                x = (width - text_width) // 2
                draw.text((x, 400), number, font=font_number, fill=text_color)
                
                # Nombre del jugador
                if "player" in camiseta:
                    player = camiseta["player"]
                    bbox = draw.textbbox((0, 0), player, font=font_medium)
                    text_width = bbox[2] - bbox[0]
                    x = (width - text_width) // 2
                    draw.text((x, 530), player, font=font_medium, fill=text_color)
            
            # Descripción abajo
            desc = camiseta["description"]
            bbox = draw.textbbox((0, 0), desc, font=font_small)
            text_width = bbox[2] - bbox[0]
            x = (width - text_width) // 2
            draw.text((x, height - 30), desc, font=font_small, fill="gray")
            
            # Guardar imagen
            filepath = os.path.join(camisetas_dir, camiseta["filename"])
            img.save(filepath, "JPEG", quality=95)
            print(f"✅ {camiseta['filename']} creada exitosamente")
            
        except Exception as e:
            print(f"❌ Error creando {camiseta['filename']}: {e}")
    
    print(f"\n🎉 ¡IMÁGENES MEJORADAS CREADAS!")
    print(f"📁 Ubicación: {os.path.abspath(camisetas_dir)}")
    print(f"🌐 Verifica en: http://127.0.0.1:8000/static/images/camisetas/")

if __name__ == "__main__":
    create_realistic_shirt_images()
