# 🚀 Práctica Clase 10: Sistema CRUD Completo para una Clínica Veterinaria Ficticia

## Contexto del Proyecto

> "El 73% de las empresas pequeñas aún gestionan datos de clientes en hojas de cálculo, lo que causa pérdidas de información y errores humanos frecuentes."
> — _Fuente: McKinsey Digital, Small Business Technology Report (2024)_

La **Clínica Veterinaria "PatasFelices"** (empresa ficticia) necesita digitalizar urgentemente su sistema de gestión. Actualmente llevan todo en cuadernos y planillas Excel: datos de dueños, mascotas, y consultas médicas. Pierden fichas, duplican información y no pueden buscar historiales.

Tu misión: construir desde cero una aplicación Django funcional que les permita gestionar estos datos con operaciones CRUD completas, accesibles desde el navegador.

---

## Objetivos de la Práctica

- [ ] Crear un proyecto Django completo desde cero con múltiples modelos relacionados.
- [ ] Separar la configuración en `base.py`, `development.py` y `production.py`.
- [ ] Configurar variables de entorno con `.env` para proteger datos sensibles.
- [ ] Conectar SQLite en desarrollo y Supabase (PostgreSQL) en producción.
- [ ] Implementar vistas basadas en clases para todas las operaciones CRUD.
- [ ] Crear templates HTML funcionales con formularios protegidos por CSRF.
- [ ] Configurar el enrutamiento completo de la aplicación.
- [ ] Registrar modelos en el admin con personalización básica.
- [ ] Verificar el flujo completo: crear, listar, editar y eliminar registros desde el navegador.

---

## 📁 Fase 1: Cimientos del Proyecto

> "La arquitectura de software es como los cimientos de un edificio: invisible para el usuario, pero si está mal hecha, todo lo que construyas encima se derrumba."
> — _Fuente: Robert C. Martin, Clean Architecture (2017)_

### Instrucciones:

1. Crea un proyecto Django llamado `veterinaria_patasfelices`.
2. Crea una aplicación llamada `fichas`.
3. Registra la app en `INSTALLED_APPS`.
4. Crea la carpeta `templates/fichas/` y configura `DIRS` en `settings.py`.
5. Ejecuta el servidor y verifica que el cohete de Django aparezca.

### Estructura esperada al terminar esta fase:

```
veterinaria_patasfelices/
├── manage.py
├── veterinaria_patasfelices/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── fichas/
│   ├── models.py
│   ├── views.py
│   ├── admin.py
│   └── ...
└── templates/
    └── fichas/
```

---

## ⚙️ Fase 2: Separación de Settings y Variables de Entorno

> "El 45% de las brechas de seguridad en aplicaciones web se deben a configuraciones incorrectas o credenciales expuestas en el código fuente."
> — _Fuente: OWASP Top 10 Report (2024)_

En un proyecto profesional **nunca** se usa el mismo `settings.py` para desarrollo y producción. Vamos a dividir la configuración en tres archivos y proteger los datos sensibles con variables de entorno.

### Paso 1: Instalar dependencias

```bash
pip install python-dotenv dj-database-url psycopg2-binary
```

| Paquete              | ¿Para qué sirve?                                              |
| :------------------- | :------------------------------------------------------------ |
| `python-dotenv`      | Cargar variables de entorno desde un archivo `.env`           |
| `dj-database-url`    | Convertir una URL de base de datos en la configuración Django |
| `psycopg2-binary`    | Driver para conectar Python con PostgreSQL (Supabase)         |

### Paso 2: Crear la carpeta `settings/`

Dentro de tu carpeta de configuración (`veterinaria_patasfelices/`), transforma el archivo `settings.py` en una carpeta:

```bash
# Desde la raíz del proyecto:
mkdir veterinaria_patasfelices/settings
mv veterinaria_patasfelices/settings.py veterinaria_patasfelices/settings/base.py
touch veterinaria_patasfelices/settings/__init__.py
touch veterinaria_patasfelices/settings/development.py
touch veterinaria_patasfelices/settings/production.py
```

### Estructura resultante:

```
veterinaria_patasfelices/
├── settings/                  ← Ahora es una CARPETA
│   ├── __init__.py            ← Elige qué entorno cargar
│   ├── base.py                ← Configuración COMÚN
│   ├── development.py         ← Solo desarrollo (SQLite)
│   └── production.py          ← Solo producción (Supabase)
├── urls.py
├── wsgi.py
└── asgi.py
```

### Paso 3: Crear el archivo `.env`

En la **raíz del proyecto** (donde está `manage.py`), crea un archivo `.env`:

```env
# .env — Variables de entorno (NO subir a Git)
DJANGO_ENV=development
SECRET_KEY=tu-clave-secreta-aqui-genera-una-nueva
DEBUG=True
DATABASE_URL=postgres://tu_usuario:tu_password@tu_host:5432/postgres
```

Y un `.env.example` (este SÍ va a Git, como referencia para otros desarrolladores):

```env
# .env.example — Plantilla de variables de entorno
DJANGO_ENV=development
SECRET_KEY=genera-tu-propia-clave
DEBUG=True
DATABASE_URL=postgres://usuario:password@host:5432/basededatos
```

> ⚠️ **Agrega `.env` a tu `.gitignore`** para que nunca se suba al repositorio.

### Paso 4: Configurar `__init__.py`

```python
# veterinaria_patasfelices/settings/__init__.py

import os
from dotenv import load_dotenv

load_dotenv()  # Carga las variables del archivo .env

env = os.getenv('DJANGO_ENV', 'development')

if env == 'production':
    from .production import *
else:
    from .development import *
```

### Paso 5: Limpiar `base.py`

En `base.py` (tu antiguo `settings.py`), haz estos cambios:

1. **Quita** la línea de `SECRET_KEY` hardcodeada y reemplázala:

```python
import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'clave-insegura-solo-desarrollo')
```

2. **Quita** la línea `DEBUG = True` (cada entorno la define).
3. **Quita** el bloque `DATABASES` completo (cada entorno lo define).
4. **Deja todo lo demás**: `INSTALLED_APPS`, `MIDDLEWARE`, `TEMPLATES`, `AUTH_PASSWORD_VALIDATORS`, etc.

### Paso 6: Configurar `development.py` (SQLite)

```python
# veterinaria_patasfelices/settings/development.py

from .base import *

DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Base de datos local — SQLite para desarrollo
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

### Paso 7: Configurar `production.py` (Supabase PostgreSQL)

```python
# veterinaria_patasfelices/settings/production.py

import os
import dj_database_url
from .base import *

DEBUG = False

ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', 'localhost').split(',')

# Base de datos en la nube — Supabase (PostgreSQL)
DATABASES = {
    'default': dj_database_url.config(
        default=os.getenv('DATABASE_URL'),
        conn_max_age=600,
        ssl_require=True,
    )
}
```

### Paso 8: Crear proyecto en Supabase

1. Entra a [https://supabase.com/](https://supabase.com/) y crea una cuenta gratuita.
2. Crea un nuevo proyecto.
3. Ve a **Project Settings → Database** y copia la **Connection String (URI)**.
4. Pégala en tu archivo `.env` como valor de `DATABASE_URL`.

### Paso 9: Verificar ambos entornos

**Verificar desarrollo (SQLite):**

```bash
# Asegúrate de que .env tiene DJANGO_ENV=development
python manage.py runserver
# Si funciona → ✅ desarrollo con SQLite OK
```

**Verificar producción (Supabase):**

```bash
# Cambia en .env: DJANGO_ENV=production
python manage.py migrate
# Si las migraciones se aplican en Supabase → ✅ producción OK
# Vuelve a cambiar a DJANGO_ENV=development para seguir trabajando
```

### Checklist de esta fase:

- [ ] Carpeta `settings/` creada con `__init__.py`, `base.py`, `development.py`, `production.py`.
- [ ] Archivo `.env` creado con `DJANGO_ENV`, `SECRET_KEY`, `DEBUG`, `DATABASE_URL`.
- [ ] Archivo `.env.example` creado (sin datos reales).
- [ ] `.env` agregado al `.gitignore`.
- [ ] `python manage.py runserver` funciona en modo `development` (SQLite).
- [ ] Migraciones se aplican correctamente en Supabase al cambiar a `production`.

---

## 📋 Fase 3: Modelado de Datos (Tres Modelos Relacionados)

> "Un modelo de datos bien diseñado es la inversión más rentable en un proyecto de software: reduce bugs, simplifica consultas y acelera el desarrollo futuro."
> — _Fuente: Martin Fowler, Patterns of Enterprise Application Architecture (2003)_

La clínica necesita registrar tres tipos de información relacionados entre sí:

### Modelo 1: `Dueno` (Dueño de la mascota)

| Campo       | Tipo             | Restricciones                          |
| :---------- | :--------------- | :------------------------------------- |
| `nombre`    | `CharField`      | `max_length=100`                       |
| `rut`       | `CharField`      | `max_length=12`, `unique=True`         |
| `telefono`  | `CharField`      | `max_length=20`                        |
| `email`     | `EmailField`     | `blank=True`                           |
| `direccion` | `TextField`      | `blank=True`                           |

### Modelo 2: `Mascota`

| Campo              | Tipo              | Restricciones                                  |
| :----------------- | :---------------- | :--------------------------------------------- |
| `nombre`           | `CharField`       | `max_length=80`                                |
| `especie`          | `CharField`       | `max_length=50` (ej: "Perro", "Gato", "Ave")  |
| `raza`             | `CharField`       | `max_length=80`, `blank=True`                  |
| `fecha_nacimiento` | `DateField`       | `null=True`, `blank=True`                      |
| `dueno`            | `ForeignKey`      | Relación con `Dueno`, `on_delete=CASCADE`      |

### Modelo 3: `ConsultaMedica`

| Campo          | Tipo              | Restricciones                                         |
| :------------- | :---------------- | :---------------------------------------------------- |
| `mascota`      | `ForeignKey`      | Relación con `Mascota`, `on_delete=CASCADE`           |
| `fecha`        | `DateTimeField`   | `auto_now_add=True`                                   |
| `motivo`       | `CharField`       | `max_length=200`                                      |
| `diagnostico`  | `TextField`       |                                                       |
| `tratamiento`  | `TextField`       | `blank=True`                                          |
| `costo`        | `DecimalField`    | `max_digits=10`, `decimal_places=2`, `default=0`      |

### Diagrama de relaciones:

```
Dueno ──── 1:N ────► Mascota ──── 1:N ────► ConsultaMedica
 │                     │                       │
 Un dueño tiene        Una mascota tiene       Cada consulta
 muchas mascotas       muchas consultas         pertenece a
                                                una mascota
```

### Tareas:

1. Define los tres modelos en `fichas/models.py`.
2. Agrega `__str__` a cada modelo para que sean legibles en el admin.
3. Agrega `class Meta` con `ordering` y `verbose_name` a cada modelo.
4. Ejecuta `makemigrations` y `migrate`.
5. Verifica con `showmigrations` que todo esté aplicado.

---

## 🔑 Fase 4: Panel de Administración Personalizado

> "Django admin no es solo una herramienta de desarrollo, es una interfaz de producción que el 42% de las startups usa como backoffice en sus primeras versiones."
> — _Fuente: Django Developers Survey, JetBrains (2024)_

No basta con registrar modelos. Un admin bien configurado hace que los datos sean fáciles de gestionar.

### Instrucciones:

1. Registra los tres modelos en `fichas/admin.py`.
2. Para el modelo `Dueno`, crea un `ModelAdmin` personalizado:

```python
@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'telefono', 'email')
    search_fields = ('nombre', 'rut')
```

3. Para `Mascota`, muestra `nombre`, `especie`, `raza` y el nombre del dueño en la lista.
4. Para `ConsultaMedica`, muestra `mascota`, `motivo`, `fecha` y `costo`.
5. Crea un **superusuario** y verifica desde `/admin/` que puedes:
   - Crear al menos 2 dueños.
   - Crear al menos 3 mascotas (asociadas a los dueños).
   - Crear al menos 2 consultas médicas (asociadas a las mascotas).

---

## 🖥️ Fase 5: Vistas CRUD con Class-Based Views

> "Las vistas genéricas de Django reducen entre un 60% y un 80% el código necesario para operaciones CRUD estándar."
> — _Fuente: Two Scoops of Django, D. Feldroy & A. Feldroy (2024)_

Ahora vamos a crear las vistas para que el CRUD funcione desde el navegador, no solo desde el admin.

### Instrucciones:

Crea en `fichas/views.py` las siguientes vistas:

#### Para Dueños (5 vistas):

| Vista               | Clase Base     | Template esperado                 |
| :------------------ | :------------- | :-------------------------------- |
| `DuenoListView`     | `ListView`     | `fichas/dueno_list.html`          |
| `DuenoDetailView`   | `DetailView`   | `fichas/dueno_detail.html`        |
| `DuenoCreateView`   | `CreateView`   | `fichas/dueno_form.html`          |
| `DuenoUpdateView`   | `UpdateView`   | `fichas/dueno_form.html`          |
| `DuenoDeleteView`   | `DeleteView`   | `fichas/dueno_confirm_delete.html`|

#### Para Mascotas (5 vistas):

| Vista                 | Clase Base     | Template esperado                   |
| :-------------------- | :------------- | :---------------------------------- |
| `MascotaListView`     | `ListView`     | `fichas/mascota_list.html`          |
| `MascotaDetailView`   | `DetailView`   | `fichas/mascota_detail.html`        |
| `MascotaCreateView`   | `CreateView`   | `fichas/mascota_form.html`          |
| `MascotaUpdateView`   | `UpdateView`   | `fichas/mascota_form.html`          |
| `MascotaDeleteView`   | `DeleteView`   | `fichas/mascota_confirm_delete.html`|

### Tips:

- Usa `reverse_lazy('fichas:dueno_lista')` como `success_url`.
- En `fields`, incluye todos los campos editables (no `fecha_registro` ni `auto_now_add`).
- Para `MascotaCreateView` incluye el campo `dueno` en `fields` para que el usuario pueda seleccionar el dueño desde un dropdown.

---

## 🔗 Fase 6: Enrutamiento Completo

> "Una aplicación web sin rutas claras es como una ciudad sin señalética: los usuarios se pierden y abandonan."
> — _Fuente: Steve Krug, Don't Make Me Think (2014)_

### Instrucciones:

1. Crea el archivo `fichas/urls.py` con las rutas para dueños y mascotas:

```python
from django.urls import path
from . import views

app_name = 'fichas'

urlpatterns = [
    # Dueños
    path('duenos/', views.DuenoListView.as_view(), name='dueno_lista'),
    path('duenos/<int:pk>/', views.DuenoDetailView.as_view(), name='dueno_detalle'),
    path('duenos/nuevo/', views.DuenoCreateView.as_view(), name='dueno_crear'),
    path('duenos/editar/<int:pk>/', views.DuenoUpdateView.as_view(), name='dueno_editar'),
    path('duenos/eliminar/<int:pk>/', views.DuenoDeleteView.as_view(), name='dueno_eliminar'),

    # Mascotas
    path('mascotas/', views.MascotaListView.as_view(), name='mascota_lista'),
    path('mascotas/<int:pk>/', views.MascotaDetailView.as_view(), name='mascota_detalle'),
    path('mascotas/nuevo/', views.MascotaCreateView.as_view(), name='mascota_crear'),
    path('mascotas/editar/<int:pk>/', views.MascotaUpdateView.as_view(), name='mascota_editar'),
    path('mascotas/eliminar/<int:pk>/', views.MascotaDeleteView.as_view(), name='mascota_eliminar'),
]
```

2. En el `urls.py` del proyecto, incluye las rutas de la app:

```python
path('', include('fichas.urls')),
```

---

## 🎨 Fase 7: Templates HTML con Formularios CSRF

> "El 85% de las vulnerabilidades web podrían evitarse implementando correctamente tokens CSRF y validación del lado del servidor."
> — _Fuente: OWASP, Web Application Security Testing Guide (2024)_

Crea los templates necesarios. Todos deben incluir `{% csrf_token %}` en los formularios.

### Template base (`templates/fichas/base.html`):

Crea un template base sencillo que todos los demás extiendan:

```html
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %}PatasFelices{% endblock %}</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 900px; margin: 0 auto; padding: 20px; }
        nav { background: #2c3e50; padding: 15px; margin-bottom: 20px; border-radius: 8px; }
        nav a { color: white; margin-right: 20px; text-decoration: none; }
        nav a:hover { text-decoration: underline; }
        table { width: 100%; border-collapse: collapse; margin: 20px 0; }
        th, td { border: 1px solid #ddd; padding: 10px; text-align: left; }
        th { background: #34495e; color: white; }
        tr:nth-child(even) { background: #f9f9f9; }
        .btn { padding: 8px 16px; border: none; border-radius: 4px; cursor: pointer;
               text-decoration: none; color: white; margin: 2px; display: inline-block; }
        .btn-primary { background: #3498db; }
        .btn-success { background: #27ae60; }
        .btn-danger { background: #e74c3c; }
        .btn-warning { background: #f39c12; }
        form p { margin: 10px 0; }
        input, select, textarea { width: 100%; padding: 8px; margin-top: 4px;
                                   box-sizing: border-box; border: 1px solid #ccc;
                                   border-radius: 4px; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <nav>
        <a href="{% url 'fichas:dueno_lista' %}">🏠 Dueños</a>
        <a href="{% url 'fichas:mascota_lista' %}">🐾 Mascotas</a>
        <a href="{% url 'fichas:dueno_crear' %}">➕ Nuevo Dueño</a>
        <a href="{% url 'fichas:mascota_crear' %}">➕ Nueva Mascota</a>
    </nav>

    {% block content %}{% endblock %}
</body>
</html>
```

### Templates a crear:

Ahora crea cada template. Todos deben extender de `base.html`:

#### 1. `dueno_list.html` — Lista de dueños

- Extiende de `base.html`.
- Muestra una tabla con columnas: Nombre, RUT, Teléfono, Email, Acciones.
- En "Acciones", agrega links de Ver, Editar y Eliminar usando `{% url %}`.
- Si no hay dueños, muestra un mensaje: "No hay dueños registrados aún."

#### 2. `dueno_detail.html` — Detalle de un dueño

- Muestra todos los datos del dueño.
- **Desafío:** Debajo de los datos del dueño, muestra una lista con las mascotas del dueño (`dueno.mascota_set.all`).
- Agrega botones para Editar y Eliminar el dueño.
- Agrega un link "Registrar mascota" para este dueño.

#### 3. `dueno_form.html` — Formulario para crear/editar dueño

- Usa `{{ form.as_p }}` para renderizar el formulario.
- Incluye `{% csrf_token %}`.
- Agrega un botón de "Guardar".
- Agrega un link "Cancelar" que vuelva a la lista.

#### 4. `dueno_confirm_delete.html` — Confirmación de eliminación

- Muestra un mensaje: "¿Estás seguro de que deseas eliminar al dueño **{{ object.nombre }}**?"
- Muestra un formulario con `{% csrf_token %}` y un botón "Confirmar eliminación".
- Agrega un link "Cancelar" que vuelva a la lista.

#### 5. Repite los templates para Mascotas:

- `mascota_list.html` — Tabla con: Nombre, Especie, Raza, Dueño, Acciones.
- `mascota_detail.html` — Datos de la mascota + lista de consultas médicas.
- `mascota_form.html` — Formulario con CSRF.
- `mascota_confirm_delete.html` — Confirmación de eliminación.

---

## ✅ Fase 8: Verificación Completa

> "Un software no probado es un software que no funciona — solo que aún no lo sabes."
> — _Fuente: Kent Beck, Test-Driven Development (2003)_

Ejecuta el servidor y verifica **cada uno** de los siguientes flujos:

### Checklist de verificación:

#### Dueños:
- [ ] Acceder a `/duenos/` muestra la lista (vacía o con datos).
- [ ] Hacer clic en "Nuevo Dueño" abre un formulario limpio.
- [ ] Llenar y enviar el formulario crea un dueño y redirige a la lista.
- [ ] Hacer clic en "Ver" abre el detalle del dueño con sus mascotas.
- [ ] Hacer clic en "Editar" abre el formulario con los datos cargados.
- [ ] Modificar un campo y guardar actualiza el registro.
- [ ] Hacer clic en "Eliminar" muestra la confirmación.
- [ ] Confirmar la eliminación borra el dueño y redirige a la lista.

#### Mascotas:
- [ ] Acceder a `/mascotas/` muestra la lista con el nombre del dueño.
- [ ] Crear una mascota permite seleccionar el dueño desde un dropdown.
- [ ] El detalle de la mascota muestra sus consultas médicas.
- [ ] Editar y eliminar funcionan correctamente.

#### Seguridad:
- [ ] Todos los formularios POST tienen `{% csrf_token %}`.
- [ ] Si quito el `{% csrf_token %}` del template y envío el formulario, Django devuelve error 403.

---

## 🌟 Bonus (Para quienes terminen antes)

> "La diferencia entre un desarrollador junior y uno senior no es que el senior sepa más, sino que el senior anticipa los problemas antes de que aparezcan."
> — _Fuente: The Pragmatic Programmer, Hunt & Thomas (2019)_

Si terminaste todo lo anterior, intenta estos desafíos adicionales:

### Bonus 1: CRUD de Consultas Médicas
Agrega las 5 vistas CRUD para `ConsultaMedica`:
- El formulario debe permitir seleccionar la mascota.
- La lista debe mostrar: mascota, motivo, fecha y costo.
- En el detalle de una mascota, agrega un link "Nueva consulta" que pase la mascota preseleccionada.

### Bonus 2: Agregar un template `inicio.html`
Crea una página de inicio (`/`) que muestre:
- Total de dueños registrados.
- Total de mascotas registradas.
- Total de consultas realizadas.
- Links rápidos para crear dueño, mascota y consulta.

> **Tip:** Usa una vista basada en función con `Cliente.objects.count()` y pasa los totales al template con el `context`.

### Bonus 3: Mensajes de éxito
Usa `django.contrib.messages` para mostrar un mensaje de éxito después de crear, editar o eliminar un registro. Investiga cómo sobreescribir el método `form_valid()` en las CBV para agregar el mensaje.

---

## 📝 Resumen del Entregable

| #   | Requisito                                                                          | Estado |
| :-- | :--------------------------------------------------------------------------------- | :----- |
| 1   | Proyecto `veterinaria_patasfelices` creado y servidor funcional                    | [ ]    |
| 2   | App `fichas` registrada en `INSTALLED_APPS`                                        | [ ]    |
| 3   | Settings separados en `base.py`, `development.py` y `production.py`                | [ ]    |
| 4   | `.env` con variables de entorno + `.env.example` + `.gitignore` actualizado        | [ ]    |
| 5   | Desarrollo con SQLite y producción con Supabase (PostgreSQL) verificados           | [ ]    |
| 6   | 3 modelos definidos con `__str__`, `Meta` y relaciones FK                          | [ ]    |
| 7   | Migraciones generadas y aplicadas                                                  | [ ]    |
| 8   | 3 modelos registrados en admin con `list_display` y `search_fields`                | [ ]    |
| 9   | 10 vistas CBV creadas (5 para Dueño + 5 para Mascota)                              | [ ]    |
| 10  | `urls.py` de la app con 10 rutas + incluido en el `urls.py` del proyecto           | [ ]    |
| 11  | 8 templates HTML creados (4 por modelo) + template base                            | [ ]    |
| 12  | Todos los formularios protegidos con `{% csrf_token %}`                            | [ ]    |
| 13  | Flujo CRUD completo verificado para Dueños y Mascotas desde el navegador           | [ ]    |

---

> [!IMPORTANT]
> **Para la próxima clase:** Necesitarás este proyecto funcionando. En la Clase 11 extenderemos la aplicación con funcionalidades más avanzadas del CRUD.
