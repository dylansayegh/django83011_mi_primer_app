# 🚀 DEPLOY A PRODUCCIÓN - CAMISETAS RETRO DS

## 🌐 **Opciones de Deploy Recomendadas:**

### 1️⃣ **Railway (Recomendado - Fácil y Gratis)**
```bash
# Instalar Railway CLI
npm install -g @railway/cli

# Login y deploy
railway login
railway init
railway up
```

### 2️⃣ **Heroku (Clásico)**
```bash
# Crear Procfile
echo "web: gunicorn mi_primer_proyecto.wsgi" > Procfile

# Deploy
heroku create camisetas-retro-ds
heroku config:set SECRET_KEY=tu-clave-secreta
git push heroku main
```

### 3️⃣ **Render (Moderno)**
- Conectar repo desde GitHub
- Configurar variables de entorno
- Deploy automático

---

## ⚙️ **CONFIGURACIÓN PARA PRODUCCIÓN:**

### 📁 **Archivos necesarios:**

#### **Procfile** (para Heroku)
```
web: gunicorn mi_primer_proyecto.wsgi --log-file -
```

#### **runtime.txt** (especificar Python version)
```
python-3.10.12
```

#### **settings_prod.py** (configuraciones de producción)
```python
from .settings import *
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='').split(',')

# Base de datos para producción
if 'DATABASE_URL' in os.environ:
    import dj_database_url
    DATABASES['default'] = dj_database_url.parse(os.environ.get('DATABASE_URL'))

# Archivos estáticos
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
```

---

## 🔐 **VARIABLES DE ENTORNO PARA PRODUCCIÓN:**

```bash
# Obligatorias
SECRET_KEY=clave-super-secreta-para-produccion
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com,www.tu-dominio.com

# Opcionales
DATABASE_URL=postgres://...
EMAIL_HOST=smtp.gmail.com
EMAIL_HOST_USER=contacto@camisetasretro.com
```

---

## ✅ **CHECKLIST PRE-DEPLOY:**

### 🔍 **Seguridad:**
- [ ] SECRET_KEY en variable de entorno
- [ ] DEBUG=False
- [ ] ALLOWED_HOSTS configurado
- [ ] .env en .gitignore

### 📦 **Dependencias:**
- [ ] requirements.txt actualizado
- [ ] gunicorn agregado
- [ ] whitenoise para archivos estáticos
- [ ] dj-database-url para PostgreSQL

### 🗄️ **Base de Datos:**
- [ ] Migraciones aplicadas
- [ ] Datos de prueba creados
- [ ] Superusuario creado

### 🎨 **Frontend:**
- [ ] Archivos estáticos recolectados
- [ ] CDNs funcionando
- [ ] Responsive testing

---

## 📊 **POST-DEPLOY TESTING:**

### ✅ **Funcionalidades a probar:**
1. ✅ Página principal carga correctamente
2. ✅ Registro de usuarios funciona
3. ✅ Login/logout operativo
4. ✅ Catálogo de camisetas visible
5. ✅ Carrito agrega productos
6. ✅ Proceso de checkout completo
7. ✅ Panel admin accesible
8. ✅ Responsive en móviles

### 🚨 **Monitoreo:**
- Logs de errores
- Performance de carga
- Uptime del servidor
- Métricas de usuarios

---

## 🔧 **COMANDOS DE MANTENIMIENTO:**

```bash
# Aplicar migraciones
python manage.py migrate

# Recolectar archivos estáticos
python manage.py collectstatic --noinput

# Crear superusuario
python manage.py createsuperuser

# Poblar base de datos
python manage.py loaddata fixtures/camisetas.json
```

---

## 🎯 **PRÓXIMOS PASOS:**

### 📈 **Mejoras futuras:**
1. **SSL Certificate** - HTTPS obligatorio
2. **CDN** - Para imágenes y archivos estáticos
3. **Redis Cache** - Para mejor performance
4. **Monitoring** - Sentry para errores
5. **Backup** - Base de datos automático
6. **Analytics** - Google Analytics
7. **SEO** - Meta tags y sitemap

### 💡 **Features adicionales:**
- Sistema de reviews
- Wishlist de productos
- Notificaciones push
- Integración con pasarelas de pago
- Multi-idioma
- Sistema de descuentos avanzado
