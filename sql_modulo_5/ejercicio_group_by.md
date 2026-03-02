# 🏴‍☠️ Guía de Estudio Autónomo: El Tesoro del GROUP BY

¡Bienvenido a los desafíos analíticos! ⚓

Está a punto de embarcarse en la aventura de aprender a usar `GROUP BY` y `HAVING`. Muchos han intentado entender cómo agrupar datos y han terminado en el fondo del mar, enredados entre sumas y filtros que no funcionaban.

Pero usted tiene ventaja. Hoy utilizará el **"Método de los Cofres Piratas"** para estudiar esto a su propio ritmo.

Lea la teoría, visualice el proceso mentalmente y luego resuelva los desafíos en su motor SQL.

---

## 🛠️ Paso 1: Carga los datos en su entorno (Preparación)

Abra DBeaver, pgAdmin o la consola SQL que utilice, copie este código y ejecútelo. Esto creará la tabla con los tesoros saqueados por 4 piratas en 3 barcos distintos:

```sql
CREATE TABLE lateral_botin_flota (
    id_saqueo SERIAL PRIMARY KEY,
    barco VARCHAR(50),
    pirata VARCHAR(50),
    tipo_tesoro VARCHAR(50),
    valor_monedas INT
);

INSERT INTO lateral_botin_flota (barco, pirata, tipo_tesoro, valor_monedas) VALUES
('La Perla Negra', 'Jack', 'Doblón de Oro', 500),
('La Perla Negra', 'Jack', 'Doblón de Plata', 100),
('La Perla Negra', 'Will', 'Doblón de Oro', 200),
('La Venganza', 'Barbanegra', 'Cáliz Sagrado', 1000),
('La Venganza', 'Barbanegra', 'Cáliz Sagrado', 1000),
('La Venganza', 'Anne', 'Doblón de Oro', 300),
('La Venganza', 'Anne', 'Doblón de Plata', 50),
('El Holandés', 'Davy', 'Perla Maldita', 800),
('El Holandés', 'Davy', 'Doblón de Oro', 400),
('El Holandés', 'Davy', 'Esmeralda', 600);
```

¡Listo! Todos los tesoros están disponibles. Ahora se procede a organizarlos.

---

---

## 📦 Nivel 1: El Arte de Hacer Cofres (GROUP BY Básico)

### 📖 La Teoría Visual

Imagine que el contramaestre grita: _"¡Quiero saber cuánto dinero recaudó CADA BARCO!"_

Si se ejecuta un `SELECT SUM(valor_monedas)` simple, SQL sumará TODO (4950 monedas) y devolverá un solo número. Eso no sirve para saber cuánto obtuvo cada barco. Es necesario separarlo.

El `GROUP BY` es como ordenar: **"¡Traigan 3 cofres grandes! Escriban 'La Perla Negra' en el primero, 'La Venganza' en el segundo, y 'El Holandés' en el tercero. ¡Y ahora coloquen cada fila (tesoro) dentro de su cofre correspondiente!"**

Una vez que los cofres están armados y cerrados, SQL aplica la función matemática (`SUM`, `COUNT`, `AVG`) **SOLO al contenido que quedó dentro del cofre**.

### ⚔️ Desafío 1: El Botín por Barco

**Misión:** Escribir una consulta SQL que devuelva dos columnas: el nombre del `barco` y su `botin_total` (la suma de sus `valor_monedas`).

_<details><summary>💡 Pista para el Desafío 1 (Haga clic para ver)</summary>_
_Seleccione las columnas barco y SUM(valor_monedas). Luego indíquele a SQL que agrupe explícitamente usando la instrucción `GROUP BY barco`._
_</details>_

---

## 🗃️ Nivel 2: Cofres dentro de Cofres (GROUP BY Múltiple)

### 📖 La Teoría Visual

El Capitán dice: _"¡Está bien saber cuánto obtuvo cada barco, pero ahora quiero saber cuánto recolectó CADA PIRATA EN SU RESPECTIVO BARCO!"_

¿Qué cambia? Ahora no bastan 3 cofres grandes, se necesitan **subgrupos**. Si se indica a SQL `GROUP BY barco, pirata`, SQL dirá: _"¡Abran el cofre grande de La Perla Negra y coloquen dos cofres pequeños, uno etiquetado 'Jack' y otro 'Will'! Y distribuyan los tesoros ahí."_

SQL crea un cofre nuevo por cada **combinación única** de barco y pirata.

> ⚠️ **LA LEY INQUEBRANTABLE:** Si en el `SELECT` se solicita ver el `barco` y el `pirata`, **AMBAS columnas** deben estar escritas después del `GROUP BY`. Si se solicita que SQL muestre al "pirata" pero solo se indica `GROUP BY barco`, SQL lanzará un error porque no sabrá de qué pirata extraer el nombre si la caja completa se llama "La Perla Negra".

### ⚔️ Desafío 2: La Cuenta Personal

**Misión:** Mostrar el `barco`, el `pirata` y su suma total de tesoros bajo el alias `botin_personal`.

---

## 🛡️ Nivel 3: El Guardia Ciego vs El Tasador (WHERE vs HAVING)

### 📖 La Teoría Visual (¡ESTO ES LO MÁS IMPORTANTE DEL TUTORIAL!)

El Capitán solicita: _"Genere un reporte de cuánto botín total tiene cada pirata. **PERO**, muéstreme solo a los piratas que sumen **más de 500 monedas en total**, el resto no importa."_

Si se tiene poca experiencia, la lógica indicaría usar un `WHERE`:
❌ `... WHERE valor_monedas > 500 GROUP BY pirata;`

**¡ESTO DESTRUIRÁ SUS DATOS! ¿Por qué?**
Porque el `WHERE` es un **Guardia Ciego**. Trabaja patrullando la cubierta del barco _ANTES_ de que existan los cofres.
El Guardia Ciego mira el primer tesoro de Jack (500 de oro) y dice _"¿Es MAYOR a 500? No. ¡Lo desecho!"_. Luego mira las 100 de plata de Jack y también las descarta. En resumen, **los elimina antes de que se realice la suma real**.
Cuando se arma la caja de botín de Jack, la suma dará cero. Jack desaparece del reporte, a pesar de que en realidad sí superaba los 500 (500 + 100 = 600) y **debía** aparecer en la lista final.

**La Solución: El HAVING**
Para evaluar "sumas matemáticas ya calculadas", se necesita un **Tasador** que trabaje **DESPUÉS** de que los cofres están cerrados. Ese tasador se llama `HAVING`.
Se coloca _siempre_ después del `GROUP BY`. Él abre la caja final y dice: _"Veamos Jack, ¿La suma completa de todo su contenido (`SUM(valor_monedas)`) supera los 500? Perfecto, ¡pasa al reporte!"_

### ⚔️ Desafío 3: El Club de los 500

**Misión:** Agrupar por `pirata`, sumar todos sus tesoros e imprimir el reporte. Usar la instrucción correcta al final para que **SOLO** aparezcan los piratas que superaron las 500 monedas acumuladas (deberían aparecer solo Davy, Jack y Barbanegra).

---

## 💎 Nivel 4: Los 5 Monóculos Mágicos (Agregaciones Simultáneas)

### 📖 La Teoría Visual

Una vez agrupado en un cofre sellado (por ejemplo, por `barco`), se puede solicitar al analista que aplique varios tipos de análisis al interior del cofre de **múltiples formas diferentes al mismo tiempo**, todo sin escribir otra consulta distinta:

- _"Sume todo"_ (`SUM`)
- _"Cuente cuántas unidades hay en total"_ (`COUNT`)
- _"Dígame cuánto vale el elemento de menor valor"_ (`MIN`)
- _"Dígame cuánto vale el elemento de mayor valor"_ (`MAX`)
- _"Calcule el promedio matemático de todo"_ (`AVG`)

### ⚔️ Desafío 4: El Gran Resumen Estadístico

**Misión:** Agrupar por `barco` y en el `SELECT`, extraer estas 5 estadísticas (con alias usando `AS`):

1. El barco (identificación).
2. Cuántos objetos trajeron (`COUNT` al id_saqueo)
3. Suma total de ganancias.
4. El tesoro de menor valor (mínimo).
5. El tesoro de mayor valor (máximo).

---

## 🏴‍☠️ Nivel 5: Desafío Jefe - Lógica en Inversa (Pensamiento Lateral)

_Si se resuelve esto de manera autónoma, el estudiante está preparado para dominar el análisis SQL._

La Reina Pirata decreta lo siguiente:
_"Muéstreme a cada pirata y sume absolutamente todo su botín._
_¡PERO DETESTO LA PLATA! Si se descubre que el cofre de un pirata contiene **AUNQUE SEA UN 'Doblón de Plata'** escondido adentro... ¡Que se elimine TODO su cofre (incluso el oro) de la lista oficial!"_

### ⚔️ Desafío 5: Salvando los Resultados

Este ejercicio es complejo.

1. Si se usa el Guardia Ciego (`WHERE tipo_tesoro != 'Doblón de Plata'`), se comete el error clásico de principiante. El guardia ciego eliminará solo las monedas de plata pero dejará entrar el oro de Anne y de Jack a sus cofres... Y lo que se necesita es **descartar el cofre de Jack COMPLETO**.
2. Se debe sumar el cofre de todos y luego hacer el descarte condicional en la fase del Tasador (`HAVING`), evaluando el contenido interior.

**Misión:** Escribir una consulta que agrupe por `pirata` mostrando su botín total. Usar `HAVING` para excluir a cualquier pirata que haya traído plata, dejando finalmente listados **SOLO** a Will, Barbanegra y Davy, mostrando sus botines completos.

_<details><summary>☠️ El Truco Final (Haga clic aquí si necesita ayuda)</summary>_
_El Tasador (`HAVING`) puede evaluar condicionales lógicos si se combinan con una función matemática (por ejemplo, SUM)._
_Intente hacer que el Tasador aplique un "filtro lógico" al interior del grupo: **Cuente cuántos elementos de tesoro eran de plata**. Si el resultado es igual a 0, el pirata puede aparecer en el listado:_
_`HAVING SUM(CASE WHEN tipo_tesoro = 'Doblón de Plata' THEN 1 ELSE 0 END) = 0;`_
_</details>_
