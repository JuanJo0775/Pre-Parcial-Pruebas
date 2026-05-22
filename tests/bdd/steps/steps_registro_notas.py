import pytest
from pytest_bdd import given, when, then, parsers
from registro_notas.modelo import RegistroNotas


@pytest.fixture
def registro():
    return RegistroNotas()


@given("un estudiante sin notas registradas", target_fixture="registro")
def estudiante_sin_notas():
    return RegistroNotas()


@given(parsers.parse("el estudiante tiene nota {nota:f} en \"{materia}\" del semestre \"{semestre}\""))
def registrar_nota(registro, nota, materia, semestre):
    registro.registrar_nota(materia, semestre, nota)


@when(parsers.parse("se consulta si aprueba \"{materia}\" en el semestre \"{semestre}\""), target_fixture="resultado_aprobacion")
def consultar_aprobacion(registro, materia, semestre):
    return registro.aprueba(materia, semestre)


@then("el resultado debe ser aprobado")
def verificar_aprobado(resultado_aprobacion):
    assert resultado_aprobacion is True


@then("el resultado debe ser reprobado")
def verificar_reprobado(resultado_aprobacion):
    assert resultado_aprobacion is False


@then(parsers.parse("el resultado debe ser {resultado}"))
def verificar_resultado(resultado_aprobacion, resultado):
    if resultado == "aprobado":
        assert resultado_aprobacion is True
    else:
        assert resultado_aprobacion is False


@when("se calcula el promedio del estudiante", target_fixture="promedio_calculado")
def calcular_promedio(registro):
    return registro.promedio()


@then(parsers.parse("el promedio debe ser {valor:f}"))
def verificar_promedio(promedio_calculado, valor):
    assert promedio_calculado == pytest.approx(valor)


@when(parsers.parse("se intenta registrar nota {nota:f} en \"{materia}\" del semestre \"{semestre}\""), target_fixture="error_capturado")
def intentar_duplicado(registro, nota, materia, semestre):
    try:
        registro.registrar_nota(materia, semestre, nota)
        return None
    except ValueError as e:
        return e


@then("el sistema debe lanzar un error de duplicado")
def verificar_error_duplicado(error_capturado):
    assert error_capturado is not None
    assert isinstance(error_capturado, ValueError)


@when(parsers.parse("se registra nota {nota:f} en \"{materia}\" del semestre \"{semestre}\""))
def registrar_nota_diferente_semestre(registro, nota, materia, semestre):
    registro.registrar_nota(materia, semestre, nota)


@then("la nota debe quedar registrada correctamente")
def verificar_nota_registrada(registro):
    assert len(registro._notas) >= 1
