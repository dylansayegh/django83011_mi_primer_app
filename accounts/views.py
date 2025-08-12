from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib import messages
from .models import Profile

@login_required
def profile(request):
    """Vista del perfil del usuario"""
    profile, created = Profile.objects.get_or_create(user=request.user)
    context = {
        'user': request.user,
        'profile': profile,
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
