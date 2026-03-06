# Práctica 10: Creando un Sistema de Componentes Frontend en Django

## Objetivo de la práctica

Poner en práctica los conceptos vistos de **CSS Variables (Tokens)**, **diseño Mobile-First 100% responsivo**, y **encapsulación de componentes (Partials)** utilizando las herramientas nativas de Django 6.

Aprenderás a transicionar de un "código HTML espagueti repetido" al orden del Atomic Design dentro de Django.

---

## El Escenario

Te han contratado refactorizar la vista principal ("Dashboard") de una aplicación académica. Actualmente, el desarrollador anterior repitió toda la estructura HTML de "Tarjeta de Curso" repetidamente, dificultando cualquier cambio de diseño.

Además, te pidieron implementar los "Brand Guidelines" (tokens de diseño) de la institución universitaria y garantizar que se vea perfecto desde un smartphone vertical hasta un Smart TV universitario.

---

## Tarea 1: Definiendo los Tokens del Sistema

1. En tu proyecto Django, asegúrate de tener configurado `STATICFILES_DIRS`.
2. Crea el archivo base para tus tokens en `static/css/variables.css`.
3. Ingresa la paleta oficial (en formato HSL para facilidad de manipulación de texturas y sombras):

```css
/* static/css/variables.css */
:root {
  /* Paleta HSL */
  --clr-brand: 220 90% 56%; /* Azul Institucional */
  --clr-brand-dark: 220 90% 40%;

  --clr-surface: 0 0% 100%; /* Blanco */
  --clr-text-main: 220 20% 15%; /* Casi negro oscuro */
  --clr-text-muted: 220 10% 40%; /* Gris plomizo */

  --clr-danger: 0 85% 60%;

  /* Tipografía fluida (asumiendo body de 16px) */
  --font-sans: "Inter", system-ui, sans-serif;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-xl: 1.5rem;

  /* Espaciados Universales */
  --space-2: 0.5rem; /* 8px */
  --space-4: 1rem; /* 16px */
  --space-6: 1.5rem; /* 24px */
  --space-8: 2rem; /* 32px */

  /* Bordes y sombras */
  --radius-md: 12px;
  --shadow-soft: 0 4px 20px hsl(var(--clr-text-main) / 0.08);
}
```

---

## Tarea 2: Abrazando el Mobile-First

Vas a crear la cuadrícula donde se mostrarán los cursos.
Crea o edita `static/css/layout.css`. Debes estructurarlo estrictamente con enfoque de desarrollo "Móvil Primero" extendiéndose a Smart TVs.

Copia, pega y analiza el siguiente CSS.

```css
/* static/css/layout.css */
/* 1. Base Móvil (Siempre en columna, padding contenido) */
.course-grid {
  display: flex;
  flex-direction: column;
  gap: var(--space-4);
  padding: var(--space-4);
}

/* 2. Tablet (2 columnas) */
@media (min-width: 768px) {
  .course-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: var(--space-6);
    padding: var(--space-6);
  }
}

/* 3. Laptops / PC (3 o 4 columnas) */
@media (min-width: 1024px) {
  .course-grid {
    grid-template-columns: repeat(3, 1fr);
    max-width: 1280px;
    margin: 0 auto; /* Centramos en pantallas gigantes */
  }
}

/* 4. Pantallas Ultra-Anchadas (TVs o monitores gamers) */
@media (min-width: 1600px) {
  .course-grid {
    grid-template-columns: repeat(4, 1fr);
    max-width: 1800px;
    /* Las tarjetas no se estirarán infinitamente gracias al max-width */
  }
}
```

---

## Tarea 3: Creación de Partials (Atomic Design)

Tenemos el siguiente monstruo espagueti repetido múltiples veces en nuestro actual archivo `dashboard.html`. Es difícil de leer y de mantener.

```html
<!-- VIEJO DASHBOARD ESPAGUETI -->
<div
  class="course-card"
  style="border: 1px solid #ddd; background: #fff; border-radius: 12px; padding: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);"
>
  <h3 style="color: #1a202c; font-size: 1.25rem; margin-top: 0;">
    Física Cuántica
  </h3>
  <p style="color: #4a5568; font-size: 0.875rem;">Prof. Erwin Schrödinger</p>
  <div style="margin-top: 16px;">
    <span
      style="background: #e2e8f0; padding: 4px 8px; border-radius: 4px; font-size: 0.75rem;"
      >Avanzado</span
    >
  </div>
  <button
    style="margin-top: 16px; width: 100%; padding: 8px; background: #3182ce; color: white; border: none; border-radius: 6px; cursor: pointer;"
  >
    Ingresar al Aula
  </button>
</div>
```

**Tu Misión:**

### A) Crea la Molécula de la Tarjeta (El componente reutilizable)

Crea una nueva carpeta en tus templates llamada `components/` y dentro crea un archivo llamado `molecule_course_card.html`. (Esa es la convención moderna).

Limpiaremos los estilos en línea y los reemplazaremos por nuestras propias clases que leen de nuestras Variables CSS (Tokens).

```html
<!-- templates/components/molecule_course_card.html -->
<article class="c-course-card">
  <h3 class="c-course-title">{{ title }}</h3>
  <p class="c-course-teacher">Prof. {{ teacher }}</p>

  <div class="c-course-tags">
    <span class="c-tag">{{ level }}</span>
  </div>

  <!-- Aquí anidamos otro componente interno "Átomo" de botón -->
  {% include 'components/atom_button.html' with text="Ingresar al Aula"
  btn_type="primary" full_width=True %}
</article>
```

### B) Crea el Átomo del Botón

Crea ahora `templates/components/atom_button.html`.

```html
<!-- templates/components/atom_button.html -->
<button
  class="c-btn c-btn-{{ btn_type|default:'primary' }} {% if full_width %}c-btn-full{% endif %}"
>
  {{ text }}
</button>
```

### C) Limpia el Dashboard principal

Ahora vuelve a tu `dashboard.html`. Con todo encapsulado, un ciclo `FOR` y etiquetas `include`, tu template principal debe verse inmensamente más limpio:

```html
<!-- templates/dashboard.html -->
{% extends 'base.html' %} {% block content %}
<main>
  <h1>Tus Cursos Asignados</h1>

  <!-- Llamamos a nuestra grilla responsive de Tarea 2 -->
  <div class="course-grid">
    {% for course in cursos %}

    <!-- Invocamos al Partial (Componente) pasándole el contexto de la base de datos -->
    {% include 'components/molecule_course_card.html' with title=course.nombre
    teacher=course.profesor_asignado level=course.dificultad %} {% empty %}
    <p>No tienes cursos inscritos por el momento.</p>
    {% endfor %}
  </div>
</main>
{% endblock %}
```

---

## Conclusión y Entrega Final

Has logrado:

1. Declarar tus fuentes puras de diseño (Variables CSS).
2. Crear un sistema sólido de grillas que adapta el contenido independientemente del dispositivo (CSS Mobile-First a Smart TV).
3. Transicionar código HTML quemado (hardcoded), eliminando por absoluto los "styles" CSS embebidos directo a la etiqueta HTML, migrándolos hacia componentes nativos reutilizables de Django.

¡Comparte capturas de pantalla de los elementos adaptados a dispositivos móviles y grandes televisores (haz zoom alejado en tu navegador) a tu instructor!
