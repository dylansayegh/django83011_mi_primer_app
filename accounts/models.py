from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    
    # Campos adicionales para tracking de login
    last_login_ip = models.GenericIPAddressField(null=True, blank=True)
    login_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class LoginLog(models.Model):
    """Modelo para registrar cada login de usuario"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='login_logs')
    login_time = models.DateTimeField(default=timezone.now)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(blank=True)
    success = models.BooleanField(default=True)
    session_key = models.CharField(max_length=40, blank=True)
    
    class Meta:
        ordering = ['-login_time']
        verbose_name = 'Log de Login'
        verbose_name_plural = 'Logs de Login'
    
    def __str__(self):
        return f"{self.user.username} - {self.login_time.strftime('%d/%m/%Y %H:%M')}"
