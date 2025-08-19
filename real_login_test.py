#!/usr/bin/env python
"""
Script para hacer un login real y verificar el tracking
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.test import Client
from django.contrib.auth.models import User
from accounts.models import Profile, LoginLog

def real_login_test():
    print("🔐 PRUEBA DE LOGIN REAL")
    print("=" * 40)
    
    # Crear cliente de prueba
    client = Client()
    
    # Verificar que el usuario existe
    try:
        user = User.objects.get(username='dylan')
        print(f"✅ Usuario encontrado: {user.username}")
    except User.DoesNotExist:
        print("❌ Usuario no encontrado")
        return
    
    # Obtener estadísticas antes del login
    profile = Profile.objects.get(user=user)
    logins_before = profile.login_count
    logs_before = LoginLog.objects.filter(user=user).count()
    
    print(f"📊 Antes del login:")
    print(f"   Logins: {logins_before}")
    print(f"   Logs: {logs_before}")
    
    # Hacer login usando el cliente de Django
    response = client.post('/auth/login/', {
        'username': 'dylan',
        'password': 'dylan123'  # Asumiendo esta contraseña
    }, follow=True)
    
    print(f"\n🌐 Respuesta del login:")
    print(f"   Status code: {response.status_code}")
    print(f"   URL final: {response.wsgi_request.get_full_path()}")
    
    # Verificar estadísticas después del login
    profile.refresh_from_db()
    logs_after = LoginLog.objects.filter(user=user).count()
    
    print(f"\n📊 Después del login:")
    print(f"   Logins: {profile.login_count}")
    print(f"   Logs: {logs_after}")
    print(f"   IP registrada: {profile.last_login_ip}")
    
    # Mostrar último log
    last_log = LoginLog.objects.filter(user=user).first()
    if last_log:
        status = "✅ Exitoso" if last_log.success else "❌ Fallido"
        print(f"\n📝 Último log:")
        print(f"   Tiempo: {last_log.login_time.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"   IP: {last_log.ip_address}")
        print(f"   Estado: {status}")
    
    print(f"\n🎯 El sistema {'✅ FUNCIONA' if logs_after > logs_before else '❌ NO REGISTRÓ'} correctamente!")

if __name__ == "__main__":
    real_login_test()
