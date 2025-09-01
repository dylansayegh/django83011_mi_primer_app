from django.db import migrations
from django.contrib.auth.models import User

def crear_datos_iniciales(apps, schema_editor):
    """Crear camisetas y superusuario de prueba"""
    Camiseta = apps.get_model('mi_primer_app', 'Camiseta')
    
    # Crear camisetas si no existen
    camisetas_data = [
        {
            'equipo': 'Selección Argentina',
            'temporada': '1986 World Cup',
            'tipo': 'local',
            'talla': 'M',
            'precio': 89.99,
            'precio_oferta': 79.99,
            'stock': 15,
            'activa': True,
            'imagen': 'camisetas/argentina_1986.jpg',
            'descripcion': 'Camiseta retro de Argentina Mundial 1986 - Diego Maradona'
        },
        {
            'equipo': 'Real Madrid CF',
            'temporada': '1998-2000',
            'tipo': 'local',
            'talla': 'L',
            'precio': 94.99,
            'precio_oferta': 84.99,
            'stock': 12,
            'activa': True,
            'imagen': 'camisetas/real_madrid_1998.jpg',
            'descripcion': 'Camiseta histórica Real Madrid era Galácticos'
        },
        {
            'equipo': 'FC Barcelona',
            'temporada': '1992-1995',
            'tipo': 'local',
            'talla': 'L',
            'precio': 99.99,
            'precio_oferta': 89.99,
            'stock': 8,
            'activa': True,
            'imagen': 'camisetas/barcelona_1992.jpg',
            'descripcion': 'Camiseta FC Barcelona Dream Team de Cruyff'
        }
    ]
    
    for data in camisetas_data:
        if not Camiseta.objects.filter(equipo=data['equipo'], temporada=data['temporada']).exists():
            Camiseta.objects.create(**data)
    
    # Crear superusuario
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@admin.com', 'admin')

def eliminar_datos(apps, schema_editor):
    """Eliminar datos creados"""
    pass

class Migration(migrations.Migration):
    dependencies = [
        ('mi_primer_app', '0002_camiseta_cliente_compra_delete_familiar'),
    ]

    operations = [
        migrations.RunPython(crear_datos_iniciales, eliminar_datos),
    ]
