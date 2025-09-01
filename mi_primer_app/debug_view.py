from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from mi_primer_app.models import Camiseta, Carrito, ItemCarrito

@login_required
def debug_carrito(request):
    """Vista para debuggear el carrito"""
    html = "<h1>DEBUG CARRITO</h1>"
    
    try:
        # 1. Verificar usuario
        html += f"<h2>Usuario actual: {request.user.username}</h2>"
        
        # 2. Verificar camisetas
        camisetas = Camiseta.objects.all()
        html += f"<h2>Camisetas en BD ({camisetas.count()})</h2>"
        for c in camisetas:
            html += f"<p>ID: {c.id} - {c.equipo} {c.temporada} - Activa: {c.activa} - Stock: {c.stock}</p>"
        
        # 3. Verificar carrito del usuario
        try:
            carrito = Carrito.objects.get(usuario=request.user)
            html += f"<h2>Carrito encontrado - ID: {carrito.id}</h2>"
            
            # 4. Verificar items del carrito
            items = carrito.items.all()
            html += f"<h3>Items en carrito ({items.count()})</h3>"
            for item in items:
                html += f"<p>- {item.cantidad} x {item.camiseta.equipo} (ID: {item.camiseta.id})</p>"
            
            html += f"<p><strong>Total items: {carrito.cantidad_items()}</strong></p>"
            html += f"<p><strong>Total precio: ${carrito.calcular_total()}</strong></p>"
            
        except Carrito.DoesNotExist:
            html += "<h2>❌ NO HAY CARRITO para este usuario</h2>"
        
        # 5. Botón para agregar manualmente
        if camisetas.exists():
            primera_camiseta = camisetas.first()
            html += f"""
            <h2>Test Manual</h2>
            <form method="post" action="/carrito/agregar/{primera_camiseta.id}/">
                <input type="hidden" name="csrfmiddlewaretoken" value="{request.META.get('CSRF_COOKIE', 'test')}">
                <input type="hidden" name="cantidad" value="1">
                <button type="submit">Agregar {primera_camiseta.equipo} manualmente</button>
            </form>
            """
        
        html += '<br><br><a href="/carrito/">Ver carrito normal</a>'
        html += '<br><a href="/">Volver al inicio</a>'
        
    except Exception as e:
        html += f"<p style='color: red;'>Error: {e}</p>"
        import traceback
        html += f"<pre>{traceback.format_exc()}</pre>"
    
    return HttpResponse(html)
