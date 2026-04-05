# Proyecto: Asociatividad y Precedencia

Este proyecto contiene dos programas en Python que implementan:

* Asociatividad
* Precedencia

---

# Programa 1: Asociatividad 

## Descripción

Este programa recibe expresiones aritméticas simples (sin paréntesis) y realiza las siguientes operaciones:

1. Construye el árbol de derivación considerando:

   * Asociatividad izquierda
   * Asociatividad derecha

2. Evalúa cada uno de los árboles generados

3. Muestra:

   * El árbol correspondiente
   * El resultado numérico de la expresión

---

## Concepto

La asociatividad define cómo se agrupan operadores del mismo nivel.

Ejemplo:

```
4 - 3 - 2
```

* Asociatividad izquierda: (4 - 3) - 2 = -1
* Asociatividad derecha: 4 - (3 - 2) = 3

---

## Validaciones implementadas

El programa verifica:

* Estructura válida (número operador número)
* Posiciones correctas de operandos y operadores
* Tokens válidos (solo números y operadores +, -, *, /)

Errores detectados:

* Operadores consecutivos (ej: `4 - - 2`)
* Falta de operandos (ej: `5 +`)
* Símbolos inválidos (ej: `a - 3`)
* Estructura incorrecta

---

## Ejemplo de entrada (`pruebaAs.txt`)

```
4 - 3 - 2
4 - - 2
10 - 5 - 1
```

---

## Ejecución

```
python asociatividad.py < pruebaAs.txt
```

---

## Salida esperada

```
Expresión: 4 - 3 - 2

--- Asociatividad Izquierda ---
(árbol)
Resultado: -1

--- Asociatividad Derecha ---
(árbol)
Resultado: 3
```

---

# Programa 2: Precedencia 

## Descripción

Este programa permite definir una jerarquía de operadores y genera automáticamente una gramática libre de contexto.

Realiza las siguientes funciones:

1. Recibe operadores ordenados de menor a mayor precedencia
2. Genera un no terminal por cada nivel
3. Construye las reglas de producción de la gramática
4. Presenta ejemplos de aplicación

---

## Concepto

La precedencia determina el orden en que se evalúan los operadores.

Ejemplo:

```
4 + 3 * 2
```

Se interpreta como:

```
4 + (3 * 2)
```

porque el operador `*` tiene mayor precedencia que `+`.

---

## Validaciones implementadas

El programa verifica:

* Que se ingresen operadores
* Que los operadores sean válidos (`+`, `-`, `*`, `/`)
* Que no haya operadores repetidos consecutivos

Errores detectados:

* Operadores inválidos (ej: `+ a *`)
* Repeticiones (ej: `+ + *`)
* Entrada vacía

---

## Ejemplo de entrada (`pruebasPre.txt`)

```
+ - *
+ + *
+ a *
```

---

## Ejecución

```
python precedencia.py < pruebaPre.txt
```
