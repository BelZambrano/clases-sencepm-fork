<!-- =========================================================
Archivo: resumen_unidad_completo.md
Tema: Última Clase SQL — Resumen + Triggers + SQL Injection
========================================================= -->

# 📋 Última Clase SQL — Resumen de la Unidad + Triggers + SQL Injection

> **Objetivo:** Cerrar la unidad con un resumen general, profundizar en Triggers
> y aprender sobre SQL Injection (seguridad).

---

## 📖 Tabla de Contenidos

1. [Mapa General de la Unidad](#mapa-general-de-la-unidad)
2. [Resumen: Todo lo que vimos](#resumen-todo-lo-que-vimos)
3. [Triggers — Automatización en la Base de Datos](#triggers--automatización-en-la-base-de-datos)
4. [SQL Injection — Seguridad](#sql-injection--seguridad)

---

---

# Mapa General de la Unidad

```
 📐 DISEÑO                    🏗️ ESTRUCTURA               📊 DATOS
 ──────────                   ──────────────               ────────
 ER Modelo                    DDL (CREATE, ALTER, DROP)    DML (INSERT, UPDATE, DELETE)
 Normalización (1NF→3NF)      Tipos de datos               SELECT (WHERE, ORDER BY, LIMIT)
 Entidades/Relaciones         Constraints (PK, FK, etc.)   JOIN (INNER, LEFT, RIGHT, FULL)
                                                           GROUP BY / HAVING
                                                           Subconsultas

 ⚡ MUNDO REAL                🛡️ SEGURIDAD                🤖 AUTOMATIZACIÓN
 ──────────                   ──────────                   ──────────────────
 NULL y sus trampas           SQL Injection                Triggers
 Índices / Performance        Prepared Statements          Funciones (PL/pgSQL)
 Problema N+1                 Mínimo Privilegio            Procedimientos Almacenados
 CASE WHEN / CTE              ORM / WAF                    Auditoría automática
```

---

---

# Resumen: Todo lo que vimos

## DDL — Lenguaje de Definición de Datos (Estructura)

| Comando        | ¿Qué hace?                             |
| -------------- | -------------------------------------- |
| `CREATE TABLE` | Crea una tabla nueva                   |
| `ALTER TABLE`  | Modifica una tabla existente           |
| `DROP TABLE`   | Elimina una tabla completa             |
| `TRUNCATE`     | Vacía todas las filas (la tabla sigue) |

## DML — Lenguaje de Manipulación de Datos

| Comando  | ¿Qué hace?                              |
| -------- | --------------------------------------- |
| `INSERT` | Agrega filas nuevas a una tabla         |
| `UPDATE` | Modifica valores de filas existentes    |
| `DELETE` | Elimina filas de una tabla              |
| `SELECT` | Consulta y lee datos (no modifica nada) |

## Tipos de Datos

| Tipo           | ¿Qué guarda?                    | Ejemplo               |
| -------------- | ------------------------------- | --------------------- |
| `INT`          | Números enteros                 | 42, 100, -5           |
| `NUMERIC(p,s)` | Decimales exactos (para dinero) | 29990.50              |
| `VARCHAR(n)`   | Texto de largo variable         | 'María López'         |
| `TEXT`         | Texto largo                     | Descripciones         |
| `DATE`         | Fecha                           | '2026-02-20'          |
| `TIMESTAMPTZ`  | Fecha y hora                    | '2026-02-20 14:30:00' |
| `BOOLEAN`      | Verdadero o falso               | TRUE / FALSE          |
| `SERIAL`       | ID autoincremental              | 1, 2, 3, ...          |

## Restricciones (Constraints)

| Restricción   | ¿Qué hace?                          |
| ------------- | ----------------------------------- |
| `PRIMARY KEY` | Identifica cada fila de forma única |
| `FOREIGN KEY` | Enlace a otra tabla                 |
| `NOT NULL`    | Campo obligatorio                   |
| `UNIQUE`      | No permite valores repetidos        |
| `DEFAULT`     | Valor automático si no se da uno    |
| `CHECK`       | Valida una condición personalizada  |

## Consultas (SELECT)

| Cláusula   | ¿Qué hace?                                |
| ---------- | ----------------------------------------- |
| `WHERE`    | Filtra filas por condición                |
| `ORDER BY` | Ordena resultados (ASC / DESC)            |
| `LIMIT`    | Limita cantidad de resultados             |
| `DISTINCT` | Elimina duplicados                        |
| `AS`       | Alias (nombre temporal)                   |
| `GROUP BY` | Agrupa filas para funciones de agregación |
| `HAVING`   | Filtra después de agrupar                 |
| `JOIN`     | Combina datos de varias tablas            |

## Funciones de Agregación

| Función   | ¿Qué hace?    |
| --------- | ------------- |
| `COUNT()` | Contar filas  |
| `SUM()`   | Sumar valores |
| `AVG()`   | Promedio      |
| `MIN()`   | Valor mínimo  |
| `MAX()`   | Valor máximo  |

## Tipos de JOIN

| JOIN         | ¿Qué devuelve?                                  |
| ------------ | ----------------------------------------------- |
| `INNER JOIN` | Solo filas con coincidencia en ambas tablas     |
| `LEFT JOIN`  | Todo de la izquierda + coincidencias de la otra |
| `RIGHT JOIN` | Todo de la derecha + coincidencias de la otra   |
| `FULL JOIN`  | Todo de ambas tablas                            |

## Modelo ER (Entidad-Relación)

| Tipo de Relación | Lectura             | En SQL...                   |
| ---------------- | ------------------- | --------------------------- |
| 1:1              | Uno tiene uno       | FK en cualquiera de las dos |
| 1:N              | Uno tiene muchos ⭐ | FK en la tabla del lado N   |
| N:M              | Muchos con muchos   | Tabla intermedia con 2 FKs  |

## Principios de transacciones (ACID)

| Principio        | Significado                               |
| ---------------- | ----------------------------------------- |
| **A**tomicidad   | Todo o nada                               |
| **C**onsistencia | De estado válido a otro estado válido     |
| **I**solamiento  | Las transacciones no se molestan entre sí |
| **D**urabilidad  | Una vez confirmado, es permanente         |

---

---

---

# Triggers — Automatización en la Base de Datos

---

## ¿Qué es un Trigger?

Un **Trigger** es código que se ejecuta **solo, automáticamente**, cuando alguien hace
un INSERT, UPDATE o DELETE en una tabla.

> Tú no lo llamas. Se dispara solo.

**Ejemplo del mundo real:**

- Sin trigger: cada vez que alguien compra, un empleado anota la venta a mano.
- Con trigger: la venta se registra **sola** cada vez que alguien compra.

---

## ¿Dónde se programa un trigger?

Los triggers se programan **directamente en la base de datos**, no en tu aplicación (no en Python, Java ni JavaScript).

```
┌────────────────────────────┐
│   Tu aplicación            │    ← Tu código (Python, Java, JS, etc.)
│   (frontend / backend)     │
└────────────┬───────────────┘
             │ Se conecta a...
             ▼
┌────────────────────────────┐
│   Servidor de Base de Datos│    ← PostgreSQL, MySQL, etc.
│   (local o remoto/nube)    │
│                            │
│   AQUÍ VIVEN LOS TRIGGERS  │    ← El trigger se guarda y ejecuta AQUÍ
│   Se ejecutan DENTRO de    │
│   la base de datos.        │
└────────────────────────────┘
```

**¿Se pueden usar en servidores remotos?** Sí. Los triggers funcionan en:

| Lugar                             | Ejemplo                            |
| --------------------------------- | ---------------------------------- |
| Tu computadora local              | PostgreSQL instalado en tu PC      |
| Un servidor en la nube            | AWS RDS, Google Cloud SQL, Azure   |
| Una plataforma como Supabase      | Supabase usa PostgreSQL por debajo |
| Cualquier servidor con PostgreSQL | Un servidor de tu empresa          |

> El trigger vive **dentro de la base de datos**, sin importar dónde esté esa base de datos. Cuando alguien hace un INSERT, UPDATE o DELETE, el trigger se dispara automáticamente **en el servidor donde esté la BD**.

---

## ¿Cuándo se ejecuta?

| Momento  | Significado                                 | ¿Cuándo usarlo?                            |
| -------- | ------------------------------------------- | ------------------------------------------ |
| `BEFORE` | Se ejecuta **antes** de guardar el cambio   | Cuando quieres **cambiar o validar** datos |
| `AFTER`  | Se ejecuta **después** de guardar el cambio | Cuando quieres **registrar o reaccionar**  |

---

## NEW y OLD

Dentro de un trigger hay dos variables especiales para acceder a los datos:

| Variable | Qué contiene                     | Disponible en   |
| -------- | -------------------------------- | --------------- |
| `NEW`    | La fila **nueva** (lo que viene) | INSERT y UPDATE |
| `OLD`    | La fila **vieja** (lo que había) | UPDATE y DELETE |

```sql
NEW.precio   -- el precio NUEVO (el que se quiere guardar)
OLD.precio   -- el precio VIEJO (el que había antes)
NEW.nombre   -- el nombre que se está insertando
OLD.nombre   -- el nombre que se está borrando
```

### Resumen: ¿Cuándo existe cada variable?

| Evento | `OLD`        | `NEW`        |
| ------ | ------------ | ------------ |
| INSERT | ❌ No existe | ✅ Sí existe |
| UPDATE | ✅ Sí existe | ✅ Sí existe |
| DELETE | ✅ Sí existe | ❌ No existe |

> **¿Qué significa ❌ y ✅ aquí?**
>
> - ✅ = **la variable EXISTE** y la puedes usar en tu código.
> - ❌ = **la variable NO EXISTE** porque no tiene sentido.
>
> **¿Por qué?**
>
> - En un **INSERT** no hay fila vieja (estás creando una nueva), entonces `OLD` no existe.
> - En un **DELETE** no hay fila nueva (estás borrando), entonces `NEW` no existe.
> - En un **UPDATE** sí hay ambas: la vieja (`OLD`) y la nueva (`NEW`).
>
> ❌ **no significa que se elimina algo**, significa que la variable **no está disponible** para usar.

---

## Las dos piezas de un Trigger

En PostgreSQL necesitas **dos cosas**:

1. Una **función** → el código (qué hacer).
2. Un **trigger** → la regla (cuándo ejecutar la función).

```
FUNCIÓN (el código)  ←──  TRIGGER (la regla que la conecta a la tabla)
```

---

## ⚙️ Tablas para practicar

> **Copia y ejecuta este bloque ANTES de probar los ejemplos.**

```sql
DROP TABLE IF EXISTS auditoria CASCADE;
DROP TABLE IF EXISTS ventas CASCADE;
DROP TABLE IF EXISTS productos CASCADE;
DROP TABLE IF EXISTS empleados CASCADE;
DROP TABLE IF EXISTS log_salarios CASCADE;
DROP TABLE IF EXISTS cuentas CASCADE;
DROP TABLE IF EXISTS movimientos CASCADE;

CREATE TABLE productos (
  id          SERIAL PRIMARY KEY,
  nombre      VARCHAR(100) NOT NULL,
  precio      NUMERIC(10,2) NOT NULL,
  stock       INT DEFAULT 0,
  updated_at  TIMESTAMP DEFAULT NOW()
);

CREATE TABLE ventas (
  id            SERIAL PRIMARY KEY,
  id_producto   INT REFERENCES productos(id),
  cantidad      INT NOT NULL,
  total         NUMERIC(12,2),
  fecha         TIMESTAMP DEFAULT NOW()
);

CREATE TABLE auditoria (
  id          SERIAL PRIMARY KEY,
  tabla       VARCHAR(50),
  operacion   VARCHAR(10),
  detalle     TEXT,
  usuario     VARCHAR(100) DEFAULT CURRENT_USER,
  fecha       TIMESTAMP DEFAULT NOW()
);

CREATE TABLE empleados (
  id        SERIAL PRIMARY KEY,
  nombre    VARCHAR(100) NOT NULL,
  salario   NUMERIC(10,2) NOT NULL
);

CREATE TABLE log_salarios (
  id            SERIAL PRIMARY KEY,
  id_empleado   INT,
  salario_antes NUMERIC(10,2),
  salario_nuevo NUMERIC(10,2),
  fecha         TIMESTAMP DEFAULT NOW()
);

CREATE TABLE cuentas (
  id     SERIAL PRIMARY KEY,
  dueno  VARCHAR(100) NOT NULL,
  saldo  NUMERIC(12,2) DEFAULT 0
);

CREATE TABLE movimientos (
  id         SERIAL PRIMARY KEY,
  id_origen  INT,
  id_destino INT,
  monto      NUMERIC(12,2),
  fecha      TIMESTAMP DEFAULT NOW()
);

INSERT INTO productos (nombre, precio, stock) VALUES
  ('Laptop',   900000, 10),
  ('Monitor',  250000, 20),
  ('Teclado',   45000, 50);

INSERT INTO empleados (nombre, salario) VALUES
  ('Lucía',  850000),
  ('Andrés', 720000);

INSERT INTO cuentas (dueno, saldo) VALUES
  ('Ana',   500000),
  ('Pedro', 300000);
```

---

---

## Pieza 1: La función — Palabra por palabra

```sql
CREATE OR REPLACE FUNCTION fn_ejemplo()
RETURNS TRIGGER AS $$
BEGIN
  -- aquí va tu código
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

| Código             | Qué significa                                                       |
| ------------------ | ------------------------------------------------------------------- |
| `CREATE`           | "Quiero crear algo nuevo"                                           |
| `OR REPLACE`       | "Si ya existe, reemplázala"                                         |
| `FUNCTION`         | "Lo que estoy creando es una función"                               |
| `fn_ejemplo()`     | El nombre que le doy (los `()` están vacíos porque no recibe datos) |
| `RETURNS TRIGGER`  | "Esta función es para ser usada por un trigger"                     |
| `AS $$`            | "Aquí empieza el código" (ver explicación de `$$` abajo)            |
| `BEGIN`            | "Inicio del bloque de código"                                       |
| `RETURN NEW;`      | "Devuelve la fila nueva para que la operación continúe"             |
| `END;`             | "Fin del bloque de código"                                          |
| `$$`               | "Aquí termina el código" (cierra el `$$` de arriba)                 |
| `LANGUAGE plpgsql` | "El lenguaje usado es PL/pgSQL" (el lenguaje de PostgreSQL)         |

### ¿Qué son los `$$`?

Los `$$` son **delimitadores de texto** en PostgreSQL. Funcionan como las comillas, pero para bloques grandes de código.

```
Comillas normales:   'texto simple'
Dólar-dólar:         $$ bloque de código largo $$
```

**¿Por qué no usar comillas simples `'...'`?**

Porque dentro del código del trigger vas a usar comillas simples para textos (como `'productos'` o `'INSERT'`). Si usaras comillas para delimitar TODO el bloque, se confundiría:

```sql
-- ❌ PROBLEMA: las comillas internas chocan con las externas
CREATE FUNCTION ... AS '
  INSERT INTO auditoria VALUES ('productos');  -- ← ¡ERROR! PostgreSQL no sabe
';                                             --   dónde termina qué

-- ✅ SOLUCIÓN: $$ no choca con las comillas internas
CREATE FUNCTION ... AS $$
  INSERT INTO auditoria VALUES ('productos');  -- ← Sin problema
$$;
```

> **Pensalo así:** `$$` es como un "abre llaves" `{` y "cierra llaves" `}` pero para SQL.
> El primer `$$` = abre. El segundo `$$` = cierra.

### ¿Qué retornar?

| Situación              | Qué poner      | Efecto                    |
| ---------------------- | -------------- | ------------------------- |
| BEFORE INSERT o UPDATE | `RETURN NEW;`  | Permite la operación      |
| BEFORE DELETE          | `RETURN OLD;`  | Permite el borrado        |
| AFTER (cualquiera)     | `RETURN NULL;` | Se ignora (ya se ejecutó) |
| Cancelar la operación  | `RETURN NULL;` | En BEFORE: cancela todo   |

---

## Pieza 2: El trigger — Palabra por palabra

```sql
CREATE TRIGGER trg_ejemplo
BEFORE UPDATE ON productos
FOR EACH ROW
EXECUTE FUNCTION fn_ejemplo();
```

| Código             | Qué significa                                     |
| ------------------ | ------------------------------------------------- |
| `CREATE TRIGGER`   | "Quiero crear un trigger"                         |
| `trg_ejemplo`      | El nombre que le doy al trigger                   |
| `BEFORE`           | "Ejecutar ANTES de la operación"                  |
| `UPDATE`           | "Cuando alguien haga un UPDATE"                   |
| `ON productos`     | "En la tabla productos"                           |
| `FOR EACH ROW`     | "Ejecutar una vez POR CADA FILA que se modifique" |
| `EXECUTE FUNCTION` | "La función que debe ejecutar es..."              |
| `fn_ejemplo()`     | El nombre de la función creada antes              |

> Esas dos piezas juntas forman el trigger completo.

---

---

## Ejemplo 1 — Actualizar fecha automáticamente

**Problema:** quiero que cada vez que modifique un producto, la columna `updated_at`
se actualice sola con la fecha y hora actual.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_poner_fecha()
RETURNS TRIGGER AS $$
BEGIN
  NEW.updated_at = NOW();
  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra:**

| Código           | Qué significa                                                    |
| ---------------- | ---------------------------------------------------------------- |
| `NEW.updated_at` | "En la fila que se está modificando, toma la columna updated_at" |
| `= NOW()`        | "Ponle la fecha y hora actual"                                   |
| `RETURN NEW;`    | "Devuelve la fila con el cambio para que se guarde"              |

### El trigger:

```sql
CREATE TRIGGER trg_fecha_producto
BEFORE UPDATE ON productos
FOR EACH ROW
EXECUTE FUNCTION fn_poner_fecha();
```

**Frase completa:** "Antes de cada UPDATE en la tabla productos, por cada fila, ejecuta fn_poner_fecha."

> **¿Qué pasaría?** Si alguien hace `UPDATE productos SET precio = 950000 WHERE id = 1;`, el trigger automáticamente pone la fecha actual en `updated_at` antes de guardar. El programador no necesita hacerlo.

---

## Ejemplo 2 — Calcular el total de una venta

**Problema:** al vender, quiero que `total = precio × cantidad` se calcule solo.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_calcular_total()
RETURNS TRIGGER AS $$
DECLARE
  v_precio NUMERIC;
BEGIN
  SELECT precio INTO v_precio
  FROM productos
  WHERE id = NEW.id_producto;

  NEW.total = v_precio * NEW.cantidad;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra:**

| Código                       | Qué significa                                          |
| ---------------------------- | ------------------------------------------------------ |
| `DECLARE`                    | "Voy a crear variables para usar después"              |
| `v_precio NUMERIC;`          | "Creo una variable llamada v_precio, de tipo número"   |
| `SELECT precio`              | "Busca el valor de la columna precio"                  |
| `INTO v_precio`              | "Y guárdalo dentro de mi variable v_precio"            |
| `FROM productos`             | "Desde la tabla productos"                             |
| `WHERE id = NEW.id_producto` | "Donde el id coincida con el producto de esta venta"   |
| `NEW.total`                  | "En la venta que se está insertando, la columna total" |
| `= v_precio * NEW.cantidad`  | "Ponle el resultado de precio × cantidad"              |
| `RETURN NEW;`                | "Devuelve la fila con el total ya calculado"           |

### El trigger:

```sql
CREATE TRIGGER trg_total_venta
BEFORE INSERT ON ventas
FOR EACH ROW
EXECUTE FUNCTION fn_calcular_total();
```

**Frase completa:** "Antes de cada INSERT en ventas, por cada fila, ejecuta fn_calcular_total."

> **¿Qué pasaría?** Al hacer `INSERT INTO ventas (id_producto, cantidad) VALUES (1, 3);` (sin poner total), el trigger busca el precio de la Laptop (900,000), lo multiplica por 3 y pone total = 2,700,000 automáticamente.

---

## Ejemplo 3 — Descontar stock al vender

**Problema:** cuando se registra una venta, restar la cantidad del stock.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_descontar_stock()
RETURNS TRIGGER AS $$
BEGIN
  UPDATE productos
  SET stock = stock - NEW.cantidad
  WHERE id = NEW.id_producto;

  RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra:**

| Código                             | Qué significa                                        |
| ---------------------------------- | ---------------------------------------------------- |
| `UPDATE productos`                 | "Quiero modificar la tabla productos"                |
| `SET stock = stock - NEW.cantidad` | "Al stock actual, réstale la cantidad que se vendió" |
| `WHERE id = NEW.id_producto`       | "Solo al producto que se vendió"                     |
| `RETURN NULL;`                     | "Es un AFTER, el retorno se ignora"                  |

### El trigger:

```sql
CREATE TRIGGER trg_stock_venta
AFTER INSERT ON ventas
FOR EACH ROW
EXECUTE FUNCTION fn_descontar_stock();
```

**Frase completa:** "Después de cada INSERT en ventas, por cada fila, ejecuta fn_descontar_stock."

> **¿Qué pasaría?** Si la Laptop tiene stock = 10 y alguien inserta una venta de 3 unidades, el trigger automáticamente hace 10 - 3 = 7 en el stock. Sin que nadie lo haga manualmente.

---

## Ejemplo 4 — Registrar auditoría

**Problema:** quiero guardar un registro cada vez que alguien inserte, modifique o borre un producto.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_auditoria()
RETURNS TRIGGER AS $$
BEGIN
  IF TG_OP = 'INSERT' THEN
    INSERT INTO auditoria (tabla, operacion, detalle)
    VALUES ('productos', 'INSERT', 'Nuevo: ' || NEW.nombre);
    RETURN NEW;

  ELSIF TG_OP = 'UPDATE' THEN
    INSERT INTO auditoria (tabla, operacion, detalle)
    VALUES ('productos', 'UPDATE',
            'Cambió ' || OLD.nombre || ' → ' || NEW.nombre);
    RETURN NEW;

  ELSIF TG_OP = 'DELETE' THEN
    INSERT INTO auditoria (tabla, operacion, detalle)
    VALUES ('productos', 'DELETE', 'Borrado: ' || OLD.nombre);
    RETURN OLD;
  END IF;

  RETURN NULL;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra (lo nuevo):**

| Código                    | Qué significa                                                |
| ------------------------- | ------------------------------------------------------------ |
| `TG_OP`                   | Variable especial. Contiene qué operación disparó el trigger |
| `= 'INSERT'`              | "¿La operación fue un INSERT?"                               |
| `IF ... THEN`             | "Si se cumple esto, entonces haz lo siguiente"               |
| `ELSIF ... THEN`          | "Si no, pero si se cumple esto otro, haz lo siguiente"       |
| `END IF;`                 | "Fin de las condiciones"                                     |
| `OLD.nombre`              | "El nombre que tenía ANTES del cambio"                       |
| `NEW.nombre`              | "El nombre que tiene DESPUÉS del cambio"                     |
| <code>&#124;&#124;</code> | Operador para **unir textos** (como un `+` de cadenas)       |

### El trigger:

```sql
CREATE TRIGGER trg_auditoria_productos
AFTER INSERT OR UPDATE OR DELETE ON productos
FOR EACH ROW
EXECUTE FUNCTION fn_auditoria();
```

**Palabra por palabra:**

| Código                       | Qué significa                                 |
| ---------------------------- | --------------------------------------------- |
| `AFTER`                      | "Después de la operación"                     |
| `INSERT OR UPDATE OR DELETE` | "Cuando alguien haga INSERT, UPDATE O DELETE" |
| `ON productos`               | "En la tabla productos"                       |

> **¿Qué pasaría?** Cada vez que alguien inserte, modifique o borre un producto, queda un registro en la tabla `auditoria` con qué se hizo, quién y cuándo. Como una cámara de seguridad en la base de datos.

---

## Ejemplo 5 — Guardar historial de salarios

**Problema:** cada vez que cambien el salario de un empleado, guardar cuánto ganaba antes y cuánto gana ahora.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_log_salario()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.salario IS DISTINCT FROM NEW.salario THEN
    INSERT INTO log_salarios (id_empleado, salario_antes, salario_nuevo)
    VALUES (NEW.id, OLD.salario, NEW.salario);
  END IF;

  RETURN NEW;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra:**

| Código                                     | Qué significa                              |
| ------------------------------------------ | ------------------------------------------ |
| `OLD.salario IS DISTINCT FROM NEW.salario` | "¿El salario viejo es DIFERENTE al nuevo?" |
| `IF ... THEN`                              | "Si sí cambió, entonces haz esto"          |
| `OLD.salario`                              | "Lo que ganaba antes"                      |
| `NEW.salario`                              | "Lo que va a ganar ahora"                  |

> `IS DISTINCT FROM` es como `!=` pero funciona correctamente con `NULL`.

### El trigger:

```sql
CREATE TRIGGER trg_log_salario
AFTER UPDATE ON empleados
FOR EACH ROW
EXECUTE FUNCTION fn_log_salario();
```

> **¿Qué pasaría?** Si Lucía ganaba $850,000 y le suben el sueldo a $900,000, el trigger automáticamente guarda: "Lucía: antes 850,000 → ahora 900,000" en la tabla de log.

---

## Ejemplo 6 — Impedir un borrado

**Problema:** no quiero que nadie pueda borrar productos que tengan stock mayor a 0.

### La función:

```sql
CREATE OR REPLACE FUNCTION fn_proteger_producto()
RETURNS TRIGGER AS $$
BEGIN
  IF OLD.stock > 0 THEN
    RAISE EXCEPTION 'No puedes borrar "%" porque tiene % unidades en stock',
      OLD.nombre, OLD.stock;
  END IF;

  RETURN OLD;
END;
$$ LANGUAGE plpgsql;
```

**Palabra por palabra:**

| Código                  | Qué significa                                             |
| ----------------------- | --------------------------------------------------------- |
| `IF OLD.stock > 0 THEN` | "Si el producto que quieren borrar tiene stock mayor a 0" |
| `RAISE EXCEPTION`       | "Lanza un error y CANCELA la operación"                   |
| `'No puedes borrar...'` | Mensaje de error que verá el usuario                      |
| `%`                     | Se reemplaza por el valor que viene después de la coma    |
| `OLD.nombre, OLD.stock` | Los valores que reemplazan a los `%`                      |
| `RETURN OLD;`           | "Si pasó la validación (stock = 0), permite el borrado"   |

### El trigger:

```sql
CREATE TRIGGER trg_proteger_producto
BEFORE DELETE ON productos
FOR EACH ROW
EXECUTE FUNCTION fn_proteger_producto();
```

> Es `BEFORE` porque necesitamos poder **cancelar** la operación.

> **¿Qué pasaría?** Si alguien intenta `DELETE FROM productos WHERE nombre = 'Laptop'` y la Laptop tiene stock = 10, el trigger lanza un error: "No puedes borrar Laptop porque tiene 10 unidades en stock" y **cancela** el borrado.

---

---

## Procedimientos vs Funciones

| Aspecto              | PROCEDURE          | FUNCTION             |
| -------------------- | ------------------ | -------------------- |
| ¿Retorna valor?      | ❌ No              | ✅ Sí                |
| ¿Cómo se llama?      | `CALL sp_nombre()` | `SELECT fn_nombre()` |
| ¿Se usa en SELECT?   | ❌ No              | ✅ Sí                |
| ¿Se usa en triggers? | ❌ No              | ✅ Sí                |

### Procedimiento — Palabra por palabra

```sql
CREATE OR REPLACE PROCEDURE sp_transferir(
  p_origen  INT,
  p_destino INT,
  p_monto   NUMERIC
)
LANGUAGE plpgsql AS $$
BEGIN
  UPDATE cuentas SET saldo = saldo - p_monto WHERE id = p_origen;
  UPDATE cuentas SET saldo = saldo + p_monto WHERE id = p_destino;

  INSERT INTO movimientos (id_origen, id_destino, monto)
  VALUES (p_origen, p_destino, p_monto);
END;
$$;
```

| Código                        | Qué significa                                        |
| ----------------------------- | ---------------------------------------------------- |
| `CREATE OR REPLACE PROCEDURE` | "Crear (o reemplazar) un procedimiento"              |
| `sp_transferir`               | El nombre (`sp_` = stored procedure)                 |
| `p_origen INT`                | Parámetro: el ID de la cuenta origen (número entero) |
| `p_destino INT`               | Parámetro: el ID de la cuenta destino                |
| `p_monto NUMERIC`             | Parámetro: cuánta plata transferir                   |
| `LANGUAGE plpgsql AS $$`      | "El código está en PL/pgSQL, comienza aquí"          |
| `saldo = saldo - p_monto`     | "Al saldo de la cuenta origen, réstale el monto"     |
| `WHERE id = p_origen`         | "Solo a la cuenta de origen"                         |
| `saldo = saldo + p_monto`     | "Al saldo de la cuenta destino, súmale el monto"     |

### Llamar al procedimiento — Palabra por palabra

```sql
CALL sp_transferir(1, 2, 100000);
```

| Código          | Qué significa                |
| --------------- | ---------------------------- |
| `CALL`          | "Ejecuta este procedimiento" |
| `sp_transferir` | El nombre del procedimiento  |
| `1`             | p_origen = cuenta 1 (Ana)    |
| `2`             | p_destino = cuenta 2 (Pedro) |
| `100000`        | p_monto = $100,000           |

> **¿Qué pasaría?** `CALL sp_transferir(1, 2, 100000)` le resta $100,000 a Ana (cuenta 1) y se los suma a Pedro (cuenta 2), y además registra el movimiento. Todo en un solo comando.

---

## Función (retorna valor) — Palabra por palabra

```sql
CREATE OR REPLACE FUNCTION fn_saldo_total()
RETURNS NUMERIC AS $$
DECLARE
  v_total NUMERIC;
BEGIN
  SELECT SUM(saldo) INTO v_total FROM cuentas;
  RETURN v_total;
END;
$$ LANGUAGE plpgsql;
```

| Código                     | Qué significa                                       |
| -------------------------- | --------------------------------------------------- |
| `RETURNS NUMERIC`          | "Esta función devuelve un número" (no dice TRIGGER) |
| `DECLARE v_total NUMERIC;` | "Creo una variable llamada v_total"                 |
| `SUM(saldo)`               | "La suma de todos los saldos"                       |
| `INTO v_total`             | "Guarda esa suma dentro de mi variable"             |
| `RETURN v_total;`          | "Devuelve el resultado"                             |

### Llamar la función:

```sql
SELECT fn_saldo_total();
-- Resultado: 800000

-- Se puede usar dentro de consultas
SELECT dueno, saldo,
       ROUND(saldo / fn_saldo_total() * 100, 1) AS porcentaje
FROM cuentas;
```

---

## Administrar Triggers

```sql
-- Desactivar un trigger
ALTER TABLE productos DISABLE TRIGGER trg_auditoria_productos;

-- Desactivar TODOS los triggers de una tabla
ALTER TABLE productos DISABLE TRIGGER ALL;

-- Reactivar
ALTER TABLE productos ENABLE TRIGGER trg_auditoria_productos;
ALTER TABLE productos ENABLE TRIGGER ALL;

-- Borrar el trigger (la función queda)
DROP TRIGGER trg_auditoria_productos ON productos;

-- Borrar la función también
DROP FUNCTION fn_auditoria();

-- Ver triggers existentes
SELECT trigger_name, event_manipulation, event_object_table
FROM information_schema.triggers
ORDER BY event_object_table;
```

| Código            | Qué significa                      |
| ----------------- | ---------------------------------- |
| `ALTER TABLE`     | "Quiero modificar la tabla"        |
| `DISABLE TRIGGER` | "Desactivar este trigger"          |
| `ENABLE TRIGGER`  | "Reactivar este trigger"           |
| `ALL`             | "Todos los triggers de esta tabla" |

> 💡 Útil para **cargas masivas**: desactivas, cargas miles de filas, reactivas.

---

## Errores comunes con Triggers

| Error                                | Causa                                  | Solución                          |
| ------------------------------------ | -------------------------------------- | --------------------------------- |
| `function does not return a trigger` | Falta `RETURNS TRIGGER`                | Agregar `RETURNS TRIGGER`         |
| `record "new" is not assigned`       | Usas `NEW` en un DELETE                | Usar `OLD` en DELETE              |
| `record "old" is not assigned`       | Usas `OLD` en un INSERT                | Usar `NEW` en INSERT              |
| El trigger no se dispara             | Está desactivado                       | `ENABLE TRIGGER`                  |
| Loop infinito                        | Trigger A modifica tabla que dispara A | Agregar condición o desactivar    |
| `RETURN NULL` en BEFORE              | Cancela la operación sin error         | Poner `RETURN NEW` o `RETURN OLD` |

---

## Resumen: ¿Cuándo usar cada cosa?

| Quiero...                            | Usar                       |
| ------------------------------------ | -------------------------- |
| Reaccionar automáticamente a cambios | **Trigger**                |
| Ejecutar código cuando yo decida     | **Procedimiento** (`CALL`) |
| Obtener un valor calculado           | **Función** (`SELECT`)     |
| Validar datos antes de guardar       | **Trigger BEFORE**         |
| Registrar cambios en un log          | **Trigger AFTER**          |

---

## Diccionario de Triggers

| Término            | Qué es                                             |
| ------------------ | -------------------------------------------------- |
| `TRIGGER`          | Código que se ejecuta solo al modificar datos      |
| `BEFORE`           | Antes de guardar                                   |
| `AFTER`            | Después de guardar                                 |
| `FOR EACH ROW`     | Se ejecuta por cada fila afectada                  |
| `NEW`              | La fila nueva (INSERT/UPDATE)                      |
| `OLD`              | La fila vieja (UPDATE/DELETE)                      |
| `TG_OP`            | Variable: dice si fue INSERT, UPDATE o DELETE      |
| `RAISE EXCEPTION`  | Lanza un error y cancela todo                      |
| `RETURN NEW`       | Permite la operación                               |
| `RETURN NULL`      | En BEFORE: cancela. En AFTER: se ignora            |
| `FUNCTION`         | Código que retorna un valor. Se llama con `SELECT` |
| `PROCEDURE`        | Código sin retorno. Se llama con `CALL`            |
| `DECLARE`          | Crear variables dentro de una función              |
| `INTO`             | Guardar resultado de SELECT en una variable        |
| `IS DISTINCT FROM` | Comparar valores (funciona bien con NULL)          |
| `PL/pgSQL`         | El lenguaje de programación de PostgreSQL          |

---

---

---

# SQL Injection — Seguridad

> **Nota para el estudiante:** Esta sección está escrita para que la entienda **cualquier persona**, incluso si nunca has programado. No necesitas saber código para entender por qué SQL Injection es tan peligroso y cómo se protegen las empresas.

---

## 🗺️ ¿Dónde puede un atacante escribir SQL malicioso?

Cualquier lugar donde una aplicación te pida escribir algo y esos datos lleguen a una base de datos, es un punto de ataque potencial. Aquí van los más comunes:

| Lugar de ataque                | ¿Por qué es vulnerable?                                                                                                      |
| ------------------------------ | ---------------------------------------------------------------------------------------------------------------------------- |
| 📝 **Formulario de login**     | Los campos de usuario y contraseña se usan para armar una consulta SQL. Si el código los pega directo, se puede inyectar.    |
| 🔍 **Barra de búsqueda**       | Cuando buscas "zapatos", el texto viaja al servidor y se mete en un SQL. Un atacante escribe código SQL en vez de "zapatos". |
| 🌐 **La URL del navegador**    | Muchas URLs contienen parámetros (ej: `tienda.com/producto?id=5`). Un atacante cambia el `5` por código SQL malicioso.       |
| 📋 **Formularios de contacto** | Si el mensaje que escribes se graba en una base de datos con SQL, un atacante puede colar órdenes dentro del mensaje.        |
| 📱 **Apps móviles**            | Las apps del celular envían datos al servidor. Si ese servidor usa SQL sin protección, es igual de vulnerable.               |
| 💬 **Campos de comentarios**   | Cualquier caja de texto donde puedas escribir y que se guarde en una base de datos es un punto de entrada potencial.         |

> **Regla simple para recordar:** Si puedes **escribir texto** y ese texto **se guarda o se busca** en algún sistema → ese campo puede ser un punto de ataque si el programador no lo protegió.

---

---

## 🏠 Primero: ¿Cómo funciona una aplicación web por dentro?

Antes de hablar de ataques, necesitas entender cómo funciona una app por dentro. Imagina que una aplicación web (como un banco online, una tienda o Instagram) funciona como un **restaurante**:

```
┌─────────────────────────────────────────────────────┐
│  👤 EL CLIENTE (Tú, el usuario)                      │
│  Llegas al restaurante y le dices al mesero:         │
│  "Quiero ver el menú de pizzas"                      │
└────────────────────┬────────────────────────────────┘
                     │ Le hablas al mesero
                     ▼
┌─────────────────────────────────────────────────────┐
│  🧑‍🍳 EL MESERO (El código de la aplicación)          │
│  Escucha tu pedido y va a la cocina a buscarlo.      │
│  Le dice al cocinero: "Dame todas las pizzas"        │
│                                                      │
│  ⚠️ EL PROBLEMA ESTÁ AQUÍ                            │
│  Si el mesero repite TEXTUALMENTE todo lo que         │
│  el cliente dice sin pensar, se mete en problemas.   │
└────────────────────┬────────────────────────────────┘
                     │ Lleva el pedido a la cocina
                     ▼
┌─────────────────────────────────────────────────────┐
│  📦 LA COCINA (La base de datos)                     │
│  Recibe la orden del mesero y la ejecuta.            │
│  La cocina NO sabe si la orden es legítima o no.     │
│  Simplemente HACE lo que le dicen.                   │
└─────────────────────────────────────────────────────┘
```

> **La base de datos (la cocina) es obediente.** Ella no piensa, no juzga. Si le llega una orden, la ejecuta. El problema NO está en la cocina. **El problema está en el mesero** (el código) que no verifica lo que el cliente realmente dijo.

---

---

## 🔓 ¿Qué es SQL Injection?

**SQL Injection** (abreviado **SQLi**) es un truco que usa un atacante para **colar órdenes maliciosas** a través de los campos de texto de una aplicación (formularios de login, barras de búsqueda, URLs) y hacer que la base de datos las ejecute como si fueran órdenes legítimas.

### La Analogía del Restaurante 🍕

**Situación normal (sin ataque):**

```
Cliente dice: "Quiero la pizza Margarita"
Mesero va a la cocina y dice: "Dame la pizza llamada 'Margarita'"
La cocina busca la pizza Margarita y la entrega → ✅ Todo bien
```

**Situación con SQL Injection (ataque):**

```
Cliente dice: "Quiero la pizza Margarita,
              Y TAMBIÉN DAME TODO EL DINERO DE LA CAJA REGISTRADORA"

Mesero va a la cocina y dice TEXTUALMENTE:
  "Dame la pizza llamada 'Margarita',
   Y TAMBIÉN DAME TODO EL DINERO DE LA CAJA REGISTRADORA"

La cocina, que es obediente, ejecuta AMBAS órdenes:
  1. Busca la pizza Margarita ✅
  2. Entrega todo el dinero de la caja ☠️
```

**¿Por qué funcionó el ataque?** Porque el mesero (el código del programador) **repitió textualmente** lo que el cliente dijo, sin verificar ni separar el pedido real de las instrucciones extra que el atacante coló.

---

---

## 🎯 ¿Cómo se ve esto en la vida real?

### El Formulario de Login (La Puerta del Banco)

Imagina la pantalla de login de tu banco online:

```
┌─────────────────────────────────┐
│         Bienvenido              │
│                                 │
│  Usuario:  [_______________]    │
│  Clave:    [_______________]    │
│                                 │
│         [ Entrar ]              │
└─────────────────────────────────┘
```

**Uso normal:**
Un usuario legítimo escribe `ariel` en el campo de usuario y `miClave123` en la contraseña.

Internamente, el mesero (el código) arma esta "orden para la cocina" (consulta SQL):

```sql
SELECT * FROM usuarios WHERE nombre = 'ariel' AND clave = 'miClave123'
```

La cocina (base de datos) busca: _"¿Existe alguien que se llame 'ariel' Y tenga la clave 'miClave123'?"_

- Si existe → le da acceso ✅
- Si no existe → acceso denegado ❌

**Hasta aquí todo es normal y seguro.**

---

### El Ataque: ¿Qué escribe un atacante?

En vez de escribir un nombre de usuario normal, el atacante escribe esto en el campo de usuario:

```
' OR '1'='1
```

Sí, eso. Esas comillas, esos caracteres raros. Parece basura, pero es un arma.

**¿Qué pasa internamente?** El mesero (código) toma lo que el usuario escribió y lo pega directamente en la orden de la cocina:

```
ANTES (lo que el programador esperaba):
  SELECT * FROM usuarios WHERE nombre = 'ariel' AND clave = '...'

DESPUÉS DE LA INYECCIÓN (lo que realmente se envió a la cocina):
  SELECT * FROM usuarios WHERE nombre = '' OR '1'='1' AND clave = '...'
```

**Analicemos esta orden manipulada, paso a paso, como si fuera español:**

| Parte de la orden | ¿Qué significa?                                     |
| ----------------- | --------------------------------------------------- |
| `nombre = ''`     | "¿El nombre es vacío?" → **No, es falso**           |
| `OR`              | "**O** (basta que una condición sea verdadera)..."  |
| `'1'='1'`         | "¿1 es igual a 1?" → **¡Sí! Siempre es verdadero!** |

**Resultado:** Como `1=1` siempre es verdadero, toda la condición se convierte en verdadera. La cocina devuelve **TODOS los usuarios de la tabla**. El sistema toma el primero (normalmente el administrador) y le da acceso total al atacante.

> **El atacante entró al banco como administrador sin conocer la contraseña.** Solo escribió unos caracteres raros en el campo de texto.

---

---

## 💣 ¿Qué más puede hacer un atacante?

El ejemplo del login es solo la puerta de entrada. Una vez que un atacante descubre que una aplicación es vulnerable, puede hacer cosas mucho peores:

### 1. 📋 Robar TODA la información

Imagina buscar un producto en una tienda online. El atacante inyecta código en la barra de búsqueda para que la cocina, además de buscar productos, **también entregue la lista completa de usuarios con sus contraseñas**.

```
Lo que el atacante escribe en la barra de búsqueda:

  Televisor' UNION SELECT nombre, clave FROM usuarios --

Lo que la cocina ejecuta:
  1. Busca "Televisor" en productos (normal)
  2. UNION = "además, combina con..."
  3. Busca TODOS los nombres y claves de la tabla usuarios ☠️
  4. -- = "ignora todo lo que viene después" (oculta el truco)
```

**Resultado:** La página que debía mostrar televisores ahora muestra los nombres y contraseñas de todos los usuarios del sistema.

---

### 2. 🗑️ BORRAR tablas enteras

```
Lo que el atacante escribe en cualquier campo de texto:

  '; DROP TABLE usuarios; --

Lo que la cocina ejecuta:
  1. Termina la consulta original (el punto y coma)
  2. DROP TABLE usuarios = "ELIMINA la tabla de usuarios COMPLETA" ☠️
  3. -- = ignora el resto
```

> Imagina que eso le pasa a un banco. **Todos los registros de clientes, desaparecidos.** No hay login, no hay cuentas, no hay historial.

---

### 3. ✏️ Modificar datos a su antojo

```
Lo que el atacante escribe:

  '; UPDATE productos SET precio = 1; --

Lo que la cocina ejecuta:
  1. Termina la consulta anterior
  2. Cambia el precio de TODOS los productos a $1 ☠️
```

**Resultado:** Todos los productos de la tienda ahora cuestan $1. El atacante o compra un computador por $1 o simplemente sabotea el negocio.

---

### 4. 👑 Darse permisos de administrador

```
Lo que el atacante escribe:

  '; UPDATE usuarios SET rol = 'admin' WHERE nombre = 'hacker'; --

Resultado: El atacante ahora tiene permisos de administrador en el sistema.
```

---

### Resumen de daños posibles

| Tipo de daño           | Impacto real                                       |
| ---------------------- | -------------------------------------------------- |
| 🔓 Saltear el login    | Entrar como admin sin contraseña                   |
| 📋 Robar datos         | Extraer usuarios, contraseñas, tarjetas de crédito |
| 🗑️ Borrar tablas       | Eliminar toda la información del sistema           |
| ✏️ Modificar datos     | Cambiar precios, notas, roles, saldos bancarios    |
| 👑 Escalar privilegios | Darse permisos de administrador                    |

> **Dato real:** SQL Injection ha sido la vulnerabilidad **#1 más peligrosa del mundo** según OWASP (la organización mundial de seguridad web) durante más de una década. Es responsable de filtraciones masivas de datos en empresas como Yahoo, LinkedIn y Sony.

---

---

## 🧩 Los "Trucos" que usa el atacante (Para que los reconozcas)

El atacante no inventa nada nuevo. Usa los mismos comandos SQL que nosotros ya aprendimos, pero los combina con unos caracteres especiales para "escaparse" del campo de texto y hablarle directamente a la cocina:

| Truco              | ¿Qué hace?                                                | Ejemplo                |
| ------------------ | --------------------------------------------------------- | ---------------------- |
| `'` (comilla)      | Cierra el "campo de texto" y empieza a hablar como código | La base de todo ataque |
| `--` (dos guiones) | "Todo lo que venga después, ignóralo"                     | `admin' --`            |
| `;` (punto y coma) | "Termina esta orden y empieza una nueva"                  | `'; DROP TABLE...`     |
| `OR 1=1`           | "Haz que la condición siempre sea verdadera"              | Bypass de login        |
| `UNION SELECT`     | "Además de lo que pedí, tráeme datos de OTRA tabla"       | Robo de datos          |

> **¿Ves el patrón?** Todo empieza con la comilla `'`. Esa comilla es como la "llave maestra" que abre la puerta entre el campo de texto del usuario y el corazón de la base de datos.

---

---

## 🛡️ ¿Cómo se protegen las empresas?

Ahora la parte más importante: ¿Cómo se evita que esto pase?

---

### Defensa 1: El Mesero Inteligente (Consultas Parametrizadas) ⭐

**Esta es la defensa número 1 del mundo.** Es tan efectiva que si el programador la usa correctamente, SQL Injection se vuelve **imposible**.

**¿En qué consiste?** En vez de que el mesero repita textualmente lo que el cliente dice, el mesero usa una **orden preimpresa** con espacios en blanco:

```
ANTES (mesero tonto → VULNERABLE):
  El mesero escucha al cliente y repite textualmente:
  "Dame la pizza llamada [lo que el cliente dijo]"
  → Si el cliente dice "Margarita Y TODO EL DINERO",
    el mesero dice exactamente eso a la cocina ☠️

DESPUÉS (mesero inteligente → SEGURO):
  El mesero tiene una hoja impresa que dice:
  "Dame la pizza llamada ______"
  El mesero SOLO escribe el nombre en el espacio en blanco.
  → Si el cliente dice "Margarita Y TODO EL DINERO",
    el mesero escribe eso entero en el espacio ____
    La cocina busca una pizza llamada
    "Margarita Y TODO EL DINERO" → no la encuentra → fin ✅
    NUNCA ejecuta "dame el dinero" como una orden separada.
```

**¿Por qué funciona?** Porque la cocina recibe la orden (el SQL) y los ingredientes (los datos del usuario) **por separado**. Primero lee la orden y la entiende. Después mete los datos del usuario en los espacios en blanco, pero **jamás los interpreta como parte de la orden**. El texto del cliente es solo texto, nunca se convierte en un comando.

---

### Defensa 2: El Guardia de Seguridad (Validación de Datos)

Antes de que el mesero lleve la orden a la cocina, un **guardia de seguridad** revisa lo que el cliente escribió:

```
El cliente dice su nombre: "Ariel123"
El guardia revisa: "¿Esto parece un nombre real?"
  → Solo letras y espacios → ✅ Pasa
  → Tiene comillas, punto y coma, guiones → ❌ Rechazado

El cliente dice su edad: "25"
El guardia revisa: "¿Esto es un número?"
  → Es un número → ✅ Pasa
  → Tiene letras o símbolos → ❌ Rechazado
```

| El campo pide... | El guardia verifica que sea...       |
| ---------------- | ------------------------------------ |
| Un nombre        | Solo letras, espacios y tildes       |
| Un email         | Formato válido (algo@algo.com)       |
| Una edad         | Solo un número entero                |
| Una fecha        | Formato de fecha válido (DD-MM-AAAA) |

> Si el usuario escribe `' OR 1=1 --` en el campo de "nombre", el guardia dice: _"Esto NO es un nombre. Tiene comillas y guiones. Rechazado."_ Y el ataque ni siquiera llega a la cocina.

---

### Defensa 3: El Empleado con Permisos Limitados (Mínimo Privilegio)

Imagina que en el restaurante, el mesero tiene una tarjeta de acceso. Esa tarjeta **solo le permite entrar a la cocina y pedir platos**. No le permite abrir la caja registradora, ni entrar a la bodega, ni cambiar el menú.

En bases de datos es lo mismo:

```
❌ LO PELIGROSO: Darle al código de la aplicación acceso TOTAL
   → "Este usuario puede leer, escribir, borrar,
      modificar tablas, crear usuarios y todo lo demás"
   → Si hay una inyección, el atacante puede DESTRUIR todo

✅ LO CORRECTO: Darle al código SOLO lo que necesita
   → "Este usuario SOLO puede leer productos y crear pedidos"
   → Si hay una inyección, el atacante solo podría leer productos
   → NO puede borrar tablas, NO puede ver contraseñas
```

> Así, incluso si un atacante logra inyectar algo, el daño que puede hacer es **muy limitado**. Es como si un ladrón entrara al restaurante pero la caja fuerte estuviera sellada con llave.

---

### Defensa 4: El Muro de Fuego (WAF - Web Application Firewall)

Un WAF es como un **detector de metales** en la entrada del restaurante. Antes de que el cliente siquiera hable con el mesero, el WAF revisa lo que trae encima:

```
Cliente normal: "Quiero ver pizzas" → ✅ Pasa
Atacante: "' OR 1=1 --"           → 🚨 ALERTA: patrón de ataque detectado → BLOQUEADO
Atacante: "UNION SELECT password"  → 🚨 ALERTA: intento de robo de datos → BLOQUEADO
Atacante: "'; DROP TABLE"          → 🚨 ALERTA: intento de destrucción → BLOQUEADO
```

El WAF conoce los "patrones típicos" de los ataques SQL Injection y los bloquea antes de que lleguen al código.

---

### Defensa 5: El ORM (El Traductor Automático)

Los frameworks modernos (como Django, Rails, Laravel) usan algo llamado **ORM** (Object-Relational Mapping). Es como tener un **traductor profesional** entre el mesero y la cocina.

En vez de que el programador escriba órdenes SQL a mano (donde puede cometer errores), el ORM las genera automáticamente y **siempre de forma segura**.

```
Sin ORM (el programador escribe SQL a mano → puede equivocarse):
  "SELECT * FROM usuarios WHERE nombre = '" + lo_que_dijo_el_cliente + "'"
  → ❌ Si el cliente mete código malicioso, se inyecta

Con ORM (el framework genera el SQL automáticamente):
  User.objects.filter(nombre=lo_que_dijo_el_cliente)
  → ✅ El ORM SIEMPRE separa los datos del código
  → Es imposible inyectar SQL
```

---

### Resumen Visual: Las Capas de Protección

```
                    🛡️ CAPAS DE DEFENSA
┌──────────────────────────────────────────────────┐
│  Capa 1 — WAF (detector de metales en la puerta)│
│  ┌──────────────────────────────────────────────┐│
│  │  Capa 2 — Validación (guardia de seguridad)  ││
│  │  ┌──────────────────────────────────────────┐││
│  │  │  Capa 3 — Consultas Parametrizadas ⭐    │││
│  │  │  (el mesero inteligente / la más          │││
│  │  │   importante de todas)                    │││
│  │  │  ┌──────────────────────────────────────┐│││
│  │  │  │  Capa 4 — Permisos Limitados en BD   ││││
│  │  │  └──────────────────────────────────────┘│││
│  │  └──────────────────────────────────────────┘││
│  └──────────────────────────────────────────────┘│
└──────────────────────────────────────────────────┘
```

> **La seguridad es por capas.** Ninguna defensa sola es suficiente. Pero si combinas varias, el atacante tendría que romper **todas** para lograr algo, y eso es prácticamente imposible.

---

---

## 🎬 La Película Completa: Un Ataque vs Una Defensa (Paso a Paso)

Para que quede cristalino, veamos la misma situación con y sin protección:

### 🔴 Escenario SIN protección

```
1. El atacante llega a la página de login del banco.

2. En el campo "Usuario" escribe:    admin' --
   En el campo "Clave" escribe:      cualquiercosa

3. El código del programador (el mesero tonto) arma la consulta
   pegando directamente lo que el usuario escribió:

   SELECT * FROM usuarios
   WHERE nombre = 'admin' --' AND clave = 'cualquiercosa'
                          ↑↑
                          Los dos guiones COMENTAN todo lo que sigue.
                          La verificación de la clave DESAPARECE.

4. La base de datos ejecuta:
   "Busca al usuario 'admin'" → Lo encuentra → Acceso concedido ☠️

5. El atacante está adentro del banco como administrador.
   Sin contraseña. En 5 segundos.
```

### 🟢 Escenario CON protección (consultas parametrizadas)

```
1. El atacante llega a la misma página de login.

2. En el campo "Usuario" escribe:    admin' --
   En el campo "Clave" escribe:      cualquiercosa

3. El código del programador (el mesero inteligente) tiene una
   orden PREIMPRESA con espacios en blanco:

   SELECT * FROM usuarios
   WHERE nombre = [___espacio 1___] AND clave = [___espacio 2___]

   Y mete los datos del usuario EN LOS ESPACIOS, como texto puro:
   Espacio 1 ← "admin' --"        (todo junto, como texto plano)
   Espacio 2 ← "cualquiercosa"

4. La base de datos ejecuta:
   "Busca a alguien cuyo nombre sea literalmente: admin' -- "
   → No encuentra a nadie con ese nombre tan raro → Acceso denegado ✅

5. El atacante se queda afuera. La comilla y los guiones
   NO se interpretaron como código. Son solo texto inocente.
```

---

---

## 🔒 Checklist: ¿Qué debe hacer una empresa para protegerse?

- [ ] **Usar consultas parametrizadas** (la defensa #1 de todo el universo)
- [ ] **Usar un ORM** cuando sea posible (genera SQL seguro automáticamente)
- [ ] **Validar toda entrada** del usuario (verificar tipo, largo y formato)
- [ ] **Dar permisos mínimos** a la cuenta de base de datos (solo lo necesario)
- [ ] **No mostrar errores técnicos** al usuario (los errores revelan información)
- [ ] **Mantener todo actualizado** (base de datos, frameworks, sistema operativo)
- [ ] **Guardar contraseñas cifradas** (nunca en texto plano legible)
- [ ] **Hacer auditorías de seguridad** periódicas

---

## ❌ Lo que un programador NUNCA debe hacer

En español simple, el error mortal es: **pegar directamente lo que el usuario escribió dentro de la instrucción SQL**. Da igual el lenguaje de programación que uses.

```
❌ PROHIBIDO (en cualquier lenguaje):
   "Toma lo que el usuario escribió y pégalo directamente en la consulta"
   → Esto permite que el atacante cuele código malicioso.

✅ CORRECTO (en cualquier lenguaje):
   "Prepara la consulta con espacios en blanco.
    Después, mete lo que el usuario escribió en esos espacios,
    pero SOLO como datos, NUNCA como código."
   → Esto hace que SQL Injection sea imposible.
```

> **Es así de simple.** Si el programador separa el código de los datos, el ataque **no funciona**.

---

---

## 💀 Por qué esto importa (aunque no seas programador)

Tal vez pienses _"Yo no programo, ¿por qué me importa?"_

Porque tus datos están en bases de datos:

- Tu cuenta bancaria está en una base de datos.
- Tu historial médico está en una base de datos.
- Tus fotos de Instagram están en una base de datos.
- Tu nota de la universidad está en una base de datos.

Si el programador que construyó esa aplicación **no protegió su código**, un atacante puede:

- Ver tu saldo bancario.
- Cambiar tu nota de un 4.0 a un 7.0 (o a un 1.0).
- Leer tus mensajes privados.
- Borrar tu cuenta completa.

> **SQL Injection no es un tema de hackers con capucha en un sótano oscuro.** Es un error de programación que se comete todos los días y que afecta a personas reales. Por eso es tan importante que incluso los no-programadores entiendan qué es y cómo exigir que las aplicaciones que usan estén protegidas.

---

## 🔗 Recursos adicionales

| Recurso                 | Enlace                                                                  | Descripción                          |
| ----------------------- | ----------------------------------------------------------------------- | ------------------------------------ |
| **OWASP SQL Injection** | [owasp.org/sqli](https://owasp.org/www-community/attacks/SQL_Injection) | Guía oficial de referencia           |
| **PortSwigger Academy** | [portswigger.net](https://portswigger.net/web-security/sql-injection)   | Labs interactivos gratuitos          |
| **OWASP Top 10**        | [owasp.org/top10](https://owasp.org/www-project-top-ten/)               | Las 10 vulnerabilidades más críticas |

### 🧪 Entornos de práctica seguros

> Estos entornos están **diseñados para ser hackeados** de forma legal y educativa:

- **DVWA** (Damn Vulnerable Web Application) — App vulnerable a propósito
- **SQLi-labs** — Laboratorio específico para practicar SQL Injection
- **Hack The Box** — Plataforma de CTF con máquinas vulnerables
- **TryHackMe** — Cursos guiados de ciberseguridad

---

> **⚠️ Aviso Legal:** Este contenido es **exclusivamente educativo**. Realizar ataques de SQL Injection contra sistemas sin autorización explícita es **ilegal** y puede acarrear consecuencias penales. Siempre practica en entornos controlados y con permiso.

