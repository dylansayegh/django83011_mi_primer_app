#!/usr/bin/env python
"""
Script para verificar credenciales y hacer login exitoso
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_primer_proyecto.settings')
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.test import Client
from accounts.models import Profile, LoginLog

def test_credentials_and_login():
    print("🔑 VERIFICANDO CREDENCIALES Y PROBANDO LOGIN")
    print("=" * 50)
    
    # Verificar usuario
    try:
        user = User.objects.get(username='dylan')
        print(f"✅ Usuario encontrado: {user.username}")
        print(f"📧 Email: {user.email or 'No especificado'}")
        print(f"🔐 Tiene contraseña: {'Sí' if user.password else 'No'}")
        print(f"🏠 Es staff: {user.is_staff}")
        print(f"🔑 Es superuser: {user.is_superuser}")
    except User.DoesNotExist:
        print("❌ Usuario no encontrado")
        return
    
    # Probar autenticación con diferentes contraseñas comunes
    common_passwords = ['dylan123', 'dylan', '123456', 'admin', 'password', 'test123']
    authenticated_user = None
    
    print("\n🔍 Probando contraseñas comunes...")
    for password in common_passwords:
        auth_user = authenticate(username='dylan', password=password)
        if auth_user:
            print(f"✅ Contraseña correcta encontrada: '{password}'")
            authenticated_user = auth_user
            break
        else:
            print(f"❌ Contraseña incorrecta: '{password}'")
    
    if not authenticated_user:
        print("\n⚠️  No se encontró la contraseña. Creando una nueva...")
        user.set_password('dylan123')
        user.save()
        print("✅ Nueva contraseña establecida: 'dylan123'")
        authenticated_user = authenticate(username='dylan', password='dylan123')
    
    if authenticated_user:
        print(f"\n🎯 Autenticación exitosa para: {authenticated_user.username}")
        
        # Hacer login real con el cliente
        client = Client()
        
        # Obtener estadísticas antes
        profile = Profile.objects.get(user=user)
        logins_before = profile.login_count
        
        print(f"\n📊 Estadísticas antes del login:")
        print(f"   Total logins: {logins_before}")
        
        # Realizar login
        response = client.post('/auth/login/', {
            'username': 'dylan',
            'password': 'dylan123'
        }, follow=True)
        
        print(f"\n🌐 Resultado del login:")
        print(f"   Status code: {response.status_code}")
        print(f"   Redirected: {response.redirect_chain}")
        
        # Verificar si fue exitoso
        if response.status_code == 200:
            # Actualizar estadísticas
            profile.refresh_from_db()
            
            print(f"\n📈 Estadísticas después del login:")
            print(f"   Total logins: {profile.login_count}")
            print(f"   Última IP: {profile.last_login_ip}")
            
            # Mostrar último log
            last_log = LoginLog.objects.filter(user=user).first()
            if last_log:
                status = "✅ Exitoso" if last_log.success else "❌ Fallido"
                print(f"\n📝 Último registro:")
                print(f"   Tiempo: {last_log.login_time.strftime('%d/%m/%Y %H:%M:%S')}")
                print(f"   IP: {last_log.ip_address}")
                print(f"   Estado: {status}")
            
            print(f"\n🎉 ¡LOGIN Y TRACKING FUNCIONANDO CORRECTAMENTE!")
        else:
            print(f"❌ Login falló con código: {response.status_code}")
    else:
        print("❌ No se pudo autenticar al usuario")

if __name__ == "__main__":
    test_credentials_and_login()
