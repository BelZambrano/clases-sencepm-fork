# 🚨 Nuevo Ticket — Cambio de Requisito

# 🔴🟢🔵 Sistema de Agendamiento: Laboratorio del Profesor Oak

---

> ⚠️ **ATENCIÓN:** Este documento se entrega a los **45 minutos** de iniciado el challenge. No antes.

---

## TICKET 8 — El Profesor Oak Cambió de Opinión

**Prioridad:** Alta

El Profesor Oak acaba de comunicar lo siguiente:

> _"Necesito que cada reserva tenga un campo `mensaje_entrenador` donde el entrenador pueda escribir un mensaje opcional (por ejemplo: 'Estoy muy emocionado por conocer a Charmander'). También necesito un campo `confirmada` (booleano) que yo pueda marcar desde el Admin cuando confirme la cita."_

---

## Lo que debes hacer

1. Agregar los dos campos nuevos al modelo de Reserva.
2. Generar la nueva migración con `makemigrations`.
3. Aplicarla con `migrate`.
4. Verificar con `showmigrations` que todo esté en `[X]`.
5. Agregar el campo de mensaje al formulario de confirmación (Paso 3).
6. Que el campo `confirmada` sea visible y editable desde el Admin.

---

## Criterio de aceptación

- La migración se genera y aplica **sin errores ni pérdida de datos**.
- El campo `mensaje_entrenador` aparece en el formulario del Paso 3.
- El campo `confirmada` es editable desde `/admin/`.
- Los registros que ya existían antes de la migración siguen intactos.

---

## ¿Por qué este ticket?

En el mundo real, los requisitos cambian todo el tiempo. Un desarrollador profesional debe poder:

- Agregar campos a modelos que ya tienen datos sin romper nada.
- Generar migraciones incrementales de forma segura.
- Adaptar la interfaz rápidamente a cambios de último minuto.

Este ticket evalúa exactamente eso.

---
