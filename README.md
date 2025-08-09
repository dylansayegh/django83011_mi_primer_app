# Mi tienda de camisetas retro - Proyecto Django

## Descripción
Este proyecto es una web de ejemplo desarrollada en Django, con herencia de plantillas, múltiples modelos y formularios para gestión de camisetas de fútbol retro, familiares y clientes. Incluye autenticación de usuarios, historial de compras y búsqueda en la base de datos.

## Requisitos
- Python 3.10+
- Django 5.x

## Instalación y ejecución
1. Clona el repositorio:
   ```
   git clone <URL_DE_TU_REPO>
   cd mi_primer_app
   ```
2. Instala dependencias y crea la base de datos:
   ```
   pip install django
   python manage.py makemigrations
   python manage.py migrate
   ```
3. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```
4. Accede a la web en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades principales
- **Herencia de plantillas:** Todas las páginas extienden de `padre.html`.
- **Modelos:**
  - `Camiseta`: camisetas de fútbol retro.
  - `Familiar`: familiares del usuario.
  - `Compra`: historial de compras de camisetas.
  - (Extras: Curso, Estudiante, Auto)
- **Formularios:**
  - Agregar familiar: `/crear-familiar/`
  - Agregar cliente: `/agregar-cliente/`
  - Registrar usuario: `/registro/`
  - Comprar camiseta: `/camisetas/` → botón "Comprar"
- **Búsqueda:**
  - Buscar camisetas por equipo: `/buscar-camisetas/`
- **Autenticación:**
  - Registro, login, logout, historial de compras (`/mis-compras/`)

## Orden sugerido para probar
1. Regístrate como usuario nuevo (`/registro/`).
2. Inicia sesión (`/login/`).
3. Agrega familiares y clientes.
4. Ve a "Camisetas" y realiza una compra.
5. Consulta tu historial en "Mis compras".
6. Prueba la búsqueda de camisetas por equipo.

## Estructura de carpetas relevante
- `mi_primer_app/models.py`: modelos de la base de datos.
- `mi_primer_app/views.py`: vistas y lógica de la web.
- `mi_primer_app/templates/mi_primer_app/`: plantillas HTML.
- `mi_primer_app/urls.py`: rutas de la aplicación.

## Notas
- Puedes modificar los modelos y vistas para agregar más funcionalidades.
- El menú principal te permite navegar por todas las secciones.

---
¡Listo para entregar y subir a GitHub!
