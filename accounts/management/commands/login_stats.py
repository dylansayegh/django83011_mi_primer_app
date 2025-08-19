from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from accounts.models import Profile, LoginLog
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
    help = 'Muestra estadísticas de login de usuarios'

    def add_arguments(self, parser):
        parser.add_argument(
            '--usuario',
            type=str,
            help='Mostrar estadísticas de un usuario específico',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('📊 ESTADÍSTICAS DE LOGIN'))
        self.stdout.write('=' * 50)
        
        if options and options.get('usuario'):
            # Estadísticas de usuario específico
            try:
                user = User.objects.get(username=options['usuario'])
                self.show_user_stats(user)
            except User.DoesNotExist:
                self.stdout.write(
                    self.style.ERROR(f'Usuario "{options["usuario"]}" no encontrado')
                )
        else:
            # Estadísticas generales
            self.show_general_stats()

    def show_user_stats(self, user):
        profile = Profile.objects.filter(user=user).first()
        logs = LoginLog.objects.filter(user=user)
        
        self.stdout.write(f'\n👤 Usuario: {user.username}')
        self.stdout.write(f'📧 Email: {user.email or "No especificado"}')
        self.stdout.write(f'📅 Miembro desde: {user.date_joined.strftime("%d/%m/%Y")}')
        
        if profile:
            self.stdout.write(f'🔄 Total logins: {profile.login_count}')
            self.stdout.write(f'🌐 Última IP: {profile.last_login_ip or "N/A"}')
            self.stdout.write(f'🕐 Último login: {user.last_login.strftime("%d/%m/%Y %H:%M") if user.last_login else "N/A"}')
        
        # Últimos 5 logins
        recent = logs.filter(success=True)[:5]
        if recent:
            self.stdout.write('\n🕒 Últimos 5 logins exitosos:')
            for log in recent:
                self.stdout.write(f'  • {log.login_time.strftime("%d/%m/%Y %H:%M")} desde {log.ip_address or "IP desconocida"}')

    def show_general_stats(self):
        total_users = User.objects.count()
        total_profiles = Profile.objects.count()
        total_logins = LoginLog.objects.filter(success=True).count()
        failed_logins = LoginLog.objects.filter(success=False).count()
        
        # Logins de hoy
        today = timezone.now().date()
        logins_today = LoginLog.objects.filter(
            login_time__date=today,
            success=True
        ).count()
        
        # Logins de esta semana
        week_ago = timezone.now() - timedelta(days=7)
        logins_week = LoginLog.objects.filter(
            login_time__gte=week_ago,
            success=True
        ).count()
        
        self.stdout.write(f'\n👥 Total de usuarios: {total_users}')
        self.stdout.write(f'📋 Perfiles creados: {total_profiles}')
        self.stdout.write(f'✅ Logins exitosos: {total_logins}')
        self.stdout.write(f'❌ Logins fallidos: {failed_logins}')
        self.stdout.write(f'📅 Logins hoy: {logins_today}')
        self.stdout.write(f'📊 Logins esta semana: {logins_week}')
        
        # Usuarios más activos
        active_profiles = Profile.objects.filter(login_count__gt=0).order_by('-login_count')[:5]
        if active_profiles:
            self.stdout.write('\n🏆 Usuarios más activos:')
            for i, profile in enumerate(active_profiles, 1):
                self.stdout.write(f'  {i}. {profile.user.username}: {profile.login_count} logins')
        
        # IPs más frecuentes
        from django.db.models import Count
        frequent_ips = LoginLog.objects.values('ip_address').annotate(
            count=Count('ip_address')
        ).order_by('-count')[:3]
        
        if frequent_ips:
            self.stdout.write('\n🌐 IPs más frecuentes:')
            for ip_data in frequent_ips:
                ip = ip_data['ip_address'] or 'IP desconocida'
                count = ip_data['count']
                self.stdout.write(f'  • {ip}: {count} accesos')
