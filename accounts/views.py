from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in
from django.dispatch import receiver
from django.utils import timezone
from functools import wraps
from .models import Profile, LoginLog

def get_client_ip(request):
    """Obtiene la dirección IP del cliente"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

@receiver(user_logged_in)
def log_user_login(sender, request, user, **kwargs):
    """Signal que se ejecuta automáticamente cada vez que un usuario se loguea"""
    try:
        # Actualizar perfil con datos de login
        profile, created = Profile.objects.get_or_create(user=user)
        profile.last_login_ip = get_client_ip(request)
        profile.login_count += 1
        profile.save()
        
        # Crear registro de login
        LoginLog.objects.create(
            user=user,
            ip_address=get_client_ip(request),
            user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
            session_key=request.session.session_key or '',
            success=True
        )
        
        print(f"✅ Login registrado: {user.username} desde IP {profile.last_login_ip}")
        
    except Exception as e:
        print(f"❌ Error guardando datos de login: {e}")
        # Crear log de error
        try:
            LoginLog.objects.create(
                user=user,
                ip_address=get_client_ip(request),
                user_agent=request.META.get('HTTP_USER_AGENT', '')[:500],
                success=False
            )
        except:
            pass

def custom_decorator(func):
    """Decorador personalizado que añade contexto extra"""
    @wraps(func)
    def wrapper(request, *args, **kwargs):
        # Añadir contexto personalizado
        request.custom_context = {'visited_at': 'Django Final Project'}
        return func(request, *args, **kwargs)
    return wrapper

@login_required
def profile(request):
    """Vista del perfil del usuario con estadísticas de login"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    
    # Obtener últimos 5 logins
    recent_logins = LoginLog.objects.filter(
        user=request.user, 
        success=True
    )[:5]
    
    # Estadísticas
    total_logins = profile.login_count
    first_login = LoginLog.objects.filter(user=request.user).last()
    
    context = {
        'user': request.user,
        'profile': profile,
        'recent_logins': recent_logins,
        'total_logins': total_logins,
        'first_login': first_login,
    }
    return render(request, 'accounts/profile.html', context)

def signup(request):
    """Vista para registro de nuevos usuarios"""
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, '¡Cuenta creada exitosamente!')
            return redirect('accounts:profile')
    else:
        form = UserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def custom_logout(request):
    """Vista personalizada para logout con redirección amigable"""
    if request.method == 'POST':
        logout(request)
        return redirect('/auth/login/?logged_out=1')
    else:
        # Si es GET, redirigir al perfil
        return redirect('accounts:profile')

@custom_decorator
def about(request):
    """Vista de información personal del desarrollador"""
    context = {
        'developer_name': 'Dylan Sayegh',
        'project_title': 'Mi Primer Blog Django',
        'description': 'Aplicación web de blog desarrollada con Django 5.2',
        'features': [
            'Sistema de autenticación de usuarios',
            'CRUD completo para páginas/posts',
            'Perfiles de usuario con avatares',
            'Interfaz responsive',
            'Panel de administración',
        ],
        'technologies': ['Django 5.2', 'Python 3.10', 'SQLite', 'HTML5', 'CSS3', 'Bootstrap'],
    }
    return render(request, 'accounts/about.html', context)
