# 📖 SQL — Consultas sobre texto de blog

> Si tenés una tabla `blog` con una columna de tipo `TEXT` que guarda el contenido de cada post,
> podés hacer consultas **dentro de ese texto** usando funciones de texto de PostgreSQL.

---

## Tabla de ejemplo

```sql
CREATE TABLE blog (
  id        SERIAL PRIMARY KEY,
  titulo    VARCHAR(200),
  contenido TEXT
);
```

---

## 1. Buscar posts que contengan una palabra

```sql
SELECT titulo
FROM blog
WHERE contenido ILIKE '%javascript%';
```

| Código           | Qué significa                                    |
| ---------------- | ------------------------------------------------ |
| `SELECT titulo`  | "Traeme la columna titulo"                       |
| `FROM blog`      | "De la tabla blog"                               |
| `WHERE`          | "Solo los que cumplan esta condición"            |
| `contenido`      | "La columna donde está el texto del post"        |
| `ILIKE`          | "Contiene este texto" (ignora mayúsculas)        |
| `'%javascript%'` | `%` es comodín: "cualquier cosa antes y después" |

---

## 2. Extraer un resumen (primeros 200 caracteres)

```sql
SELECT titulo,
       LEFT(contenido, 200) AS resumen
FROM blog;
```

| Código                 | Qué significa                                    |
| ---------------------- | ------------------------------------------------ |
| `LEFT(contenido, 200)` | "Tomá los primeros 200 caracteres del contenido" |
| `AS resumen`           | "Llamá a ese resultado 'resumen'"                |

---

## 3. Contar cuántas veces aparece una palabra en el texto

```sql
SELECT titulo,
       (LENGTH(contenido) - LENGTH(REPLACE(contenido, 'SQL', ''))) / 3 AS veces_sql
FROM blog;
```

| Código                        | Qué significa                                                  |
| ----------------------------- | -------------------------------------------------------------- |
| `LENGTH(contenido)`           | "Longitud total del texto (en caracteres)"                     |
| `REPLACE(contenido,'SQL','')` | "Copia del texto con todas las apariciones de 'SQL' borradas"  |
| `LENGTH(...) - LENGTH(...)`   | "La diferencia = cuántos caracteres sacamos = 3 × apariciones" |
| `/ 3`                         | "Dividido por 3 porque 'SQL' tiene 3 letras"                   |
| `AS veces_sql`                | "Llama al resultado 'veces_sql'"                               |

---

## 4. Buscar posts que contengan varias palabras a la vez

```sql
SELECT titulo
FROM blog
WHERE contenido ILIKE '%base de datos%'
  AND contenido ILIKE '%seguridad%';
```

| Código                    | Qué significa                                     |
| ------------------------- | ------------------------------------------------- |
| `ILIKE '%base de datos%'` | "El texto debe contener la frase 'base de datos'" |
| `AND`                     | "Y además..."                                     |
| `ILIKE '%seguridad%'`     | "...también debe contener la palabra 'seguridad'" |

> Solo devuelve posts que tengan **ambas** cosas. Si querés que tenga una **u otra**, usás `OR`.

---

## 5. Full-Text Search — búsqueda inteligente por relevancia

```sql
SELECT titulo
FROM blog
WHERE to_tsvector('spanish', contenido) @@ to_tsquery('spanish', 'inyeccion');
```

| Código                               | Qué significa                                           |
| ------------------------------------ | ------------------------------------------------------- |
| `to_tsvector('spanish', contenido)`  | "Convertí el texto en un índice de palabras en español" |
| `'spanish'`                          | "Usá las reglas del idioma español"                     |
| `@@`                                 | "Contiene / coincide con..."                            |
| `to_tsquery('spanish', 'inyeccion')` | "...la búsqueda de la palabra 'inyeccion' en español"   |

---

## ¿Cuándo usar cada uno?

| Técnica         | Cuándo usarla                            | Velocidad                  |
| --------------- | ---------------------------------------- | -------------------------- |
| `ILIKE`         | Búsquedas simples, textos cortos         | 🐢 Lenta en tablas grandes |
| `REPLACE`       | Contar apariciones de una palabra exacta | 🐢 Lenta en tablas grandes |
| `AND` + `ILIKE` | Buscar varias palabras obligatorias      | 🐢 Lenta en tablas grandes |
| `to_tsvector`   | Búsqueda por relevancia en textos largos | ⚡ Rápida con índice       |

> **Full-Text Search** (`to_tsvector`) es lo más potente: ignora artículos ("el", "la", "de"),
> maneja plurales/singulares, y con un índice es **mucho más rápido** en tablas grandes.
> Es lo que usan plataformas como WordPress y sistemas de búsqueda similares por dentro.
