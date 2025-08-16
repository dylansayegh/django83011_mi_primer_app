pip install django
# django83011_mi_primer_app

Proyecto web en Django: blog y tienda de camisetas retro

## Descripción
Aplicación web desarrollada en Django 5.x con:
- Herencia de plantillas y navegación moderna
- CRUD de páginas/blog (app `pages`) con vistas basadas en clase (CBV)
- Tienda de camisetas retro (app `mi_primer_app`)
- Registro, login, logout y perfil de usuario (app `accounts`)
- Página "Acerca de mí" y perfil personalizado
- Integración de avatar generado por IA
- Búsqueda y filtrado de camisetas

## Instalación y ejecución

   cd mi_primer_app
   ```
2. Instala dependencias:
   ```
   pip install -r requirements.txt
   ```
3. Realiza migraciones:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
4. Ejecuta el servidor:
   ```
   python manage.py runserver
   ```
5. Accede a la web en: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades principales
- Home, About, perfil, login, registro, logout
- CRUD de páginas/blog (crear, ver, editar, borrar)
- Tienda de camisetas retro y compras
- Historial de compras y búsqueda de camisetas
- Avatar personalizado en perfil
- Navegación clara y diseño responsive

## Estructura de carpetas relevante
- `mi_primer_app/`: tienda y vistas principales
- `pages/`: blog y páginas con CBV
- `accounts/`: autenticación y perfil
- `static/avatar/`: imagen de avatar personalizada

## Notas
- No subas `db.sqlite3` ni la carpeta `media/` al repo (ya está en `.gitignore`)
- Si agregas imágenes, colócalas en `static/`
- Puedes personalizar el perfil y la página About a tu gusto

## Video
Agrega aquí el link a tu video de presentación

---
¡Listo para entregar y subir a GitHub!