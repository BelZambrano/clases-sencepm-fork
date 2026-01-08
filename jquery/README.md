# Demo jQuery — Eventos comunes (sitio completo)

## Resumen ejecutivo

Este proyecto es una página web educativa (una sola vista) diseñada para enseñar, de forma práctica y visual, los **eventos más comunes de jQuery** en un contexto realista: un “sitio largo” con navegación por secciones, componentes con Bootstrap y un **panel de Log** que registra cada interacción del alumno.

El objetivo es que el estudiante entienda:
- qué evento se dispara,
- en qué momento se dispara,
- y cómo se conecta con un caso de uso típico (formularios, UI, navegación, etc.).

La página funciona como material de **Clase 1–2** para introducir interacciones con DOM, eventos y buenas prácticas básicas (evitar recarga con `preventDefault`, habilitar botones por estado, etc.).

---

## Objetivo pedagógico (para clase)

- Practicar eventos frecuentes: `click`, `dblclick`, `mouseenter`, `mouseleave`, `keydown`, `keyup`, `keypress`, `change`, `submit`, `load`, `focus`, `blur`, `input`, `scroll`, `resize`.
- Aprender a leer el comportamiento de la UI mediante un **Log** centralizado.
- Asociar cada evento a una aplicación real: UX, formularios, navegación, interacción con teclado, etc.

---

## Alcance y funcionalidades

### 1) Navegación por secciones (menú superior fijo)
- Menú fijo con botones que hacen scroll suave a secciones.
- Usa `data-ir` para definir el destino del scroll.
- Ajusta el offset según altura del menú para evitar que la sección quede debajo.

**Eventos asociados:**
- `click` (botones del menú)
- `scroll` (interacción general con la página)

---

### 2) Módulos de demostración por evento

Cada sección incluye:
- explicación breve,
- ejemplo interactivo,
- resultado visible (alertas / mensajes),
- registro automático en el Log.

#### a) `click`
- Botón principal que cambia estado y texto de un mensaje.
- Botón “Reset” para volver al estado inicial.

#### b) `dblclick`
- Tarjeta que requiere doble clic como “confirmación”.

#### c) `mouseenter` / `mouseleave`
- Caja “hover” que se resalta con una leve escala y cambia mensajes al entrar/salir.

#### d) `keydown` / `keyup` / `keypress`
- Input con contadores por tipo de evento.
- Registra teclas presionadas (`e.key`) en el Log.
- Incluye nota pedagógica sobre `keypress` (evento más antiguo).

#### e) `change`
- `select` que actualiza un mensaje según la opción elegida.
- `checkbox` que:
  - actualiza estado visual,
  - y habilita/deshabilita el botón de envío del formulario (con `prop("disabled", ...)`).

#### f) `submit`
- Formulario que:
  - usa `preventDefault()` para evitar recarga,
  - valida nombre + email,
  - muestra mensaje de éxito sin recargar,
  - registra acción en el Log.

#### g) `load` (en imagen)
- Imagen embebida (SVG en Data URI) que dispara evento `load`.
- Al cargar, cambia el estado del mensaje a “cargada”.

#### h) Otros eventos extra
- `focus` / `blur`: muestra estado del input.
- `input`: vista previa en vivo del texto escrito.
- `scroll`: muestra botón “Arriba” con `fadeIn`/`fadeOut` al pasar cierta altura.
- `resize`: registra tamaño de ventana y actualiza mensaje.

---

## Componentes clave

### 1) Panel “Log”
El Log es el núcleo pedagógico: permite observar, en tiempo real, el disparo de eventos.

- Función `log(msg)`:
  - agrega timestamp,
  - usa `prepend` para mostrar primero el evento más reciente,
  - se renderiza en `#logBox`.

**Controles de log:**
- “Limpiar log”
- “Agregar ejemplo” (mensaje manual)

---

## Estructura técnica

### Dependencias (CDN)
- **Bootstrap 4.6.2** (solo CSS) para maquetación rápida.
- **jQuery 3.6.0** para eventos y manipulación DOM.

### Arquitectura
- Archivo HTML único (`.html`), autocontenido:
  - estilos en `<style>`,
  - lógica en `<script>`,
  - layout en HTML con secciones.

### Convenciones usadas
- Selectores por `id` para demos puntuales: `#btnClick`, `#dblBox`, etc.
- Clase `.js-ir` + atributo `data-ir` para navegación.
- Uso de `.on("evento", handler)` para asociar eventos.
- Uso de `.toggleClass`, `.prop`, `.text`, `.val`, `.css`, `.animate`, `.fadeIn`, `.fadeOut`.

---

## Cómo ejecutar

### Opción A: abrir localmente
1) anda a la carpeta `jquery` y busca el archivo `jquery_event.html`.
2) Ábrelo con el navegador.


