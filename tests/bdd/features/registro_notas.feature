Feature: Registro de notas académicas
  Como coordinador académico de la Universidad Regional del Sur
  Quiero gestionar las notas de los estudiantes
  Para determinar si aprueban o reprueban sus materias y calcular su rendimiento

  Background:
    Given un estudiante sin notas registradas

  # ─── REQUERIMIENTO 2: Aprobación ─────────────────────────────────────────

  @smoke @critical
  Scenario: Estudiante aprueba con nota exactamente igual al mínimo
    Given el estudiante tiene nota 3.0 en "Matematicas" del semestre "2024-1"
    When se consulta si aprueba "Matematicas" en el semestre "2024-1"
    Then el resultado debe ser aprobado

  @smoke @critical
  Scenario: Estudiante reprueba con nota inferior al mínimo
    Given el estudiante tiene nota 2.9 en "Matematicas" del semestre "2024-1"
    When se consulta si aprueba "Matematicas" en el semestre "2024-1"
    Then el resultado debe ser reprobado

  @regression
  Scenario Outline: Verificar aprobación para distintas notas
    Given el estudiante tiene nota <nota> en "<materia>" del semestre "2024-1"
    When se consulta si aprueba "<materia>" en el semestre "2024-1"
    Then el resultado debe ser <resultado>

    Examples:
      | nota | materia   | resultado  |
      | 5.0  | Fisica    | aprobado   |
      | 3.0  | Quimica   | aprobado   |
      | 2.9  | Historia  | reprobado  |
      | 0.0  | Biologia  | reprobado  |

  # ─── REQUERIMIENTO 3: Promedio ─────────────────────────────────────────────

  @smoke
  Scenario: Promedio de estudiante sin notas es cero
    When se calcula el promedio del estudiante
    Then el promedio debe ser 0.0

  @regression
  Scenario: Promedio con múltiples materias
    Given el estudiante tiene nota 4.0 en "Matematicas" del semestre "2024-1"
    And el estudiante tiene nota 2.0 en "Fisica" del semestre "2024-1"
    When se calcula el promedio del estudiante
    Then el promedio debe ser 3.0

  # ─── REQUERIMIENTO 4: No duplicados ─────────────────────────────────────────

  @critical
  Scenario: No se puede registrar dos notas para la misma materia en el mismo semestre
    Given el estudiante tiene nota 3.5 en "Historia" del semestre "2024-1"
    When se intenta registrar nota 4.0 en "Historia" del semestre "2024-1"
    Then el sistema debe lanzar un error de duplicado

  @regression
  Scenario: Sí se puede registrar la misma materia en semestre diferente
    Given el estudiante tiene nota 3.5 en "Historia" del semestre "2024-1"
    When se registra nota 4.0 en "Historia" del semestre "2024-2"
    Then la nota debe quedar registrada correctamente
