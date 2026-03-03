# neutralize.py — Guía de uso

## Qué hace

Normaliza el lenguaje de archivos Markdown: convierte conjugaciones y modismos del español rioplatense (Argentina/Uruguay) a español latinoamericano neutro y formal.

Ejemplos de lo que corrige automáticamente:

| Antes (voseo / regional) | Después (neutro) |
| ------------------------ | ---------------- |
| `tenés`                  | `tienes`         |
| `hacé`                   | `haz`            |
| `mirá`                   | `mira`           |
| `acá`                    | `aquí`           |
| `vos`                    | `tú`             |
| `a ver`                  | `veamos`         |
| `tipear`                 | `escribir`       |
| `asegurate`              | `asegúrate`      |

El script modifica el archivo directamente y reporta cuántos cambios realizó. Si no hay nada que corregir, lo indica sin modificar el archivo.

---

## Requisitos

- Python 3 instalado
- Ejecutar desde la raíz del repositorio (`clasepm/`)

```bash
# Verificar que Python3 está disponible
python3 --version
```

---

## Uso desde la terminal

### Un solo archivo

```bash
cd /home/ars/Escritorio/ariel_it/clasepm
python3 neutralize.py django_modulo_6/semana2/clase_6/teoria_clase_6b.md
```

### Múltiples archivos en el mismo comando

```bash
python3 neutralize.py archivo1.md archivo2.md archivo3.md
```

### Todos los `.md` de una carpeta (sin subcarpetas)

```bash
for f in django_modulo_6/semana2/clase_6/*.md; do python3 neutralize.py "$f"; done
```

### Todos los `.md` de una carpeta y sus subcarpetas

```bash
find django_modulo_6 -name "*.md" | xargs -I{} python3 neutralize.py {}
```

### Todos los `.md` del repositorio completo

```bash
find . -name "*.md" | xargs -I{} python3 neutralize.py {}
```

---

## Ejemplos de salida

```
✅ Modificado (6 cambios): django_modulo_6/semana1/clase_1/practica_django.md
✔️  Sin cambios: django_modulo_6/semana1/clase_2/teoria_clase_2.md
✅ Modificado (1 cambios): django_modulo_6/semana1/clase_3/informe_orm_vs_sql.md
```

---

## Cuándo ejecutarlo

- **Siempre** al terminar de escribir o editar un archivo `.md`, sea nuevo o existente.
- Después de sesiones de dictado o escritura rápida donde es fácil que escapen regionalismos.
- Al procesar archivos generados por IA que puedan haber adoptado el registro del instructor.

---

## Desglose del comando masivo

```bash
find django_modulo_6 -name "*.md" | xargs -I{} python3 neutralize.py {}
```

| Segmento                   | Qué hace                                                |
| -------------------------- | ------------------------------------------------------- |
| `find django_modulo_6`     | Busca dentro de esa carpeta y todas las subcarpetas     |
| `-name "*.md"`             | Filtra solo archivos con extensión `.md`                |
| `\| xargs -I{}`            | Pasa cada resultado como argumento al siguiente comando |
| `python3 neutralize.py {}` | Ejecuta neutralize sobre cada archivo encontrado        |

---

## Ver los archivos que serían procesados (sin modificarlos)

```bash
find django_modulo_6 -name "*.md" | sort
```

---

## Procesar otro módulo

```bash
# SQL Módulo 5
find sql_modulo_5 -name "*.md" | xargs -I{} python3 neutralize.py {}

# Todo el repositorio
find . -name "*.md" -not -path "./.git/*" | xargs -I{} python3 neutralize.py {}
```
