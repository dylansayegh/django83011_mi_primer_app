from django.core.management.base import BaseCommand
from mi_primer_app.models import Camiseta
from django.db import transaction

class Command(BaseCommand):
    help = 'Poblar base de datos con camisetas retro icónicas'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('👕 POBLANDO BASE DE DATOS CON CAMISETAS RETRO'))
        self.stdout.write('=' * 60)
        
        # Limpiar camisetas existentes (opcional)
        # Camiseta.objects.all().delete()
        
        camisetas_iconicas = [
            # Argentina 1986
            {
                'equipo': 'Selección Argentina',
                'temporada': '1986 World Cup',
                'tipo': 'local',
                'talla': 'M',
                'precio': 89.99,
                'precio_oferta': 79.99,
                'stock': 15,
                'descripcion': 'Camiseta icónica usada por Maradona en el Mundial de México 1986',
                'marca': 'Le Coq Sportif',
                'numero_jugador': 10,
                'nombre_jugador': 'MARADONA',
                'imagen': 'images/camisetas/argentina_1986.jpg',
                'año_fabricacion': 1986,
                'disponible': True,
                'destacada': True
            },
            {
                'equipo': 'Selección Argentina', 
                'temporada': '1986 World Cup',
                'tipo': 'local',
                'talla': 'L',
                'precio': 89.99,
                'precio_oferta': 79.99,
                'stock': 12,
                'descripcion': 'Camiseta icónica usada por Maradona en el Mundial de México 1986',
                'marca': 'Le Coq Sportif',
                'numero_jugador': 10,
                'nombre_jugador': 'MARADONA',
                'imagen': 'images/camisetas/argentina_1986.jpg',
                'año_fabricacion': 1986,
                'disponible': True,
                'destacada': True
            },
            
            # Real Madrid 1998-2000
            {
                'equipo': 'Real Madrid CF',
                'temporada': '1998-2000',
                'tipo': 'local',
                'talla': 'M',
                'precio': 94.99,
                'precio_oferta': 84.99,
                'stock': 8,
                'descripcion': 'Camiseta clásica del Real Madrid era pre-galácticos',
                'marca': 'Adidas',
                'numero_jugador': 7,
                'nombre_jugador': 'RAUL',
                'imagen': 'images/camisetas/real_madrid_1998.jpg',
                'año_fabricacion': 1998,
                'disponible': True,
                'destacada': True
            },
            {
                'equipo': 'Real Madrid CF',
                'temporada': '1998-2000', 
                'tipo': 'local',
                'talla': 'L',
                'precio': 94.99,
                'precio_oferta': 84.99,
                'stock': 10,
                'descripcion': 'Camiseta clásica del Real Madrid era pre-galácticos',
                'marca': 'Adidas',
                'numero_jugador': 3,
                'nombre_jugador': 'ROBERTO CARLOS',
                'imagen': 'images/camisetas/real_madrid_1998.jpg',
                'año_fabricacion': 1998,
                'disponible': True,
                'destacada': True
            },
            
            # FC Barcelona 1992-1995
            {
                'equipo': 'FC Barcelona',
                'temporada': '1992-1995',
                'tipo': 'local',
                'talla': 'M',
                'precio': 99.99,
                'precio_oferta': 89.99,
                'stock': 6,
                'descripcion': 'Camiseta histórica del Dream Team de Johan Cruyff',
                'marca': 'Kappa',
                'numero_jugador': 11,
                'nombre_jugador': 'ROMARIO',
                'imagen': 'images/camisetas/barcelona_1992.jpg',
                'año_fabricacion': 1992,
                'disponible': True,
                'destacada': True
            },
            {
                'equipo': 'FC Barcelona',
                'temporada': '1992-1995',
                'tipo': 'local', 
                'talla': 'L',
                'precio': 99.99,
                'precio_oferta': 89.99,
                'stock': 9,
                'descripcion': 'Camiseta histórica del Dream Team de Johan Cruyff',
                'marca': 'Kappa',
                'numero_jugador': 8,
                'nombre_jugador': 'STOICHKOV',
                'imagen': 'images/camisetas/barcelona_1992.jpg',
                'año_fabricacion': 1992,
                'disponible': True,
                'destacada': True
            }
        ]
        
        camisetas_creadas = 0
        
        with transaction.atomic():
            for data in camisetas_iconicas:
                # Crear camiseta con los campos que existen en el modelo
                camiseta_data = {
                    'equipo': data['equipo'],
                    'temporada': data['temporada'], 
                    'tipo': data['tipo'],
                    'talla': data['talla'],
                    'precio': data['precio'],
                    'stock': data['stock']
                }
                
                # Añadir precio_oferta si está disponible
                if 'precio_oferta' in data:
                    camiseta_data['precio_oferta'] = data['precio_oferta']
                
                # Añadir campos adicionales si existen en el modelo
                campos_opcionales = [
                    'descripcion', 'marca', 'numero_jugador', 'nombre_jugador',
                    'imagen', 'año_fabricacion', 'disponible', 'destacada'
                ]
                
                for campo in campos_opcionales:
                    if campo in data and hasattr(Camiseta, campo):
                        camiseta_data[campo] = data[campo]
                
                camiseta, created = Camiseta.objects.get_or_create(
                    equipo=data['equipo'],
                    temporada=data['temporada'],
                    talla=data['talla'],
                    tipo=data['tipo'],
                    defaults=camiseta_data
                )
                
                if created:
                    camisetas_creadas += 1
                    self.stdout.write(
                        self.style.SUCCESS(
                            f'✅ {data["equipo"]} {data["temporada"]} (Talla {data["talla"]})'
                        )
                    )
                else:
                    self.stdout.write(
                        self.style.WARNING(
                            f'⚠️  Ya existe: {data["equipo"]} {data["temporada"]} (Talla {data["talla"]})'
                        )
                    )
        
        self.stdout.write('\n' + '=' * 60)
        self.stdout.write(
            self.style.SUCCESS(
                f'🎯 COMPLETADO: {camisetas_creadas} camisetas retro creadas'
            )
        )
        self.stdout.write(
            self.style.SUCCESS(
                f'📊 Total en catálogo: {Camiseta.objects.count()} camisetas'
            )
        )
