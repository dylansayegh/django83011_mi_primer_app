# Mi Blog Django - Proyecto Final

## Descripción del Proyecto
Aplicación web de blog desarrollada con Django 5.2 como proyecto final. La aplicación incluye todas las funcionalidades requeridas para una entrega completa y profesional.

## Funcionalidades Implementadas

### ✅ Sistema de Autenticación Completo
- **Login/Logout**: Sistema de autenticación de Django con templates personalizados
- **Registro de usuarios**: Formulario de signup con validación
- **Perfiles de usuario**: Modelo Profile con avatares e información personal
- **Protección de rutas**: LoginRequiredMixin en vistas que lo requieren

### ✅ CRUD Completo con Class Based Views
- **ListView**: Listado de todas las páginas/posts
- **DetailView**: Vista detallada de cada página
- **CreateView**: Crear nuevas páginas (solo usuarios autenticados)
- **UpdateView**: Editar páginas propias
- **DeleteView**: Eliminar páginas propias

### ✅ Estructura de Apps Modular
- **mi_primer_app**: App principal con página de inicio
- **pages**: App de blog para gestión de páginas/posts
- **accounts**: App de gestión de usuarios y perfiles

### ✅ Templates con Herencia
- **Template padre**: Base template con Bootstrap 5 y navegación responsiva
- **Templates específicos**: Para cada funcionalidad (login, signup, profile, etc.)
- **Navegación dinámica**: Cambia según estado de autenticación del usuario

### ✅ Características Adicionales
- **Diseño responsivo**: Bootstrap 5 con iconos FontAwesome
- **Media files**: Configuración para manejo de archivos de usuario (avatares)
- **Admin interface**: Registro de modelos en Django Admin
- **Mensajes del sistema**: Feedback visual para acciones del usuario
- **URLs con namespaces**: Organización clara de rutas

## Estructura del Proyecto

```
mi_primer_app/
├── mi_primer_proyecto/          # Configuración principal
│   ├── settings.py             # Configuración completa
│   ├── urls.py                 # URLs principales
│   └── ...
├── mi_primer_app/              # App principal
│   ├── templates/              # Templates de inicio
│   ├── views.py                # Vistas principales
│   └── urls.py                 # URLs de la app
├── pages/                      # App de blog
│   ├── models.py               # Modelo Page
│   ├── views.py                # CBVs para CRUD
│   ├── templates/              # Templates del blog
│   └── urls.py                 # URLs del blog
├── accounts/                   # App de usuarios
│   ├── models.py               # Modelo Profile
│   ├── views.py                # Vistas de auth
│   ├── templates/              # Templates de auth
│   └── urls.py                 # URLs de usuarios
├── static/                     # Archivos estáticos
├── media/                      # Archivos de usuario
└── requirements.txt            # Dependencias
```

## Tecnologías Utilizadas
- **Backend**: Django 5.2, Python 3.10
- **Base de datos**: SQLite
- **Frontend**: HTML5, CSS3, Bootstrap 5
- **Iconos**: FontAwesome 6
- **Imágenes**: Pillow para manejo de archivos

## URLs Principales
- `/` - Página de inicio
- `/pages/` - Lista de páginas del blog
- `/pages/crear/` - Crear nueva página
- `/accounts/profile/` - Perfil de usuario
- `/accounts/about/` - Información del proyecto
- `/auth/login/` - Iniciar sesión
- `/auth/logout/` - Cerrar sesión
- `/accounts/signup/` - Registro de usuario

## Instalación y Uso

1. **Clonar el repositorio**
2. **Activar entorno virtual**: `venv\Scripts\activate`
3. **Instalar dependencias**: `pip install -r requirements.txt`
4. **Aplicar migraciones**: `python manage.py migrate`
5. **Ejecutar servidor**: `python manage.py runserver`

## Características del Código
- **Código limpio y documentado**
- **Separación de responsabilidades**
- **Reutilización de componentes**
- **Validaciones de seguridad**
- **Estructura escalable**

## Desarrollado por
**Dylan Sayegh** - Proyecto Final Django

---
*Este proyecto demuestra un dominio completo de Django, incluyendo modelos, vistas, templates, autenticación, y mejores prácticas de desarrollo web.*
