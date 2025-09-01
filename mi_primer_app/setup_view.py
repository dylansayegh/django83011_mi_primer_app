from django.http import HttpResponse
from django.contrib.auth.models import User
from mi_primer_app.models import Camiseta

def setup_datos(request):
    """Vista especial para crear datos de prueba"""
    html = "<h1>Configurando Datos de Prueba</h1>"
    
    try:
        # 1. Crear superusuario
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
            html += "<p>✓ Superusuario 'admin' creado (password: admin)</p>"
        else:
            html += "<p>- Superusuario 'admin' ya existe</p>"
        
        # 2. Crear camisetas
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
                'descripcion': 'Camiseta retro de Argentina Mundial 1986'
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
                html += f"<p>✓ Camiseta creada: {camiseta.equipo} {camiseta.temporada} - ${camiseta.precio_final}</p>"
        
        # 3. Resumen
        html += f"<h3>Resumen</h3>"
        html += f"<p>Total usuarios: {User.objects.count()}</p>"
        html += f"<p>Total camisetas: {Camiseta.objects.count()}</p>"
        html += f"<p>Camisetas activas: {Camiseta.objects.filter(activa=True).count()}</p>"
        
        html += "<hr>"
        html += "<h3>¡Configuración completada!</h3>"
        html += '<p><a href="/">Ir a página principal</a></p>'
        html += '<p><a href="/admin/">Ir al admin (admin/admin)</a></p>'
        html += '<p><a href="/carrito/">Ver carrito</a></p>'
        
    except Exception as e:
        html += f"<p style='color: red;'>Error: {e}</p>"
    
    return HttpResponse(html)
