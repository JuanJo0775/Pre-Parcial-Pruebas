# Registro de Notas Académicas
## Pre-Parcial — Pruebas de Software | Semestre V

**Tecnología elegida:** Python + pytest + pytest-bdd  
**Razón:** Ecosistema maduro para TDD y BDD. pytest es el estándar de facto en Python. pytest-bdd integra Gherkin nativamente sin frameworks adicionales. Curva de aprendizaje baja y excelente soporte en CI/CD.

---

## 1. Análisis de Particiones de Equivalencia (Req. 1)

| Partición | Rango | Valor representativo | Resultado esperado |
|---|---|---|---|
| Válida inferior | [0.0, 3.0) | 1.5 | Registro exitoso |
| Válida aprobatoria | [3.0, 5.0] | 4.0 | Registro exitoso |
| Límite inferior exacto | {0.0} | 0.0 | Registro exitoso |
| Límite superior exacto | {5.0} | 5.0 | Registro exitoso |
| Inválida negativa | (-∞, 0.0) | -1.0 | ValueError |
| Inválida superior | (5.0, +∞) | 6.0 | ValueError |

---

## 2. Análisis de Valores Límite (Req. 1)

| Valor | Posición | En rango | Resultado esperado |
|---|---|---|---|
| -0.1 | Justo antes del límite inferior | No | ValueError |
| 0.0 | Límite inferior exacto | Sí | Registro exitoso |
| 0.1 | Justo después del límite inferior | Sí | Registro exitoso |
| 4.9 | Justo antes del límite superior | Sí | Registro exitoso |
| 5.0 | Límite superior exacto | Sí | Registro exitoso |
| 5.1 | Justo después del límite superior | No | ValueError |

---

## 3. Preguntas al Product Owner (Req. 4)

**Pregunta 1:** ¿El "semestre" es un identificador libre (texto) o tiene un formato controlado como "2024-1"?  
**Impacto:** Si es texto libre, "2024-1" y "2024 - 1" podrían ser semestres distintos o iguales según interpretación. Esto define si necesitamos normalización de entradas y cambia completamente los casos de prueba de duplicados.

**Pregunta 2:** ¿Qué sucede si se intenta registrar una nota duplicada? ¿Se rechaza silenciosamente, se lanza una excepción o se actualiza la nota existente?  
**Impacto:** Según la respuesta, los casos de prueba negativos cambian: si se actualiza, necesitamos verificar el nuevo valor; si se lanza excepción, debemos probar el tipo y mensaje del error.

---

## 4. Tabla de Casos de Prueba

| ID | Req | Descripción | Precondición | Datos de entrada | Pasos | Resultado esperado | Tipo |
|---|---|---|---|---|---|---|---|
| TC01 | 1 | Registrar nota en límite inferior | Sin notas | materia="Mat", sem="2024-1", nota=0.0 | Llamar registrar_nota | Registro exitoso, sin error | Borde |
| TC02 | 1 | Registrar nota en límite superior | Sin notas | materia="Mat", sem="2024-1", nota=5.0 | Llamar registrar_nota | Registro exitoso, sin error | Borde |
| TC03 | 1 | Registrar nota válida intermedia | Sin notas | materia="Mat", sem="2024-1", nota=3.5 | Llamar registrar_nota | Registro exitoso, sin error | Positivo |
| TC04 | 1 | Nota negativa justo bajo límite | Sin notas | materia="Mat", sem="2024-1", nota=-0.1 | Llamar registrar_nota | ValueError | Negativo |
| TC05 | 1 | Nota justo sobre límite superior | Sin notas | materia="Mat", sem="2024-1", nota=5.1 | Llamar registrar_nota | ValueError | Negativo |
| TC06 | 1 | Nota muy negativa | Sin notas | materia="Mat", sem="2024-1", nota=-10.0 | Llamar registrar_nota | ValueError | Negativo |
| TC07 | 2 | Nota exactamente 3.0 aprueba | Nota 3.0 registrada | materia="Fis", sem="2024-1" | Consultar aprueba() | True | Borde |
| TC08 | 2 | Nota 4.5 aprueba | Nota 4.5 registrada | materia="Fis", sem="2024-1" | Consultar aprueba() | True | Positivo |
| TC09 | 2 | Nota 2.9 reprueba | Nota 2.9 registrada | materia="Fis", sem="2024-1" | Consultar aprueba() | False | Borde |
| TC10 | 2 | Nota 0.0 reprueba | Nota 0.0 registrada | materia="Fis", sem="2024-1" | Consultar aprueba() | False | Negativo |
| TC11 | 3 | Promedio sin notas | Sin notas | — | Consultar promedio() | 0.0 | Negativo |
| TC12 | 3 | Promedio con una nota | Una nota registrada | nota=4.0 | Consultar promedio() | 4.0 | Positivo |
| TC13 | 3 | Promedio con múltiples notas | Dos notas registradas | notas=4.0 y 2.0 | Consultar promedio() | 3.0 | Positivo |
| TC14 | 4 | Duplicado misma materia mismo semestre | Nota registrada | misma materia y semestre | Intentar registrar_nota | ValueError | Negativo |
| TC15 | 4 | Misma materia diferente semestre | Nota en 2024-1 | misma materia, sem="2024-2" | Llamar registrar_nota | Registro exitoso | Positivo |
| TC16 | 4 | Diferente materia mismo semestre | Una nota registrada | nueva materia, mismo semestre | Llamar registrar_nota | Registro exitoso | Positivo |

---

## 5. Reporte de Cobertura

```text
---------- coverage: platform win32, python 3.12.10-final-0 ----------
Name                             Stmts   Miss  Cover   Missing
--------------------------------------------------------------
src\__init__.py                      0      0   100%
src\registro_notas\__init__.py       0      0   100%
src\registro_notas\modelo.py        19      0   100%
--------------------------------------------------------------
TOTAL                               19      0   100%

Required test coverage of 85% reached. Total coverage: 100.00%
```

---
