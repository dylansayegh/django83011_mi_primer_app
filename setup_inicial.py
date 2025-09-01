import sys
import os

# Agregar el directorio del proyecto al path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')

try:
    import django
    django.setup()
    
    from django.contrib.auth.models import User
    from mi_primer_app.models import Camiseta
    
    print("=== CREANDO DATOS INICIALES ===")
    
    # Crear superusuario
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@test.com', 'admin')
        print("✓ Superusuario 'admin' creado (password: admin)")
    else:
        print("- Superusuario 'admin' ya existe")
    
    # Crear camisetas
    camisetas_data = [
        {
            'equipo': 'Selección Argentina',
            'temporada': '1986 World Cup',
            'tipo': 'local',
            'talla': 'M',
            'precio': 89.99,
            'precio_oferta': 79.99,
            'stock': 5,
            'activa': True,
            'imagen': 'camisetas/argentina_1986.jpg',
            'descripcion': 'Camiseta retro de Argentina Mundial 1986'
        },
        {
            'equipo': 'Real Madrid CF',
            'temporada': '1998-2000',
            'tipo': 'local',
            'talla': 'L',
            'precio': 94.99,
            'precio_oferta': 84.99,
            'stock': 3,
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
            'stock': 7,
            'activa': True,
            'imagen': 'camisetas/barcelona_1992.jpg',
            'descripcion': 'Camiseta FC Barcelona Dream Team'
        }
    ]
    
    created_count = 0
    for data in camisetas_data:
        camiseta, created = Camiseta.objects.get_or_create(
            equipo=data['equipo'],
            temporada=data['temporada'],
            defaults=data
        )
        if created:
            created_count += 1
            print(f"✓ Camiseta creada: {camiseta.equipo} {camiseta.temporada}")
        else:
            print(f"- Camiseta ya existe: {camiseta.equipo} {camiseta.temporada}")
    
    print(f"\n=== RESUMEN ===")
    print(f"Usuarios totales: {User.objects.count()}")
    print(f"Camisetas totales: {Camiseta.objects.count()}")
    print(f"Camisetas activas: {Camiseta.objects.filter(activa=True).count()}")
    print("\n¡Todo configurado! Puedes acceder a:")
    print("- http://127.0.0.1:8000 (sitio principal)")
    print("- http://127.0.0.1:8000/admin (admin: admin/admin)")
    
except Exception as e:
    print(f"Error: {e}")
    import traceback
    traceback.print_exc()
