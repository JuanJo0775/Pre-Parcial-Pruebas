class RegistroNotas:
    """Clase para gestionar el registro de notas académicas de estudiantes."""

    def __init__(self):
        """Inicializa un nuevo registro de notas."""
        pass

    def registrar_nota(self, materia: str, semestre: str, nota: float) -> None:
        """
        Registra una nota para una materia en un semestre específico.

        Args:
            materia (str): Nombre de la materia.
            semestre (str): Identificador del semestre (ej. '2024-1').
            nota (float): Valor de la nota, debe estar entre 0.0 y 5.0.

        Raises:
            ValueError: Si la nota está fuera del rango permitido.
        """
        if not (0.0 <= nota <= 5.0):
            raise ValueError(f"La nota {nota} está fuera del rango permitido (0.0 - 5.0)")
