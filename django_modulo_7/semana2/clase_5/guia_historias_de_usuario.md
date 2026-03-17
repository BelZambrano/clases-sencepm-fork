# 📖 Guía Práctica: Cómo Crear Historias de Usuario

## De la idea de negocio al software funcional — sin necesidad de saber programar

---

## 🎯 ¿Qué vas a aprender?

Al terminar esta guía serás capaz de:

- Transformar una necesidad de negocio en requisitos claros para un equipo técnico
- Escribir historias de usuario profesionales que cualquier desarrollador pueda implementar
- Priorizar qué construir primero para obtener valor rápido
- Evitar los errores más comunes que causan software mal hecho

> **Dato:** Según el informe *Standish Group CHAOS Report (2020)*, el **66% de los proyectos de software fallan o tienen problemas graves**, y la causa #1 es la **mala comunicación de requisitos** entre el negocio y el equipo técnico.
>
> *Fuente: The Standish Group, "CHAOS Report", 2020.*

---

## 📌 Sección 1: ¿Qué es una Historia de Usuario?

Una **historia de usuario** es una descripción corta y simple de una funcionalidad contada **desde el punto de vista de la persona que la va a usar**.

### La fórmula mágica

```
COMO [tipo de usuario]
QUIERO [realizar una acción]
PARA [obtener un beneficio]
```

### Ejemplo real de negocio

Imagina que tienes una **pastelería ficticia llamada "Dulce Amanecer"** y quieres un sistema para gestionar pedidos:

```
COMO dueña de Dulce Amanecer
QUIERO ver todos los pedidos del día en una sola pantalla
PARA saber cuántos pasteles debo preparar antes de las 6 AM
```

### ¿Por qué esta fórmula funciona?

| Parte de la fórmula | ¿Qué le dice al equipo técnico? |
|---|---|
| **COMO** (tipo de usuario) | Para **quién** construimos esto |
| **QUIERO** (acción) | **Qué** debe hacer el software |
| **PARA** (beneficio) | **Por qué** es importante — esto guía las decisiones de diseño |

> **Dato:** Las organizaciones que usan historias de usuario tienen **un 30% más de probabilidad de entregar proyectos exitosos** comparadas con las que usan documentos extensos de requisitos.
>
> *Fuente: VersionOne, "State of Agile Report", 14th Edition, 2020.*

---

## 📌 Sección 2: Antes de Escribir — Identifica a tus Usuarios

Antes de escribir una sola historia, necesitas responder: **¿Quién va a usar tu software?**

### Paso 1: Lista todos los tipos de personas que interactúan con tu negocio

Siguiendo con nuestro ejemplo de **Dulce Amanecer**:

| Tipo de usuario | ¿Qué hace? | ¿Qué necesita del sistema? |
|---|---|---|
| 🧑‍🍳 **Pastelera principal** | Prepara los pedidos | Ver qué preparar y para cuándo |
| 📱 **Cliente** | Hace pedidos | Elegir productos, pagar, rastrear su pedido |
| 💼 **Administradora** (dueña) | Gestiona el negocio | Ver ventas, ganancias, inventario |
| 🚚 **Repartidor** | Entrega los pedidos | Ver dirección, confirmar entrega |
| 📞 **Recepcionista** | Recibe llamadas | Crear pedidos por teléfono rápidamente |

### Paso 2: Prioriza — ¿Quién es el usuario MÁS importante?

Ordénalos por impacto en tu negocio. Para **Dulce Amanecer**, la pastelera y los clientes son los más críticos: si ellos no pueden usar el sistema, no hay negocio.

> **Consejo de oro 💡:** No intentes construir para todos a la vez. Empieza con **1 o 2 tipos de usuario** y expande después.

---

## 📌 Sección 3: Cómo Escribir Historias de Usuario Paso a Paso

### Paso 1: Piensa en un problema real de tu negocio

❌ **No pienses en tecnología todavía.**

Pregúntate:
- ¿Qué me quita tiempo?
- ¿Dónde pierdo dinero?
- ¿Qué se me olvida frecuentemente?
- ¿De qué se quejan mis clientes?

**Ejemplo para Dulce Amanecer:**
> "A veces se me olvida un pedido y el cliente llega a recogerlo y no está listo. Eso me ha costado clientes."

---

### Paso 2: Convierte el problema en una historia de usuario

Toma ese problema y usa la fórmula:

```
COMO pastelera principal de Dulce Amanecer
QUIERO recibir una alerta automática 3 horas antes de la hora de entrega
PARA nunca olvidar preparar un pedido a tiempo
```

---

### Paso 3: Agrega los Criterios de Aceptación

Los **criterios de aceptación** son las condiciones que deben cumplirse para que la historia se considere **terminada**. Son como una lista de verificación.

```
HISTORIA: Alerta de pedidos próximos

COMO pastelera principal de Dulce Amanecer
QUIERO recibir una alerta automática 3 horas antes de la hora de entrega
PARA nunca olvidar preparar un pedido a tiempo

CRITERIOS DE ACEPTACIÓN:
✅ La alerta se muestra en pantalla y suena una notificación
✅ La alerta incluye: nombre del cliente, productos, cantidad y hora de entrega
✅ Si ya marqué el pedido como "en preparación", la alerta no se repite
✅ Puedo ver una lista de todas las alertas pendientes del día
```

> **Dato:** Los equipos que usan criterios de aceptación bien definidos reducen los **defectos en producción en un 40%** y los **retornos por malentendidos en un 60%**.
>
> *Fuente: Cohn, M. "User Stories Applied", Addison-Wesley, 2004.*

---

### Paso 4: Asigna un tamaño (sin ser técnico)

No necesitas saber cuántas horas toma programar algo. Usa la escala de **camisetas**:

| Talla | Significado | Ejemplo en Dulce Amanecer |
|---|---|---|
| **XS** | Muy simple, un cambio pequeño | Cambiar el logo de la página |
| **S** | Simple, pocas pantallas | Agregar un campo "notas especiales" al pedido |
| **M** | Mediano, requiere algo de lógica | Sistema de alertas de pedidos |
| **L** | Grande, varias pantallas y reglas | Módulo completo de inventario |
| **XL** | Muy grande, necesita dividirse | Sistema de delivery con rastreo GPS en tiempo real |

> **Regla importante ⚠️:** Si una historia es talla **L o XL**, DIVÍDELA en historias más pequeñas. Las historias grandes son difíciles de construir, probar y entregar.

---

## 📌 Sección 4: El Arte de Dividir Historias Grandes

### Ejemplo: Dividir una historia XL

**Historia original (demasiado grande):**
```
COMO administradora de Dulce Amanecer
QUIERO un sistema completo de inventario
PARA saber siempre qué ingredientes tengo disponibles
```

**Dividida en historias manejables:**

```
Historia 1 (S):
COMO administradora de Dulce Amanecer
QUIERO registrar los ingredientes que compro con su cantidad
PARA tener un inventario inicial

Historia 2 (S):
COMO administradora de Dulce Amanecer
QUIERO que al confirmar un pedido se descuenten automáticamente los ingredientes
PARA que el inventario se actualice solo

Historia 3 (M):
COMO administradora de Dulce Amanecer
QUIERO recibir una alerta cuando un ingrediente esté por debajo del mínimo
PARA comprar antes de quedarme sin stock

Historia 4 (S):
COMO administradora de Dulce Amanecer
QUIERO ver un reporte mensual de consumo de ingredientes
PARA negociar mejores precios con mis proveedores
```

### Técnica: La regla INVEST

Cada historia bien escrita debe cumplir con **INVEST**:

| Letra | Significado | ¿Qué significa para ti? |
|---|---|---|
| **I** | Independiente | Se puede construir sin depender de otras historias |
| **N** | Negociable | Se puede ajustar el alcance si es necesario |
| **V** | Valiosa | Le da valor real al usuario o al negocio |
| **E** | Estimable | El equipo puede calcular el esfuerzo necesario |
| **S** | Small (Pequeña) | Se puede completar en una semana o menos |
| **T** | Testeable | Se puede verificar que funciona correctamente |

> **Dato:** El acrónimo INVEST fue acuñado por **Bill Wake en 2003** y se ha convertido en el estándar de la industria para evaluar la calidad de las historias de usuario.
>
> *Fuente: Wake, B. "INVEST in Good Stories, and SMART Tasks", XP123.com, 2003.*

---

## 📌 Sección 5: Priorizando — ¿Qué Construir Primero?

### La Matriz de Valor vs. Esfuerzo

Clasifica cada historia en esta matriz:

```
         ALTO VALOR
              │
    ★ HACER   │  ⏰ PLANIFICAR
    PRIMERO   │  (vale la pena pero
              │   toma tiempo)
 ─────────────┼──────────────────
    🤔 LLENAR │  ❌ EVITAR
    ESPACIOS  │  (mucho esfuerzo,
    (si sobra  │   poco valor)
     tiempo)  │
              │
         BAJO VALOR

   POCO ESFUERZO ──── MUCHO ESFUERZO
```

### Ejemplo aplicado a Dulce Amanecer

| Historia | Valor | Esfuerzo | Clasificación |
|---|---|---|---|
| Ver pedidos del día | ⬆️ Alto | ⬇️ Bajo | ★ **HACER PRIMERO** |
| Alertas de pedidos | ⬆️ Alto | ➡️ Medio | ★ **HACER PRIMERO** |
| Inventario automático | ⬆️ Alto | ⬆️ Alto | ⏰ Planificar |
| Cambiar colores del sitio | ⬇️ Bajo | ⬇️ Bajo | 🤔 Si sobra tiempo |
| Rastreo GPS de delivery | ➡️ Medio | ⬆️ Alto | ❌ No es prioridad ahora |

> **Dato:** Según el **Principio de Pareto aplicado al software**, el **80% del valor de un producto lo genera el 20% de sus funcionalidades**. Priorizar correctamente es la diferencia entre un proyecto exitoso y uno que se queda sin presupuesto.
>
> *Fuente: Koch, R. "The 80/20 Principle", Currency Doubleday, 1998.*

---

## 📌 Sección 6: Errores Comunes que DEBES Evitar

### ❌ Error 1: Escribir soluciones técnicas, no necesidades

```
❌ MALO:
COMO administradora
QUIERO una base de datos PostgreSQL con una tabla de pedidos
PARA guardar la información

✅ BUENO:
COMO administradora
QUIERO guardar todos los pedidos con sus detalles
PARA poder consultarlos después si hay algún reclamo
```

**¿Por qué?** Tú describes **QUÉ** necesitas. El equipo técnico decide **CÓMO** construirlo.

---

### ❌ Error 2: Historias demasiado vagas

```
❌ MALO:
COMO cliente
QUIERO que el sistema sea fácil de usar
PARA estar contento

✅ BUENO:
COMO cliente de Dulce Amanecer
QUIERO buscar pasteles por categoría (cumpleaños, bodas, infantiles)
PARA encontrar rápidamente lo que necesito sin navegar todo el catálogo
```

---

### ❌ Error 3: Olvidar los criterios de aceptación

Sin criterios de aceptación, el equipo técnico tiene que **adivinar** qué quieres. Esto produce:

- 🔄 Reprocesos costosos
- 😤 Frustración en ambos lados
- 💸 Presupuesto desperdiciado

> **Dato:** El costo de corregir un error descubierto en producción es **100 veces mayor** que si se detecta en la fase de requisitos.
>
> *Fuente: Boehm, B. & Basili, V. "Software Defect Reduction Top 10 List", IEEE Computer, 2001.*

---

### ❌ Error 4: No priorizar

Si le dices al equipo "todo es urgente", nada es urgente. El resultado: un software que hace muchas cosas a medias y ninguna bien.

---

## 📌 Sección 7: Plantilla Lista para Usar

Copia esta plantilla cada vez que necesites crear una nueva historia:

```
═══════════════════════════════════════════════════
📋 HISTORIA DE USUARIO #[número]
═══════════════════════════════════════════════════

📌 Título: [nombre corto y descriptivo]

👤 COMO [tipo de usuario]
🎯 QUIERO [acción que quiero realizar]
💎 PARA [beneficio que obtengo]

📏 Tamaño: [ ] XS  [ ] S  [ ] M  [ ] L  [ ] XL

🏷️ Prioridad: [ ] Alta  [ ] Media  [ ] Baja

✅ CRITERIOS DE ACEPTACIÓN:
  □ [condición 1 que debe cumplirse]
  □ [condición 2 que debe cumplirse]
  □ [condición 3 que debe cumplirse]

📝 NOTAS ADICIONALES:
  [cualquier contexto, restricción o aclaración importante]

═══════════════════════════════════════════════════
```

---

## 📌 Sección 8: Caso Práctico Completo

### Contexto: "Floristería Virtual Pétalos de Luna" 🌸

Una floristería ficticia que quiere vender por internet. La dueña, Valentina, no sabe nada de tecnología pero sabe exactamente qué necesita su negocio.

### Las primeras 5 historias de Valentina:

---

**Historia #1 — Talla S — Prioridad Alta**
```
COMO clienta de Pétalos de Luna
QUIERO ver el catálogo de arreglos florales con fotos y precios
PARA elegir el arreglo que mejor se ajuste a mi presupuesto y ocasión

CRITERIOS DE ACEPTACIÓN:
✅ Cada arreglo muestra: foto, nombre, precio y descripción breve
✅ Puedo filtrar por ocasión: cumpleaños, aniversario, condolencias, amor
✅ Puedo filtrar por rango de precio
✅ Los arreglos agotados aparecen marcados como "no disponible"
```

---

**Historia #2 — Talla S — Prioridad Alta**
```
COMO clienta de Pétalos de Luna
QUIERO agregar arreglos a un carrito de compras
PARA pedir varios productos en una sola orden

CRITERIOS DE ACEPTACIÓN:
✅ Puedo ver cuántos productos tengo en el carrito en todo momento
✅ Puedo cambiar la cantidad o eliminar productos del carrito
✅ El carrito muestra el total actualizado automáticamente
✅ El carrito se mantiene aunque cierre la página y vuelva después
```

---

**Historia #3 — Talla M — Prioridad Alta**
```
COMO clienta de Pétalos de Luna
QUIERO pagar mi pedido con tarjeta de crédito o transferencia
PARA completar mi compra sin ir a la tienda física

CRITERIOS DE ACEPTACIÓN:
✅ Puedo elegir entre tarjeta de crédito, débito o transferencia bancaria
✅ Recibo un comprobante por correo electrónico inmediatamente
✅ Si el pago falla, el sistema me avisa claramente qué pasó
✅ Mi pedido no se confirma hasta que el pago sea exitoso
```

---

**Historia #4 — Talla S — Prioridad Alta**
```
COMO Valentina (dueña de Pétalos de Luna)
QUIERO recibir una notificación cada vez que entre un pedido nuevo
PARA preparar el arreglo lo antes posible

CRITERIOS DE ACEPTACIÓN:
✅ La notificación llega por correo electrónico y en la pantalla del sistema
✅ La notificación incluye: productos, dirección de entrega y hora solicitada
✅ Puedo marcar el pedido como "leído" para no confundirme
```

---

**Historia #5 — Talla M — Prioridad Media**
```
COMO Valentina (dueña de Pétalos de Luna)
QUIERO ver un resumen de ventas por semana y por mes
PARA saber cuáles son mis arreglos más vendidos y planificar mis compras de flores

CRITERIOS DE ACEPTACIÓN:
✅ El resumen muestra: total de ventas, cantidad de pedidos y ticket promedio
✅ Puedo ver qué arreglos se vendieron más
✅ Puedo comparar esta semana/mes con la anterior
✅ Puedo exportar el resumen como PDF
```

---

## 📌 Sección 9: Checklist Final — Antes de Entregar tus Historias al Equipo Técnico

Usa esta lista para verificar que tus historias están listas:

- [ ] ¿Cada historia tiene la fórmula COMO/QUIERO/PARA?
- [ ] ¿Los criterios de aceptación son específicos y verificables?
- [ ] ¿Las historias son independientes entre sí (se pueden construir en cualquier orden)?
- [ ] ¿Ninguna historia es talla L o XL sin dividir?
- [ ] ¿Define las prioridades (qué se construye primero)?
- [ ] ¿Evité mencionar tecnología específica en las historias?
- [ ] ¿Cada historia describe un beneficio real para el usuario o el negocio?
- [ ] ¿Revisé que no haya historias duplicadas o que se contradigan?

---

## 📌 Sección 10: Glosario para No-Técnicos

| Término | Significado en palabras simples |
|---|---|
| **Historia de usuario** | Una tarjeta que describe algo que el software debe hacer |
| **Criterio de aceptación** | La lista de "check" para saber si algo está terminado |
| **Sprint** | Un período corto (1-2 semanas) donde se construyen algunas historias |
| **Backlog** | La lista completa de todas las historias pendientes |
| **MVP** (Producto Mínimo Viable) | La primera versión del software con solo lo esencial |
| **Deploy** | Poner el software disponible para que los usuarios lo usen |
| **Bug** | Un error en el software que hace que algo no funcione bien |
| **Feedback** | Opinión del usuario sobre lo que se construyó, para mejorarlo |
| **Stakeholder** | Cualquier persona interesada en el proyecto (dueño, usuario, inversor) |
| **Product Owner** | La persona del lado del negocio que decide qué se construye |

> **Dato:** El rol de **Product Owner** fue formalizado por **Ken Schwaber y Jeff Sutherland** en el marco de trabajo **Scrum (1995)**, y hoy es usado por el **81% de los equipos ágiles** en el mundo.
>
> *Fuente: Digital.ai, "State of Agile Report", 16th Edition, 2022.*

---

## 🎓 Resumen Visual del Proceso Completo

```
┌─────────────────┐
│  1. IDENTIFICA   │
│  tus usuarios    │
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  2. LISTA los    │
│  problemas de    │
│  tu negocio      │
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  3. ESCRIBE      │
│  historias con   │
│  COMO/QUIERO/    │
│  PARA            │
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  4. AGREGA       │
│  criterios de    │
│  aceptación      │
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  5. ASIGNA       │
│  tamaño y        │
│  prioridad       │
└───────┬─────────┘
        │
        ▼
┌─────────────────┐
│  6. DIVIDE       │
│  las historias    │
│  grandes         │
└───────┬─────────┘
        │
        ▼
┌─────────────────────┐
│  7. ENTREGA al       │
│  equipo técnico      │
│  y revisa juntos     │
└──────────────────────┘
```

---

## 📚 Fuentes y Lecturas Recomendadas

1. **Cohn, M.** (2004). *User Stories Applied: For Agile Software Development*. Addison-Wesley.
2. **Wake, B.** (2003). *INVEST in Good Stories, and SMART Tasks*. XP123.com.
3. **Schwaber, K. & Sutherland, J.** (2020). *The Scrum Guide*. Scrum.org.
4. **The Standish Group.** (2020). *CHAOS Report*.
5. **Digital.ai.** (2022). *State of Agile Report*, 16th Edition.
6. **Boehm, B. & Basili, V.** (2001). *Software Defect Reduction Top 10 List*. IEEE Computer.
7. **Koch, R.** (1998). *The 80/20 Principle*. Currency Doubleday.

---

> 💡 **Recuerda:** No necesitas saber programar para crear excelentes historias de usuario. Solo necesitas **conocer tu negocio** y **comunicar claramente lo que necesitas**. El equipo técnico se encarga del cómo; tú te encargas del qué y el por qué.
