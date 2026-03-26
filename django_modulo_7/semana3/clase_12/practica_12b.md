# 🏥 Práctica Final — Módulo 7 · Clase 12

## Optimización de Rendimiento en PatasFelices

---

> _"Un sistema que funciona no es lo mismo que un sistema que funciona bien. Esta clase convierte tu proyecto funcional en un proyecto profesional."_

---

## Contexto

En la **Clase 10** construiste `veterinaria_patasfelices` con CRUD completo, CBV, templates y rutas. En la **Clase 11** personalizaste el admin, agregaste permisos, grupos y protegiste vistas con `PermissionRequiredMixin`.

Hoy es la **clase final** del módulo. Vas a aplicar todas las técnicas de optimización vistas en la teoría directamente sobre tu proyecto de PatasFelices. Al terminar, tendrás un sistema que no solo funciona, sino que **escala**.

---

## ¿Qué vas a hacer?

1. Agregar nuevos modelos para simular un escenario con volumen de datos real.
2. Crear un comando de Django para poblar la base de datos con miles de registros ficticios.
3. Identificar y corregir problemas N+1 en las vistas existentes.
4. Implementar paginación en las listas del CRUD.
5. Agregar índices a los modelos para acelerar filtros y ordenamiento.
6. Crear una vista de estadísticas usando `aggregate()` y `annotate()`.
7. Instalar y usar Django Debug Toolbar para medir el impacto de cada cambio.
8. Optimizar el admin con `select_related` y `prefetch_related`.
9. Documentar cada mejora con mediciones de antes/después.
10. Crear un dashboard de resumen con métricas agregadas.

---

---

# FASE 1 — Preparar el escenario de rendimiento

---

## Paso 1 — Agregar el modelo `Vacuna` y el campo `activo` a Mascota

---

**¿Por qué?** Para simular un escenario real con volumen de datos, necesitamos más modelos y relaciones. Una clínica veterinaria real registra vacunas aplicadas y necesita filtrar mascotas activas e inactivas.

### 1.1 — Agregar campo `activo` a `Mascota`

Abre `fichas/models.py` y agrega un campo booleano al modelo `Mascota`:

| Campo    | Tipo            | Restricciones     |
| :------- | :-------------- | :---------------- |
| `activo` | `BooleanField`  | `default=True`    |

> 💡 Este campo permitirá filtrar mascotas que ya no atiende la clínica, sin borrarlas del sistema.

### 1.2 — Crear el modelo `Vacuna`

Agrega un nuevo modelo `Vacuna` con los siguientes campos:

| Campo              | Tipo            | Restricciones                                    |
| :----------------- | :-------------- | :----------------------------------------------- |
| `mascota`          | `ForeignKey`    | Relación con `Mascota`, `on_delete=CASCADE`      |
| `nombre_vacuna`    | `CharField`     | `max_length=100`                                 |
| `fecha_aplicacion` | `DateField`     |                                                  |
| `proxima_dosis`    | `DateField`     | `null=True`, `blank=True`                        |
| `veterinario`      | `CharField`     | `max_length=100`                                 |
| `lote`             | `CharField`     | `max_length=50`, `blank=True`                    |

No olvides:

1. Agregar `__str__` que devuelva algo como el nombre de la vacuna junto con el nombre de la mascota.
2. Agregar `class Meta` con `ordering = ['-fecha_aplicacion']` y un `verbose_name_plural`.

### 1.3 — Migrar

```bash
python manage.py makemigrations
python manage.py migrate
```

**Verificación:** Ejecuta `python manage.py showmigrations` — la nueva migración debe tener `[X]`.

---

---

# Paso 2 — Registrar `Vacuna` en el admin

---

**¿Por qué?** Necesitas poder ver y gestionar vacunas desde el admin para las pruebas posteriores.

En `fichas/admin.py`:

1. Importa el modelo `Vacuna`.
2. Crea un `VacunaAdmin` con:

| Opción            | Qué poner                                                  |
| :---------------- | :--------------------------------------------------------- |
| `list_display`    | mascota, nombre_vacuna, fecha_aplicacion, proxima_dosis, veterinario |
| `search_fields`   | nombre_vacuna, nombre de la mascota                        |
| `list_filter`     | fecha_aplicacion, nombre_vacuna                            |
| `ordering`        | `-fecha_aplicacion`                                        |

3. Crea un inline `VacunaInline` de tipo `TabularInline` y agrégalo a `MascotaAdmin`, para poder ver las vacunas directamente al editar una mascota.

**Verificación:** Entra al admin → la sección Vacunas aparece con todas las columnas configuradas. Al editar una mascota, se ven las vacunas como inline.

---

---

# FASE 2 — Poblar con datos ficticios masivos

---

## Paso 3 — Crear un Management Command para generar datos

---

**¿Por qué?** No se puede medir rendimiento con 5 registros. Necesitas **miles** para que los problemas sean visibles. Un management command es la forma profesional de hacerlo en Django.

> 📊 **Dato real**: Según el Django Developers Survey de JetBrains (2025), el 67% de los proyectos Django en producción manejan más de 100.000 registros. Las pruebas de rendimiento con datos reales son una de las prácticas más recomendadas por la comunidad.
>
> _Fuente: JetBrains, "Django Developers Survey" (2025)_

### 3.1 — Crear la estructura del comando

Crea la carpeta necesaria:

```bash
mkdir -p fichas/management/commands
touch fichas/management/__init__.py
touch fichas/management/commands/__init__.py
```

### 3.2 — Crear el archivo del comando

Crea el archivo `fichas/management/commands/poblar_datos.py`.

El comando debe:

1. Heredar de `BaseCommand`.
2. Tener un `help` descriptivo.
3. Aceptar un argumento opcional `--cantidad` (por defecto 100 dueños).
4. Generar datos ficticios usando listas de nombres, apellidos, especies, razas, vacunas y motivos de consulta chilenos.
5. Crear registros en este orden: Dueños → Mascotas → Consultas → Vacunas.
6. Usar `bulk_create` para insertar masivamente.
7. Mostrar un resumen al final con la cantidad de registros creados.

### 3.3 — Listas de datos ficticios sugeridas

Aquí tienes listas para generar datos realistas en contexto chileno:

```python
import random
from datetime import date, timedelta
from decimal import Decimal

NOMBRES_PERSONA = [
    'Javiera', 'Catalina', 'Francisca', 'Valentina', 'Constanza',
    'Martín', 'Sebastián', 'Benjamín', 'Matías', 'Nicolás',
    'Camila', 'Fernanda', 'Ignacio', 'Diego', 'Tomás',
    'Antonia', 'Isidora', 'Renato', 'Joaquín', 'Felipe',
]

APELLIDOS = [
    'González', 'Muñoz', 'Rojas', 'Soto', 'Contreras',
    'Silva', 'Araya', 'Díaz', 'Reyes', 'López',
    'Morales', 'Sepúlveda', 'Rodríguez', 'Torres', 'Fuentes',
    'Vargas', 'Castillo', 'Tapia', 'Hernández', 'Flores',
]

NOMBRES_MASCOTA = [
    'Luna', 'Max', 'Coco', 'Pelusa', 'Rocky',
    'Miel', 'Thor', 'Canela', 'Toby', 'Princesa',
    'Simón', 'Nala', 'Zeus', 'Chispita', 'Bruno',
    'Manchas', 'Copito', 'Estrella', 'Rayo', 'Panchita',
]

ESPECIES_RAZAS = {
    'Perro': ['Mestizo', 'Labrador', 'Pastor Alemán', 'Poodle', 'Chihuahua', 'Golden Retriever'],
    'Gato': ['Mestizo', 'Siamés', 'Persa', 'Angora', 'Bengalí'],
    'Ave': ['Periquito', 'Canario', 'Cacatúa', 'Loro'],
    'Conejo': ['Enano', 'Belier', 'Angora', 'Rex'],
}

MOTIVOS_CONSULTA = [
    'Control general', 'Vacunación', 'Problema digestivo',
    'Lesión en pata', 'Control dental', 'Dermatitis',
    'Problema respiratorio', 'Desparasitación', 'Esterilización',
    'Control post-operatorio', 'Fiebre', 'Pérdida de apetito',
    'Picadura de insecto', 'Alergia alimentaria', 'Control de peso',
]

VACUNAS = [
    'Antirrábica', 'Séxtuple', 'Triple Felina', 'Parvovirus',
    'Moquillo', 'Leptospirosis', 'Bordetella', 'Leucemia Felina',
]

VETERINARIOS = [
    'Dra. Marcela Vidal', 'Dr. Andrés Pereira', 'Dra. Carolina Jara',
    'Dr. Roberto Espinoza', 'Dra. Lorena Bravo', 'Dr. Héctor Cárdenas',
]
```

### 3.4 — Lógica de generación

Aquí tienes la estructura que tu comando debe seguir. **No copies este código directamente** — entiende la lógica y escríbelo adaptándolo a tu proyecto:

```
Para cada dueño:
    1. Generar nombre + apellido aleatorio
    2. Generar RUT ficticio (formato XX.XXX.XXX-X)
    3. Generar teléfono ficticio (+569XXXXXXXX)
    4. Generar email basado en el nombre

Para cada dueño, crear entre 1 y 4 mascotas:
    1. Nombre aleatorio de mascota
    2. Especie aleatoria, raza según especie
    3. Fecha de nacimiento aleatoria (últimos 15 años)
    4. 80% activas, 20% inactivas

Para cada mascota, crear entre 0 y 8 consultas:
    1. Motivo aleatorio
    2. Diagnóstico genérico
    3. Costo aleatorio entre $5.000 y $150.000
    4. Fecha aleatoria (últimos 3 años)

Para cada mascota, crear entre 0 y 4 vacunas:
    1. Vacuna aleatoria de la lista
    2. Fecha de aplicación aleatoria
    3. Próxima dosis: fecha + 365 días
    4. Veterinario aleatorio
```

> ⚠️ **Usa `bulk_create()`** para insertar los registros. No uses `.save()` dentro de un loop — eso genera una consulta INSERT por cada registro.

### 3.5 — Ejecutar el comando

```bash
python manage.py poblar_datos --cantidad 500
```

Con 500 dueños deberías obtener aproximadamente:

```
Dueños:       500
Mascotas:   ~1.250
Consultas:  ~5.000
Vacunas:    ~2.500
```

**Verificación:** Entra al admin y navega las listas. Si la lista de consultas tarda más de 2 segundos en cargar, el escenario de rendimiento está listo.

---

---

# FASE 3 — Instalar Django Debug Toolbar

---

## Paso 4 — Configurar la herramienta de diagnóstico

---

**¿Por qué?** Sin medición, la optimización es adivinanza. Django Debug Toolbar te muestra exactamente cuántas consultas genera cada página.

> 📊 **Dato real**: Según el proyecto Django Debug Toolbar en GitHub (2025), la herramienta se descarga más de 1.5 millones de veces al mes desde PyPI, siendo la herramienta de diagnóstico más usada en el ecosistema Django.
>
> _Fuente: PyPI Stats, "django-debug-toolbar download statistics" (2025)_

### 4.1 — Instalar

```bash
pip install django-debug-toolbar
```

### 4.2 — Configurar en `development.py`

Agrega al archivo `fichas/settings/development.py` (o el archivo donde está tu configuración de desarrollo):

```python
INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware']

INTERNAL_IPS = ['127.0.0.1']
```

> ⚠️ **Solo en desarrollo.** Nunca agregues Debug Toolbar en producción.

### 4.3 — Agregar la URL

En el `urls.py` **del proyecto**, agrega:

```python
from django.conf import settings

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
```

### 4.4 — Verificar

Corre el servidor y entra a cualquier página del CRUD (ej: `/duenos/`). A la derecha debería aparecer un **panel lateral** con información de SQL, tiempo, templates, etc.

Haz clic en la sección **SQL** del panel. Anota:

- **Cantidad de queries** en la lista de dueños: ______
- **Cantidad de queries** en la lista de mascotas: ______
- **Cantidad de queries** en la lista de consultas: ______

Estos son tus números de referencia **antes** de optimizar.

---

---

# FASE 4 — Diagnosticar y corregir el problema N+1

---

## Paso 5 — Identificar N+1 en la lista de mascotas

---

**¿Por qué?** La lista de mascotas muestra el nombre del dueño con cada mascota. Sin optimización, Django hace una consulta extra por cada mascota para obtener los datos de su dueño. Esto genera el clásico problema N+1.

### 5.1 — Medir el problema

Con Debug Toolbar activo, entra a `/mascotas/`. Observa la sección SQL:

- Si tienes 1.250 mascotas, deberías ver aproximadamente **1.251 consultas** (1 para traer las mascotas + 1 por cada mascota para traer su dueño).
- El tiempo total de base de datos debería ser alto.

Anota estos valores:

```
ANTES — Lista de mascotas:
  Queries: ______
  Tiempo DB: ______
```

### 5.2 — Corregir con `select_related`

Abre `fichas/views.py`. En `MascotaListView`, sobreescribe el `queryset` para usar `select_related`:

```python
class MascotaListView(ListView):
    model = Mascota
    template_name = 'fichas/mascota_list.html'
    queryset = Mascota.objects.select_related('dueno')
```

> 📖 `select_related('dueno')` le dice al ORM: "cuando traigas las mascotas, trae también los datos del dueño en la misma consulta con un JOIN".

### 5.3 — Medir la mejora

Recarga `/mascotas/` y observa Debug Toolbar:

```
DESPUÉS — Lista de mascotas:
  Queries: ______  (debería ser 1 o 2)
  Tiempo DB: ______  (debería ser mucho menor)
```

> 💡 La cantidad de queries debería bajar de ~1.251 a exactamente **1** (o 2 si Django Debug Toolbar agrega una consulta propia). Si la mejora es visible, el `select_related` está funcionando.

---

## Paso 6 — Corregir N+1 en la lista de consultas médicas

---

La lista de consultas médicas tiene el mismo problema: muestra el nombre de la mascota, lo que genera N+1 queries.

### 6.1 — Identificar la cadena de relaciones

`ConsultaMedica` tiene una FK a `Mascota`, y `Mascota` tiene una FK a `Dueno`. Si en el template muestras el nombre de la mascota **y** el nombre del dueño, son **dos niveles** de relación.

### 6.2 — Corregir con `select_related` encadenado

En `ConsultaMedicaListView` (si la tienes) o en cualquier vista que liste consultas:

```python
queryset = ConsultaMedica.objects.select_related('mascota', 'mascota__dueno')
```

Esto genera un solo JOIN que trae la consulta, la mascota y el dueño en una única consulta SQL.

### 6.3 — Medir y documentar

```
ANTES — Lista de consultas médicas:
  Queries: ______
  Tiempo DB: ______

DESPUÉS — Lista de consultas médicas:
  Queries: ______
  Tiempo DB: ______
```

---

## Paso 7 — Usar `prefetch_related` en el detalle de un dueño

---

**¿Por qué?** El detalle de un dueño muestra sus mascotas (relación inversa). Aquí `select_related` no funciona — la relación es uno-a-muchos. Se debe usar `prefetch_related`.

### 7.1 — Corregir `DuenoDetailView`

```python
class DuenoDetailView(DetailView):
    model = Dueno
    template_name = 'fichas/dueno_detail.html'

    def get_queryset(self):
        return Dueno.objects.prefetch_related('mascota_set')
```

### 7.2 — Prefetch anidado: mascotas con sus consultas

Si en el detalle del dueño también muestras las consultas de cada mascota, necesitas un prefetch anidado:

```python
from django.db.models import Prefetch

def get_queryset(self):
    return Dueno.objects.prefetch_related(
        Prefetch(
            'mascota_set',
            queryset=Mascota.objects.prefetch_related('consultamedica_set')
        )
    )
```

Con esto, Django ejecuta exactamente **3 consultas** sin importar cuántas mascotas o consultas tenga el dueño:

```
Consulta 1: SELECT * FROM dueno WHERE id = X;
Consulta 2: SELECT * FROM mascota WHERE dueno_id = X;
Consulta 3: SELECT * FROM consultamedica WHERE mascota_id IN (lista de IDs);
```

### 7.3 — Medir y documentar

```
ANTES — Detalle de dueño (con 4 mascotas y 20 consultas):
  Queries: ______

DESPUÉS — Detalle de dueño:
  Queries: ______  (debería ser 3)
```

---

---

# FASE 5 — Paginación

---

## Paso 8 — Implementar paginación en todas las listas

---

**¿Por qué?** Sin paginación, la lista de consultas carga **todos** los registros en una sola página. Con 5.000 consultas, el navegador tarda en renderizar la tabla completa.

> 📊 **Dato real**: Según el reporte de rendimiento web de Cloudflare (2025), las páginas que implementan paginación server-side reducen el Time to First Byte (TTFB) en un 78% comparado con cargar todos los registros.
>
> _Fuente: Cloudflare, "Web Performance Report: Server-Side Pagination Impact" (2025)_

### 8.1 — Agregar paginación a las CBV

Django `ListView` tiene paginación integrada. Solo necesitas agregar un atributo:

```python
class DuenoListView(ListView):
    model = Dueno
    template_name = 'fichas/dueno_list.html'
    paginate_by = 25
```

Haz lo mismo para `MascotaListView` y cualquier otra ListView.

### 8.2 — Crear el template parcial de paginación

Crea el archivo `templates/fichas/paginacion.html` con controles de navegación:

```html
{% if is_paginated %}
<nav style="text-align: center; margin: 20px 0;">
    {% if page_obj.has_previous %}
        <a href="?page=1" class="btn btn-primary">⏮ Primera</a>
        <a href="?page={{ page_obj.previous_page_number }}" class="btn btn-primary">◀ Anterior</a>
    {% endif %}

    <span style="margin: 0 15px; font-weight: bold;">
        Página {{ page_obj.number }} de {{ page_obj.paginator.num_pages }}
    </span>

    {% if page_obj.has_next %}
        <a href="?page={{ page_obj.next_page_number }}" class="btn btn-primary">Siguiente ▶</a>
        <a href="?page={{ page_obj.paginator.num_pages }}" class="btn btn-primary">Última ⏭</a>
    {% endif %}
</nav>
{% endif %}
```

### 8.3 — Incluir la paginación en las listas

En cada template de lista (`dueno_list.html`, `mascota_list.html`, etc.), agrega al final de la tabla:

```html
{% include 'fichas/paginacion.html' %}
```

### 8.4 — Verificar

Recarga `/duenos/` — ahora muestra solo 25 registros por página con controles de navegación. La carga debería ser instantánea incluso con miles de registros.

```
ANTES — Lista de dueños (500 registros sin paginar):
  Tiempo de carga: ______

DESPUÉS — Lista de dueños (25 por página):
  Tiempo de carga: ______
```

---

---

# FASE 6 — Índices de base de datos

---

## Paso 9 — Agregar índices a los campos más consultados

---

**¿Por qué?** Sin índices, la base de datos hace búsqueda secuencial por cada consulta filtrada u ordenada. Con miles de registros, la diferencia entre búsqueda secuencial (O(n)) e indexada (O(log n)) es enorme.

> 📊 **Dato real**: Según benchmarks de Percona (2025), en una tabla de 1 millón de registros en PostgreSQL 17, una consulta filtrada sin índice tarda 2-3 segundos. Con un índice B-tree apropiado, la misma consulta se ejecuta en 1-5 milisegundos.
>
> _Fuente: Percona, "Database Indexing Best Practices" (2025)_

### 9.1 — Identificar qué campos necesitan índice

Revisa tu código: ¿qué campos usas en `filter()`, `order_by()`, `search_fields` y `list_filter`?

| Modelo           | Campo                 | ¿Se filtra/ordena? | ¿Tiene índice? |
| :--------------- | :-------------------- | :------------------ | :------------- |
| `Dueno`          | `rut`                 | Sí (unique ya lo tiene) | ✅         |
| `Mascota`        | `especie`             | Sí (list_filter)    | ❌ Agregar  |
| `Mascota`        | `activo`              | Sí (se filtrará)    | ❌ Agregar  |
| `ConsultaMedica` | `fecha`               | Sí (ordering)       | ❌ Agregar  |
| `ConsultaMedica` | `costo`               | Sí (posible filtro) | ❌ Agregar  |
| `Vacuna`         | `fecha_aplicacion`    | Sí (ordering)       | ❌ Agregar  |
| `Vacuna`         | `nombre_vacuna`       | Sí (list_filter)    | ❌ Agregar  |

### 9.2 — Agregar índices en los modelos

Abre `fichas/models.py` y agrega los índices usando `class Meta`:

Para `Mascota`:

```python
class Meta:
    indexes = [
        models.Index(fields=['especie']),
        models.Index(fields=['activo']),
    ]
```

Para `ConsultaMedica`:

```python
class Meta:
    indexes = [
        models.Index(fields=['-fecha']),
        models.Index(fields=['costo']),
    ]
```

Para `Vacuna`:

```python
class Meta:
    indexes = [
        models.Index(fields=['-fecha_aplicacion']),
        models.Index(fields=['nombre_vacuna']),
    ]
```

> 💡 El prefijo `-` en el campo indica un índice descendente, ideal para ordenar "los más recientes primero".

### 9.3 — Migrar los índices

```bash
python manage.py makemigrations
python manage.py migrate
```

Revisa la migración generada — deberías ver operaciones `AddIndex` para cada índice nuevo.

**Verificación:** Los índices son invisibles para el usuario, pero puedes verificar su efecto midiendo el tiempo de las consultas filtradas con Debug Toolbar antes y después de migrar.

---

---

# FASE 7 — Estadísticas con `aggregate()` y `annotate()`

---

## Paso 10 — Crear la vista de estadísticas de la clínica

---

**¿Por qué?** La clínica necesita un panel que muestre métricas clave: ingresos totales, promedio de costo por consulta, cantidad de mascotas por especie, etc. Estos cálculos **deben hacerse en la base de datos**, no en Python.

### 10.1 — Crear la vista

Crea una nueva vista basada en función en `fichas/views.py`:

```python
from django.db.models import Sum, Avg, Count, Max, Min
from django.shortcuts import render

def estadisticas_clinica(request):
    # -- Métricas generales con aggregate() --
    metricas = ConsultaMedica.objects.aggregate(
        total_ingresos=Sum('costo'),
        promedio_consulta=Avg('costo'),
        consulta_mas_cara=Max('costo'),
        consulta_mas_barata=Min('costo'),
        total_consultas=Count('id'),
    )

    # -- Mascotas por especie con annotate() --
    mascotas_por_especie = (
        Mascota.objects
        .values('especie')
        .annotate(cantidad=Count('id'))
        .order_by('-cantidad')
    )

    # -- Top 5 dueños con más mascotas --
    top_duenos = (
        Dueno.objects
        .annotate(total_mascotas=Count('mascota'))
        .order_by('-total_mascotas')[:5]
    )

    # -- Ingresos por mes (últimos 6 meses) --
    from django.db.models.functions import TruncMonth
    ingresos_por_mes = (
        ConsultaMedica.objects
        .annotate(mes=TruncMonth('fecha'))
        .values('mes')
        .annotate(
            total=Sum('costo'),
            cantidad=Count('id')
        )
        .order_by('-mes')[:6]
    )

    # -- Vacunas más aplicadas --
    vacunas_populares = (
        Vacuna.objects
        .values('nombre_vacuna')
        .annotate(total=Count('id'))
        .order_by('-total')[:5]
    )

    # -- Conteos generales (usando .count() en vez de len()) --
    total_duenos = Dueno.objects.count()
    total_mascotas = Mascota.objects.count()
    mascotas_activas = Mascota.objects.filter(activo=True).count()
    mascotas_inactivas = Mascota.objects.filter(activo=False).count()

    # -- Verificar existencia eficiente --
    hay_consultas_sin_costo = ConsultaMedica.objects.filter(costo=0).exists()

    context = {
        'metricas': metricas,
        'mascotas_por_especie': mascotas_por_especie,
        'top_duenos': top_duenos,
        'ingresos_por_mes': ingresos_por_mes,
        'vacunas_populares': vacunas_populares,
        'total_duenos': total_duenos,
        'total_mascotas': total_mascotas,
        'mascotas_activas': mascotas_activas,
        'mascotas_inactivas': mascotas_inactivas,
        'hay_consultas_sin_costo': hay_consultas_sin_costo,
    }
    return render(request, 'fichas/estadisticas.html', context)
```

> ⚠️ **Observa:** Ninguno de estos cálculos carga registros individuales a memoria. Todo se calcula en la base de datos. Con 5.000 consultas, esto se ejecuta en milisegundos.

### 10.2 — Agregar la URL

En `fichas/urls.py`, agrega:

```python
path('estadisticas/', views.estadisticas_clinica, name='estadisticas'),
```

### 10.3 — Crear el template `estadisticas.html`

Crea `templates/fichas/estadisticas.html` que extienda de `base.html` y presente las estadísticas de forma atractiva.

El template debe mostrar:

**Sección 1 — Resumen General:**

Una tabla o tarjetas con:

| Métrica                | Valor                                |
| :--------------------- | :----------------------------------- |
| Total de dueños        | `{{ total_duenos }}`                 |
| Total de mascotas      | `{{ total_mascotas }}`               |
| Mascotas activas       | `{{ mascotas_activas }}`             |
| Total de consultas     | `{{ metricas.total_consultas }}`     |
| Ingresos totales       | `{{ metricas.total_ingresos }}`      |
| Promedio por consulta   | `{{ metricas.promedio_consulta }}`   |

**Sección 2 — Mascotas por especie:**

Una tabla con las columnas `Especie` y `Cantidad`, iterando sobre `mascotas_por_especie`.

**Sección 3 — Top 5 dueños con más mascotas:**

Una tabla con `Nombre` y `Total mascotas`, iterando sobre `top_duenos`.

**Sección 4 — Ingresos por mes:**

Una tabla con `Mes`, `Cantidad de consultas` y `Total ingresos`, iterando sobre `ingresos_por_mes`.

**Sección 5 — Vacunas más aplicadas:**

Una tabla con `Vacuna` y `Cantidad`, iterando sobre `vacunas_populares`.

> 💡 Si hay consultas sin costo, muestra un aviso:
> ```html
> {% if hay_consultas_sin_costo %}
>     <p style="color: #e74c3c;">⚠️ Hay consultas registradas sin costo.</p>
> {% endif %}
> ```

### 10.4 — Actualizar la navegación

En `templates/fichas/base.html`, agrega un link al navbar:

```html
<a href="{% url 'fichas:estadisticas' %}">📊 Estadísticas</a>
```

### 10.5 — Verificar con Debug Toolbar

Entra a `/estadisticas/` y observa la sección SQL del Debug Toolbar:

```
Página de estadísticas:
  Queries: ______  (debería ser entre 6 y 10, una por cada aggregate/annotate)
  Tiempo DB: ______  (debería ser milisegundos, no segundos)
```

Si toda la información aparece con menos de 10 queries, las delegaciones a la base de datos están funcionando correctamente.

---

---

# FASE 8 — Optimizar el Admin

---

## Paso 11 — Corregir N+1 en el admin personalizado

---

**¿Por qué?** El admin de Django también sufre el problema N+1. Si en `MascotaAdmin` muestras el nombre del dueño como columna (`list_display`), Django hace una consulta extra por cada mascota para obtener el dueño.

### 11.1 — Sobreescribir `get_queryset` en el admin

En cada `ModelAdmin` que muestre relaciones en `list_display`, sobreescribe `get_queryset`:

```python
@admin.register(Mascota)
class MascotaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'especie', 'raza', 'dueno', 'activo')
    # ... resto de la configuración ...

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('dueno')
```

Haz lo mismo para `ConsultaMedicaAdmin`:

```python
def get_queryset(self, request):
    qs = super().get_queryset(request)
    return qs.select_related('mascota', 'mascota__dueno')
```

Y para `VacunaAdmin`:

```python
def get_queryset(self, request):
    qs = super().get_queryset(request)
    return qs.select_related('mascota')
```

### 11.2 — Medir la mejora en el admin

Con Debug Toolbar, navega a la lista de mascotas en el admin (`/admin/fichas/mascota/`):

```
ANTES — Admin lista mascotas:
  Queries: ______

DESPUÉS — Admin lista mascotas:
  Queries: ______
```

---

## Paso 12 — Optimizar las columnas calculadas del admin

---

En la Clase 11 creaste la columna calculada `cantidad_mascotas` en `DuenoAdmin` que hace `obj.mascota_set.count()`. Esta columna genera **una consulta extra por cada dueño** mostrado en la lista.

### 12.1 — Optimizar con `annotate`

Sobreescribe `get_queryset` en `DuenoAdmin` para anotar la cantidad:

```python
@admin.register(Dueno)
class DuenoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'rut', 'telefono', 'email', 'cantidad_mascotas')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_cantidad_mascotas=Count('mascota'))

    def cantidad_mascotas(self, obj):
        return obj._cantidad_mascotas
    cantidad_mascotas.short_description = 'Mascotas'
    cantidad_mascotas.admin_order_field = '_cantidad_mascotas'
```

> 💡 Al usar `admin_order_field`, la columna se vuelve **ordenable** con un clic en el encabezado.

### 12.2 — Lo mismo para `costo_total_consultas` en `MascotaAdmin`

Si tienes la columna calculada de costo total:

```python
def get_queryset(self, request):
    qs = super().get_queryset(request)
    return qs.select_related('dueno').annotate(
        _costo_total=Sum('consultamedica__costo')
    )

def costo_total_consultas(self, obj):
    total = obj._costo_total or 0
    return f'${total:,.0f}'
costo_total_consultas.short_description = 'Costo total consultas'
costo_total_consultas.admin_order_field = '_costo_total'
```

**Verificación:** La lista de dueños en el admin muestra la columna "Mascotas" y es ordenable. Debug Toolbar muestra que toda la lista se genera con **una sola consulta**.

---

---

# FASE 9 — Uso de `.only()` y `.defer()`

---

## Paso 13 — Traer solo los campos necesarios

---

**¿Por qué?** Si la lista de mascotas solo muestra nombre, especie y dueño, no hay razón para traer los campos `raza`, `fecha_nacimiento`, `direccion` del dueño, etc. Cada campo extra consume ancho de banda y memoria.

### 13.1 — Usar `.only()` en la vista de lista

Modifica `MascotaListView`:

```python
class MascotaListView(ListView):
    model = Mascota
    template_name = 'fichas/mascota_list.html'
    paginate_by = 25

    def get_queryset(self):
        return (
            Mascota.objects
            .select_related('dueno')
            .only('nombre', 'especie', 'raza', 'activo', 'dueno__nombre')
        )
```

### 13.2 — Usar `.defer()` para excluir campos pesados

Si un modelo tuviera un campo `TextField` muy largo (como `diagnostico` en `ConsultaMedica`), puedes excluirlo de la lista:

```python
queryset = ConsultaMedica.objects.select_related('mascota').defer('diagnostico', 'tratamiento')
```

> ⚠️ **Regla de seguridad:** Si en el template accedes a un campo excluido con `defer()`, el ORM hará una consulta extra por cada registro para buscarlo. Si no estás seguro, usa `.only()` que es más explícito.

**Verificación:** Con Debug Toolbar, observa el SQL generado. Debería mostrar `SELECT nombre, especie, ...` en vez de `SELECT *`.

---

---

# FASE 10 — Filtros avanzados y búsqueda eficiente

---

## Paso 14 — Agregar filtro de mascotas activas/inactivas

---

### 14.1 — Vista con filtro por estado

Modifica `MascotaListView` para aceptar un parámetro de filtro por URL:

```python
class MascotaListView(ListView):
    model = Mascota
    template_name = 'fichas/mascota_list.html'
    paginate_by = 25

    def get_queryset(self):
        qs = Mascota.objects.select_related('dueno')
        estado = self.request.GET.get('estado')
        if estado == 'activas':
            qs = qs.filter(activo=True)
        elif estado == 'inactivas':
            qs = qs.filter(activo=False)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['estado_actual'] = self.request.GET.get('estado', 'todas')
        return context
```

### 14.2 — Agregar botones de filtro en el template

En `mascota_list.html`, antes de la tabla:

```html
<div style="margin-bottom: 15px;">
    <strong>Filtrar:</strong>
    <a href="?estado=todas" class="btn btn-primary">Todas</a>
    <a href="?estado=activas" class="btn btn-success">Activas</a>
    <a href="?estado=inactivas" class="btn btn-warning">Inactivas</a>
</div>
```

### 14.3 — Buscador eficiente con `icontains`

Agrega un buscador a `DuenoListView`:

```python
class DuenoListView(ListView):
    model = Dueno
    template_name = 'fichas/dueno_list.html'
    paginate_by = 25

    def get_queryset(self):
        qs = Dueno.objects.all()
        busqueda = self.request.GET.get('q')
        if busqueda:
            qs = qs.filter(nombre__icontains=busqueda)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['busqueda'] = self.request.GET.get('q', '')
        return context
```

En `dueno_list.html`, antes de la tabla:

```html
<form method="get" style="margin-bottom: 15px;">
    <input type="text" name="q" placeholder="Buscar por nombre..."
           value="{{ busqueda }}"
           style="padding: 8px; width: 300px; border: 1px solid #ccc; border-radius: 4px;">
    <button type="submit" class="btn btn-primary">🔍 Buscar</button>
    {% if busqueda %}
        <a href="{% url 'fichas:dueno_lista' %}" class="btn btn-warning">Limpiar</a>
    {% endif %}
</form>
```

**Verificación:** El buscador filtra los dueños por nombre y el filtro de estado funciona para mascotas. Debug Toolbar muestra que la consulta SQL incluye el `WHERE` correspondiente.

---

---

# FASE 11 — Documentación de cambios

---

## Paso 15 — Crear el informe de optimización

---

**¿Por qué?** Documentar las mejoras es parte del trabajo profesional. Sin documentación, nadie sabe qué se cambió ni por qué.

Crea un archivo en la raíz de tu proyecto llamado `informe_optimizacion.md` con el siguiente formato:

```markdown
# Informe de Optimización — PatasFelices

## Datos del proyecto
- **Cantidad de dueños:** ___
- **Cantidad de mascotas:** ___
- **Cantidad de consultas:** ___
- **Cantidad de vacunas:** ___

## Mejoras aplicadas

### 1. select_related en lista de mascotas
- **Archivo:** fichas/views.py
- **Antes:** ___ queries, ___ ms
- **Después:** ___ queries, ___ ms
- **Mejora:** ___% menos queries

### 2. select_related en lista de consultas
- **Archivo:** fichas/views.py
- **Antes:** ___ queries, ___ ms
- **Después:** ___ queries, ___ ms
- **Mejora:** ___% menos queries

### 3. prefetch_related en detalle de dueño
- **Archivo:** fichas/views.py
- **Antes:** ___ queries
- **Después:** 3 queries
- **Mejora:** ___

### 4. Paginación (25 por página)
- **Archivos:** fichas/views.py, templates
- **Antes:** ___ registros en una sola página
- **Después:** 25 registros por página
- **Mejora:** carga instantánea

### 5. Índices de base de datos
- **Archivo:** fichas/models.py
- **Índices agregados:** especie, activo, fecha, costo, fecha_aplicacion, nombre_vacuna

### 6. aggregate() / annotate() en estadísticas
- **Archivo:** fichas/views.py
- **Queries totales en /estadisticas/:** ___
- **Todas las métricas calculadas en la BD:** Sí

### 7. Optimización del admin
- **Archivo:** fichas/admin.py
- **Antes (lista mascotas admin):** ___ queries
- **Después:** ___ queries

## Conclusiones
(Escribe 3-4 líneas sobre lo que aprendiste)
```

---

---

# Prueba final del flujo completo

---

Realiza cada verificación antes de marcarla como completada:

**Modelos y datos:**

- [ ] El modelo `Vacuna` existe, con migración aplicada.
- [ ] El campo `activo` existe en `Mascota`.
- [ ] El comando `poblar_datos` genera correctamente dueños, mascotas, consultas y vacunas.
- [ ] La base de datos tiene al menos 500 dueños y datos proporcionales.

**Debug Toolbar:**

- [ ] Django Debug Toolbar está instalado y funcionando.
- [ ] Se puede ver la cantidad de queries en cada página.

**Optimizaciones N+1:**

- [ ] La lista de mascotas usa `select_related('dueno')`.
- [ ] La lista de consultas usa `select_related('mascota', 'mascota__dueno')`.
- [ ] El detalle de dueño usa `prefetch_related`.

**Paginación:**

- [ ] Todas las listas muestran 25 registros por página.
- [ ] Los controles de navegación funcionan (primera, anterior, siguiente, última).

**Índices:**

- [ ] Se agregaron índices a especie, activo, fecha, costo, fecha_aplicacion, nombre_vacuna.
- [ ] Las migraciones de índices están aplicadas.

**Estadísticas:**

- [ ] La página `/estadisticas/` funciona y muestra todas las métricas.
- [ ] Todas las métricas se calculan con `aggregate()`/`annotate()`, no con loops de Python.
- [ ] Debug Toolbar muestra menos de 10 queries en la página de estadísticas.

**Admin optimizado:**

- [ ] `MascotaAdmin` usa `select_related` en `get_queryset`.
- [ ] `DuenoAdmin` usa `annotate` para la columna calculada `cantidad_mascotas`.
- [ ] La columna `cantidad_mascotas` es ordenable.

**Filtros y búsqueda:**

- [ ] El filtro de mascotas activas/inactivas funciona.
- [ ] El buscador de dueños filtra correctamente.

**Documentación:**

- [ ] Existe el archivo `informe_optimizacion.md` con mediciones de antes/después.

---

---

# Checklist de entrega

---

| #   | Requisito                                                                         | Estado |
| :-- | :-------------------------------------------------------------------------------- | :----- |
| 1   | Modelo `Vacuna` creado con migración aplicada                                     | [ ]    |
| 2   | Campo `activo` en `Mascota` con migración aplicada                                | [ ]    |
| 3   | Management command `poblar_datos` funcional con `bulk_create`                     | [ ]    |
| 4   | Django Debug Toolbar instalado y configurado (solo en desarrollo)                 | [ ]    |
| 5   | `select_related` aplicado en `MascotaListView` y lista de consultas              | [ ]    |
| 6   | `prefetch_related` aplicado en `DuenoDetailView`                                 | [ ]    |
| 7   | Paginación de 25 registros en todas las `ListView`                               | [ ]    |
| 8   | Template `paginacion.html` creado y funcionando                                   | [ ]    |
| 9   | Índices agregados en campos de filtro y ordenamiento (6 índices mínimo)           | [ ]    |
| 10  | Vista `estadisticas_clinica` con `aggregate()` y `annotate()`                    | [ ]    |
| 11  | Template `estadisticas.html` mostrando todas las métricas                        | [ ]    |
| 12  | Admin optimizado con `select_related` en `get_queryset`                          | [ ]    |
| 13  | Columna `cantidad_mascotas` optimizada con `annotate` y ordenable                | [ ]    |
| 14  | Filtro de mascotas activas/inactivas funcionando                                  | [ ]    |
| 15  | Buscador de dueños implementado                                                   | [ ]    |
| 16  | `informe_optimizacion.md` con datos de antes/después para cada mejora            | [ ]    |

---

---

# Preguntas para pensar después de terminar

---

- ¿Qué pasaría si usas `len(queryset)` en vez de `queryset.count()` para contar 500.000 registros? ¿Cuánta memoria consumiría?
- Si agregas un índice a un campo que **nunca** se usa en filtros, ¿mejora o empeora el rendimiento? ¿Por qué?
- ¿En qué caso usarías `prefetch_related` en vez de `select_related`? Da un ejemplo con los modelos de PatasFelices.
- ¿Qué diferencia hay entre `aggregate()` y `annotate()`? ¿Cuándo usarías cada uno?
- Si la lista de dueños muestra 50.000 registros sin paginación y la tabla tarda 15 segundos en cargar, ¿cuántos puntos de optimización podrías aplicar? Nómbralos.
- ¿Por qué `sorted()` en Python es peor que `order_by()` del ORM para ordenar registros de la base de datos?

---

> _"Optimizar no es hacer que el código se vea más complejo. Es hacer que la base de datos trabaje de forma inteligente, para que el usuario ni siquiera piense en esperar."_

---
