from django.contrib import admin
from .models import Profile, LoginLog

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'location', 'last_login_ip', 'login_count', 'created_at']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['user__username', 'location']
    readonly_fields = ['created_at', 'updated_at', 'login_count']

@admin.register(LoginLog)
class LoginLogAdmin(admin.ModelAdmin):
    list_display = ['user', 'login_time', 'ip_address', 'success']
    list_filter = ['login_time', 'success']
    search_fields = ['user__username', 'ip_address']
    readonly_fields = ['login_time', 'session_key']
    date_hierarchy = 'login_time'
    
    def has_add_permission(self, request):
        return False  # No permitir agregar logs manualmente
