import pytest
from registro_notas.modelo import RegistroNotas


# ─── REQUERIMIENTO 1: Registro de notas válidas e inválidas ───────────────────

class TestRegistrarNota:

    def test_TC01_registrar_nota_valida_limite_inferior(self):
        r = RegistroNotas()
        r.registrar_nota("Matematicas", "2024-1", 0.0)

    def test_TC02_registrar_nota_valida_limite_superior(self):
        r = RegistroNotas()
        r.registrar_nota("Matematicas", "2024-1", 5.0)

    def test_TC03_registrar_nota_valida_intermedia(self):
        r = RegistroNotas()
        r.registrar_nota("Matematicas", "2024-1", 3.5)

    def test_TC04_nota_negativa_lanza_error(self):
        r = RegistroNotas()
        with pytest.raises(ValueError):
            r.registrar_nota("Matematicas", "2024-1", -0.1)

    def test_TC05_nota_mayor_cinco_lanza_error(self):
        r = RegistroNotas()
        with pytest.raises(ValueError):
            r.registrar_nota("Matematicas", "2024-1", 5.1)

    def test_TC06_nota_muy_negativa_lanza_error(self):
        r = RegistroNotas()
        with pytest.raises(ValueError):
            r.registrar_nota("Matematicas", "2024-1", -10.0)


# ─── REQUERIMIENTO 2: Aprobación ─────────────────────────────────────────────

class TestAprobacion:

    def test_TC07_nota_exactamente_tres_aprueba(self):
        r = RegistroNotas()
        r.registrar_nota("Fisica", "2024-1", 3.0)
        assert r.aprueba("Fisica", "2024-1") is True

    def test_TC08_nota_superior_a_tres_aprueba(self):
        r = RegistroNotas()
        r.registrar_nota("Fisica", "2024-1", 4.5)
        assert r.aprueba("Fisica", "2024-1") is True

    def test_TC09_nota_inferior_a_tres_reprueba(self):
        r = RegistroNotas()
        r.registrar_nota("Fisica", "2024-1", 2.9)
        assert r.aprueba("Fisica", "2024-1") is False

    def test_TC10_nota_cero_reprueba(self):
        r = RegistroNotas()
        r.registrar_nota("Fisica", "2024-1", 0.0)
        assert r.aprueba("Fisica", "2024-1") is False


# ─── REQUERIMIENTO 3: Promedio ────────────────────────────────────────────────

class TestPromedio:

    def test_TC11_promedio_sin_notas_es_cero(self):
        r = RegistroNotas()
        assert r.promedio() == 0.0

    def test_TC12_promedio_una_nota(self):
        r = RegistroNotas()
        r.registrar_nota("Quimica", "2024-1", 4.0)
        assert r.promedio() == 4.0

    def test_TC13_promedio_multiples_notas(self):
        r = RegistroNotas()
        r.registrar_nota("Quimica", "2024-1", 4.0)
        r.registrar_nota("Fisica", "2024-1", 2.0)
        assert r.promedio() == 3.0


# ─── REQUERIMIENTO 4: No duplicar nota ───────────────────────────────────────

class TestNoDuplicados:

    def test_TC14_duplicado_misma_materia_mismo_semestre_lanza_error(self):
        r = RegistroNotas()
        r.registrar_nota("Historia", "2024-1", 3.5)
        with pytest.raises(ValueError):
            r.registrar_nota("Historia", "2024-1", 4.0)

    def test_TC15_misma_materia_diferente_semestre_es_valido(self):
        r = RegistroNotas()
        r.registrar_nota("Historia", "2024-1", 3.5)
        r.registrar_nota("Historia", "2024-2", 4.0)

    def test_TC16_diferente_materia_mismo_semestre_es_valido(self):
        r = RegistroNotas()
        r.registrar_nota("Historia", "2024-1", 3.5)
        r.registrar_nota("Matematicas", "2024-1", 4.0)
