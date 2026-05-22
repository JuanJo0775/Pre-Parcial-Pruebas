class RegistroNotas:
    def __init__(self):
        pass

    def registrar_nota(self, materia: str, semestre: str, nota: float) -> None:
        if nota < 0.0 or nota > 5.0:
            raise ValueError()
