from django.core.management.base import BaseCommand
from mi_primer_app.models import Camiseta

class Command(BaseCommand):
    help = 'Poblar base de datos con camisetas de ejemplo'

    def handle(self, *args, **options):
        # Limpiar datos existentes
        Camiseta.objects.all().delete()
        
        camisetas_ejemplo = [
            {
                'equipo': 'Barcelona',
                'temporada': '1992-1995',
                'tipo': 'local',
                'talla': 'M',
                'precio': 89.99,
                'precio_oferta': 69.99,
                'stock': 15,
                'imagen': 'https://via.placeholder.com/300x400/004B87/FFD700?text=FCB+92-95',
                'descripcion': 'Camiseta retro del FC Barcelona, temporada 1992-1995. Dream Team de Cruyff.'
            },
            {
                'equipo': 'Real Madrid',
                'temporada': '1998-2000',
                'tipo': 'local',
                'talla': 'L',
                'precio': 79.99,
                'stock': 12,
                'imagen': 'https://via.placeholder.com/300x400/FFFFFF/000000?text=REAL+98-00',
                'descripcion': 'Camiseta histórica del Real Madrid de los Galácticos.'
            },
            {
                'equipo': 'Argentina',
                'temporada': '1986',
                'tipo': 'local',
                'talla': 'M',
                'precio': 129.99,
                'precio_oferta': 99.99,
                'stock': 8,
                'imagen': 'https://via.placeholder.com/300x400/75AADB/FFFFFF?text=ARG+86',
                'descripcion': 'Camiseta legendaria de Argentina Mundial 1986 - Maradona.'
            },
            {
                'equipo': 'Brazil',
                'temporada': '1970',
                'tipo': 'local',
                'talla': 'L',
                'precio': 119.99,
                'stock': 10,
                'imagen': 'https://via.placeholder.com/300x400/FFFF00/0000FF?text=BRA+70',
                'descripcion': 'Camiseta icónica de Brasil Mundial 1970 - Pelé.'
            },
            {
                'equipo': 'Milan',
                'temporada': '1989-1990',
                'tipo': 'local',
                'talla': 'XL',
                'precio': 94.99,
                'precio_oferta': 74.99,
                'stock': 6,
                'imagen': 'https://via.placeholder.com/300x400/FF0000/000000?text=ACM+89-90',
                'descripcion': 'AC Milan de Van Basten, Gullit y Rijkaard.'
            },
            {
                'equipo': 'Liverpool',
                'temporada': '1984',
                'tipo': 'local',
                'talla': 'S',
                'precio': 84.99,
                'stock': 20,
                'imagen': 'https://via.placeholder.com/300x400/C8102E/FFFFFF?text=LFC+84',
                'descripción': 'Liverpool retro de los años 80.'
            }
        ]
        
        for camiseta_data in camisetas_ejemplo:
            Camiseta.objects.create(**camiseta_data)
            
        self.stdout.write(
            self.style.SUCCESS(f'¡{len(camisetas_ejemplo)} camisetas creadas exitosamente!')
        )
