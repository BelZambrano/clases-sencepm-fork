# 🚨 Django — Módulo 6 · Clase 9b

## Páginas de Error Personalizadas

---

> _"Un 500 con el stack trace de Django en producción no es un error — es un currículum para hackers."_

---

## ¿De qué trata esta parte?

Cuando algo sale mal, el servidor responde con un **código de estado HTTP**.
Django puede mostrar páginas propias para esos errores — o las del framework por defecto, que son feas y exponen información interna.

Esta guía cubre los tres errores más importantes en este orden:

| Código | Cuándo aparece                        |
| ------ | ------------------------------------- |
| `404`  | La URL o el objeto buscado no existe  |
| `403`  | Acceso denegado — sin permiso         |
| `500`  | El servidor crasheó con una excepción |

---

## El interruptor: `DEBUG`

Hay un parámetro en `settings.py` que cambia todo el comportamiento de los errores:

| Comportamiento                       | `DEBUG = True` (desarrollo)    | `DEBUG = False` (producción) |
| ------------------------------------ | ------------------------------ | ---------------------------- |
| 404                                  | Página amarilla con las URLs   | Tu `404.html`                |
| 403                                  | Texto plano "403 Forbidden"    | Tu `403.html`                |
| 500                                  | Stack trace completo del error | Tu `500.html`                |
| ¿Las páginas personalizadas se usan? | ❌ No                          | ✅ Sí                        |

**Mientras `DEBUG = True`, Django ignora los templates `403.html`, `404.html` y `500.html`.**
Se activan únicamente con `DEBUG = False`.

---

## Carpeta de templates a nivel proyecto

Los tres templates van en la raíz de la carpeta `templates/`:

```
mi_proyecto/
├── templates/
│   ├── base.html
│   ├── 404.html     ← aquí
│   ├── 403.html     ← aquí
│   └── 500.html     ← aquí
├── mi_app/
└── settings.py
```

Y `settings.py` debe apuntar a esa carpeta:

```python
# settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],   # ← sin esto Django no los encuentra
        'APP_DIRS': True,
        ...
    },
]
```

---

---

# Parte I — Error 404

---

> _"La URL que buscás no existe. Pero el sitio sí."_

---

## ¿Cuándo dispara Django un 404?

| Situación                                         | Cómo se dispara                   |
| ------------------------------------------------- | --------------------------------- |
| La URL no coincide con ningún patrón en `urls.py` | Automático, Django lo hace solo   |
| El objeto buscado no existe en la base de datos   | `get_object_or_404()` o `Http404` |
| El código lo lanza explícitamente                 | `raise Http404`                   |

---

## Cómo disparar un 404 desde el código

### La forma correcta: `get_object_or_404`

```python
from django.shortcuts import get_object_or_404, render
from .models import Producto

def detalle_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    #          ↑ si pk=999 y no existe → dispara 404 automáticamente
    #            si existe              → devuelve el objeto normalmente
    return render(request, 'detalle.html', {'producto': producto})
```

**Por qué no usar `.get()` directamente:**

```python
# ❌ Forma incorrecta
producto = Producto.objects.get(pk=pk)
# Si el producto no existe → lanza DoesNotExist → crash → error 500
# Un "objeto no encontrado" termina siendo un "error del servidor". Incorrecto.

# ✅ Forma correcta
producto = get_object_or_404(Producto, pk=pk)
# Si no existe → 404. Semánticamente correcto — el recurso no existe.
```

### `get_object_or_404` acepta cualquier campo

```python
# buscar por slug en lugar de pk
articulo = get_object_or_404(Articulo, slug=slug)

# buscar con condición adicional
articulo = get_object_or_404(Articulo, slug=slug, publicado=True)
# → si el artículo existe pero no está publicado → también dispara 404
```

### Lanzar Http404 manualmente

Cuando la lógica es más compleja que buscar un objeto:

```python
from django.http import Http404

def busqueda(request):
    query = request.GET.get('q', '')
    if len(query) < 3:
        raise Http404("La búsqueda necesita al menos 3 caracteres")
    #    ↑ cualquier condición de negocio puede disparar un 404
```

---

## El template `404.html`

```html
<!-- templates/404.html -->
{% extends 'base.html' %} {% block content %}

<div class="container my-5 text-center">
  <h1 class="display-1 text-warning">404</h1>
  <h2>Página no encontrada</h2>
  <p class="text-muted">La página que buscás no existe o fue movida.</p>
  {% if exception %}
  <p class="text-secondary"><small>Detalle: {{ exception }}</small></p>
  {% endif %}
  <a href="{% url 'home' %}" class="btn btn-primary">Volver al inicio</a>
</div>

{% endblock %}
```

**Variable especial `{{ exception }}`:** Django la pasa automáticamente al template del 404.
Contiene el mensaje del error — por ejemplo, el string dentro de `raise Http404("...")`.

---

## Manejador personalizado para el 404

Por defecto, Django busca `404.html` y lo renderiza.
Si se necesita lógica adicional (pasar contexto extra, registrar el intento en la BD, etc.),
se puede reemplazar con una función propia:

```python
# mi_app/views.py
from django.shortcuts import render

def handler_404(request, exception):
    context = {
        'url_intentada': request.path,   # la URL que el usuario quiso visitar
    }
    return render(request, '404.html', context, status=404)
    #                                            ↑ el status=404 es obligatorio
    #                                              sin él, Django devuelve 200 aunque muestre la página de error
```

```python
# urls.py principal del proyecto
handler404 = 'mi_app.views.handler_404'
#            ↑ siempre un string con la ruta completa: 'app.views.nombre_funcion'
#              y siempre en el urls.py raíz, no en el de una app
```

```html
<!-- templates/404.html — usando el contexto adicional -->
{% extends 'base.html' %} {% block content %}

<div class="container my-5 text-center">
  <h1 class="display-1 text-warning">404</h1>
  <h2>Página no encontrada</h2>
  <p class="text-muted">
    La URL <code>{{ url_intentada }}</code> no existe en este sitio.
  </p>
  <a href="{% url 'home' %}" class="btn btn-primary">Volver al inicio</a>
</div>

{% endblock %}
```

---

## Probar el 404 en desarrollo (sin cambiar `DEBUG`)

Mientras `DEBUG = True`, los templates personalizados no se muestran.
Para probarlos sin apagar el debug:

```python
# mi_app/views.py — solo para testing, eliminar después
from django.shortcuts import render

def test_404(request):
    return render(request, '404.html', status=404)
```

```python
# urls.py
path('test-404/', test_404),   # visitar esta URL para ver cómo queda el template
```

---

---

# Parte II — Error 403

---

> _"Sé quién sos. Pero no puedes entrar."_

---

## ¿Cuándo dispara Django un 403?

| Situación                                  | Cómo se dispara                                        |
| ------------------------------------------ | ------------------------------------------------------ |
| Permiso requerido y el usuario no lo tiene | `@permission_required(..., raise_exception=True)`      |
| Permiso requerido en vista de clase        | `PermissionRequiredMixin` con `raise_exception = True` |
| Lógica manual en la vista                  | `raise PermissionDenied`                               |
| Token CSRF inválido o ausente              | Middleware CSRF — automático                           |

---

## Cómo disparar un 403 desde el código

### Con decorador

```python
from django.contrib.auth.decorators import login_required, permission_required

@login_required
@permission_required('tienda.change_producto', raise_exception=True)
#                                              ↑ sin esto → redirige al login aunque ya tenga sesión
#                                                con esto  → muestra el error 403
def editar_producto(request, pk):
    ...
```

### Con Mixin en vista de clase

```python
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import UpdateView

class EditarProductoView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model               = Producto
    fields              = ['nombre', 'precio']
    template_name       = 'producto_form.html'
    permission_required = 'tienda.change_producto'
    raise_exception     = True     # ← 403 si tiene sesión pero no el permiso
```

### Lanzar `PermissionDenied` manualmente

```python
from django.core.exceptions import PermissionDenied

def editar_perfil(request, pk):
    perfil = get_object_or_404(Perfil, pk=pk)
    if perfil.usuario != request.user:
        raise PermissionDenied
        # ↑ el usuario intenta editar el perfil de otro → 403
    ...
```

---

## El template `403.html`

```html
<!-- templates/403.html -->
{% extends 'base.html' %} {% block content %}

<div class="container my-5 text-center">
  <h1 class="display-1 text-danger">403</h1>
  <h2>Acceso denegado</h2>
  <p class="text-muted">
    No tienes permiso para ver esta página. Contactá a un administrador si crees
    que esto es un error.
  </p>
  <a href="{% url 'home' %}" class="btn btn-secondary">Volver al inicio</a>
</div>

{% endblock %}
```

---

## Comportamiento del 403 según el estado de sesión

Aquí está el punto que confunde a muchos:

```
Usuario sin sesión → intenta acceder a /panel-admin/
      ↓
¿Cómo está configurado el decorador?

  @login_required                           → redirige a /login/?next=/panel-admin/
  @permission_required(raise_exception=True)→ muestra 403 (incorrecto para este caso)
  @login_required + @permission_required    → primero verifica sesión → redirige al login ✅
```

**La regla:** siempre poner `@login_required` antes de `@permission_required`.
Si el usuario no tiene sesión → va al login. Si tiene sesión pero no el permiso → 403.

---

## Qué hace Django cuando llega un 403 sin sesión

Por defecto, `@login_required` redirige al login con `?next=`.
`@permission_required` con `raise_exception=True` muestra el 403 **sin importar** si hay sesión o no.

Por eso el orden de decoradores es crítico:

```python
@login_required                                              # 1° verifica: ¿tiene sesión?
@permission_required('app.change_x', raise_exception=True)  # 2° verifica: ¿tiene permiso?
def mi_vista(request):
    ...
```

Los decoradores se aplican **de abajo hacia arriba** (el de abajo se ejecuta primero).
En este orden: primero se verifica el permiso, y si falla, `@login_required` lo intercepta y manda al login si no tiene sesión.

---

## Redirección al login en lugar de mostrar el 403

### Cuándo tiene sentido

| Escenario                                              | Qué hacer                               |
| ------------------------------------------------------ | --------------------------------------- |
| Sin sesión, llega a una vista protegida                | Redirigir al login con `?next=` ✅      |
| Con sesión, sin permiso                                | Mostrar 403 — el login no resuelve nada |
| Sistema simple sin permisos finos, solo login/no login | Siempre redirigir al login              |

### Opción A — Dejar que `@login_required` lo maneje (automático)

La forma más simple. No hay que hacer nada extra:

```python
# settings.py
LOGIN_URL = '/login/'   # ← @login_required redirige aquí si no hay sesión
```

```python
@login_required   # ← si no tiene sesión → /login/?next=/mi-vista/ automáticamente
def mi_vista(request):
    ...
```

### Opción B — Redirigir manualmente desde la vista

```python
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def panel(request):
    if not request.user.has_perm('app.view_reporte'):
        return redirect(f'/login/?next={request.path}')
        #                         ↑ ?next= guarda la URL actual
        #                           después del login, el usuario regresa aquí
    ...
```

### Opción C — Handler global para el 403 (nivel proyecto)

La opción más profesional: interceptar **todos** los 403 a nivel de proyecto y decidir el comportamiento según el estado de sesión:

```python
# mi_app/views.py
from django.shortcuts import redirect, render

def handler_403(request, exception):
    if not request.user.is_authenticated:
        # No tiene sesión → redirigir al login con ?next= para volver a donde estaba
        return redirect(f'/login/?next={request.path}')
    # Tiene sesión pero no tiene permiso → mostrar la página de error
    return render(request, '403.html', status=403)
```

```python
# urls.py del proyecto (raíz)
handler403 = 'mi_app.views.handler_403'
```

Este patrón es el más usado en proyectos profesionales:

- El usuario sin sesión nunca ve un "403 Forbidden" — ve el formulario de login.
- El usuario con sesión pero sin permiso recibe la página de error que le dice qué hacer.

---

## Probar el 403 en desarrollo

```python
# mi_app/views.py — solo para testing
from django.shortcuts import render

def test_403(request):
    return render(request, '403.html', status=403)
```

```python
# urls.py
path('test-403/', test_403),
```

---

---

# Parte III — Error 500

---

> _"El servidor encontró un error que no supo manejar. Siempre es un bug del código."_

---

## ¿Cuándo dispara Django un 500?

| Situación                                                    | Ejemplo                             |
| ------------------------------------------------------------ | ----------------------------------- |
| Una excepción no capturada en la vista                       | `AttributeError`, `TypeError`, etc. |
| Error en el template (variable que no existe en una DBquery) | `{{ objeto.metodo_que_no_existe }}` |
| La base de datos no responde                                 | `OperationalError` de psycopg2      |
| Cualquier `Exception` que Django no captura                  | Cualquier bug no manejado           |

El 500 **no se puede disparar intencionalmente** como el 404 o el 403 —
aparece cuando el código tiene un bug. Si el código funciona bien, los 500 no ocurren.

---

## Por qué el `500.html` es diferente

El `500.html` tiene una regla que no tienen el `404.html` ni el `403.html`:

> **No puede usar `{% extends 'base.html' %}` ni `{% url %}` ni variables de contexto.**

**¿Por qué?** El servidor está en un estado inestable. Si crasheó por un problema con la base de datos, intentar renderizar `base.html` (que puede tener consultas a la BD, `{{ user.username }}`, etc.) puede causar **otro error encima del primero** — y el usuario no ve nada.

El `500.html` debe ser **HTML puro y estático**:

```html
<!-- templates/500.html -->
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Error del servidor</title>
    <style>
      body {
        font-family: sans-serif;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        min-height: 100vh;
        margin: 0;
        background: #f8f9fa;
        text-align: center;
        padding: 1rem;
      }
      h1 {
        font-size: 5rem;
        color: #dc3545;
        margin: 0;
      }
      h2 {
        color: #343a40;
      }
      p {
        color: #6c757d;
      }
      a {
        display: inline-block;
        margin-top: 1rem;
        padding: 0.5rem 1.5rem;
        background: #0d6efd;
        color: #fff;
        border-radius: 0.375rem;
        text-decoration: none;
      }
    </style>
  </head>
  <body>
    <h1>500</h1>
    <h2>Error interno del servidor</h2>
    <p>Algo salió mal de nuestro lado. El equipo ya fue notificado.</p>
    <a href="/">Volver al inicio</a>
    <!-- ↑ se usa "/" directamente, no {% url 'home' %} — el motor de templates puede estar roto -->
  </body>
</html>
```

**Qué NO puede tener el 500.html:**

```
❌ {% extends 'base.html' %}
❌ {% url 'home' %}
❌ {{ user.username }}
❌ {% load static %}
❌ Cualquier tag o variable de Django
```

**Qué SÍ puede tener:**

```
✅ HTML puro
✅ CSS embebido (<style>)
✅ JavaScript puro
✅ href="/" directamente en el link
✅ Imagen embebida en base64 (si se quiere logo sin CDN)
```

---

## Manejador personalizado para el 500

```python
# mi_app/views.py
from django.shortcuts import render

def handler_500(request):
    # Importante: el handler del 500 NO recibe 'exception' como argumento
    # El servidor está en mal estado — no se puede confiar en ese objeto
    return render(request, '500.html', status=500)
```

```python
# urls.py del proyecto (raíz)
handler500 = 'mi_app.views.handler_500'
```

La firma del `handler_500` no tiene el argumento `exception` — a diferencia del 403 y el 404.
Esto es intencional: Django no pasa la excepción porque el servidor puede estar en un estado que la hace inaccesible.

---

## Notificar errores 500 al equipo

En producción, los 500 no deben pasar desapercibidos.
La forma más simple de recibir notificaciones por email es configurar `ADMINS` en `settings.py`:

```python
# settings.py
ADMINS = [
    ('Nombre Developer', 'developer@miempresa.com'),
]

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# ... configuración de email ...
```

Con `DEBUG = False` y `ADMINS` configurado, Django envía un email automáticamente
cada vez que ocurre un error 500 no capturado, incluyendo el stack trace completo.

---

---

# Resumen final

---

## Comparación entre los tres errores

| Característica                | 404                | 403                         | 500                   |
| ----------------------------- | ------------------ | --------------------------- | --------------------- |
| Hereda `base.html`            | ✅ Sí              | ✅ Sí                       | ❌ No — HTML puro     |
| Usa `{% url %}`               | ✅ Sí              | ✅ Sí                       | ❌ No                 |
| Variable especial de Django   | `{{ exception }}`  | `{{ exception }}`           | Ninguna               |
| Handler recibe `exception`    | ✅ Sí              | ✅ Sí                       | ❌ No                 |
| Se puede disparar manualmente | ✅ `raise Http404` | ✅ `raise PermissionDenied` | ❌ Solo pasa por bugs |
| Se puede redirigir al login   | No aplica          | ✅ Sí (ver Parte II)        | No aplica             |

---

## Definir los handlers — siempre en el `urls.py` raíz

```python
# proyecto/urls.py — el archivo que tiene los include() de todas las apps

handler400 = 'mi_app.views.handler_400'
handler403 = 'mi_app.views.handler_403'
handler404 = 'mi_app.views.handler_404'
handler500 = 'mi_app.views.handler_500'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mi_app.urls')),
    ...
]
```

Sin definir estas variables, Django usa los manejadores por defecto
(que solo buscan el template correspondiente y lo renderizan sin lógica extra).

---

## Checklist de producción

```
[ ] 1. Crear templates/404.html   — puede usar {% extends 'base.html' %}
[ ] 2. Crear templates/403.html   — puede usar {% extends 'base.html' %}
[ ] 3. Crear templates/500.html   — HTML puro, sin Django templates
[ ] 4. DIRS configurado en TEMPLATES en settings.py
[ ] 5. DEBUG = False en producción
[ ] 6. ALLOWED_HOSTS con el dominio real
[ ] 7. handler403 con lógica de redirección al login si no hay sesión
[ ] 8. ADMINS configurado para recibir emails en caso de 500
```

---

## Flujo completo

```
Request entra al servidor
        ↓
¿La URL coincide con algún patrón?
        │
        ├── NO  ──────────────────────────────────────────→ 404 (tu 404.html)
        │
        └── SÍ  → ejecuta la vista
                        │
                        ├── raise Http404 ──────────────→ 404 (tu 404.html)
                        │
                        ├── raise PermissionDenied ─────→ 403 (tu handler_403)
                        │          ↓
                        │   ¿tiene sesión?
                        │     NO  → redirect /login/?next=
                        │     SÍ  → mostrar 403.html
                        │
                        ├── excepción no capturada ──────→ 500 (tu 500.html, HTML puro)
                        │
                        └── respuesta OK ──────────────→ 200 ✅

En desarrollo (DEBUG=True): Django ignora tus templates y muestra páginas propias.
En producción (DEBUG=False): tus templates toman el control.
```

---

> _"En producción, el usuario nunca debería ver el stack trace de Python.
> Esa información es para el developer — y vía logs, no vía el navegador."_

---
