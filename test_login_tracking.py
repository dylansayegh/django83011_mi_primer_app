#!/usr/bin/env python
"""
Script de prueba para demostrar el sistema de tracking de logins
"""
import os
import django
import sys

# Configurar Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from accounts.models import Profile, LoginLog
from django.test.client import Client
from django.test import RequestFactory
from accounts.views import get_client_ip, log_user_login

def test_login_system():
    print("🚀 PRUEBA DEL SISTEMA DE TRACKING DE LOGINS")
    print("=" * 50)
    
    # Verificar usuario existente
    try:
        user = User.objects.get(username='dylan')
        print(f"✅ Usuario encontrado: {user.username}")
        print(f"📧 Email: {user.email or 'No especificado'}")
        print(f"📅 Miembro desde: {user.date_joined.strftime('%d/%m/%Y')}")
    except User.DoesNotExist:
        print("❌ Usuario 'dylan' no encontrado")
        return
    
    # Verificar perfil
    profile, created = Profile.objects.get_or_create(user=user)
    print(f"📋 Perfil {'creado' if created else 'existente'}")
    print(f"🔄 Logins actuales: {profile.login_count}")
    
    # Simular una solicitud de login
    factory = RequestFactory()
    request = factory.post('/auth/login/', {
        'username': 'dylan', 
        'password': 'test123'
    })
    
    # Simular headers de una solicitud real
    request.META['HTTP_USER_AGENT'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
    request.META['REMOTE_ADDR'] = '127.0.0.1'
    request.session = {}
    
    print("\n🌐 Simulando login desde:")
    print(f"   IP: {get_client_ip(request)}")
    print(f"   User-Agent: {request.META.get('HTTP_USER_AGENT')[:50]}...")
    
    # Ejecutar la función de logging manualmente
    try:
        log_user_login(sender=None, request=request, user=user)
        print("✅ Datos de login guardados exitosamente")
    except Exception as e:
        print(f"❌ Error: {e}")
        return
    
    # Mostrar estadísticas actualizadas
    profile.refresh_from_db()
    print(f"\n📊 ESTADÍSTICAS ACTUALIZADAS:")
    print(f"🔄 Total logins: {profile.login_count}")
    print(f"🌐 Última IP: {profile.last_login_ip}")
    print(f"📅 Actualizado: {profile.updated_at.strftime('%d/%m/%Y %H:%M')}")
    
    # Mostrar logs recientes
    recent_logs = LoginLog.objects.filter(user=user).order_by('-login_time')[:3]
    if recent_logs:
        print(f"\n📝 ÚLTIMOS {len(recent_logs)} LOGS:")
        for i, log in enumerate(recent_logs, 1):
            status = "✅ Exitoso" if log.success else "❌ Fallido"
            print(f"   {i}. {log.login_time.strftime('%d/%m/%Y %H:%M:%S')} - {log.ip_address} - {status}")
    
    print(f"\n🎯 RESUMEN:")
    print(f"   • Usuario: {user.username}")
    print(f"   • Total logins registrados: {profile.login_count}")
    print(f"   • Logs en base de datos: {LoginLog.objects.filter(user=user).count()}")
    print(f"   • Sistema funcionando: ✅")

if __name__ == "__main__":
    test_login_system()
