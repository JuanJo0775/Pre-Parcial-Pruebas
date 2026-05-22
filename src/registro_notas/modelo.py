class RegistroNotas:
    """Clase para gestionar el registro de notas académicas de estudiantes."""

    def __init__(self):
        """Inicializa un nuevo registro de notas."""
        self._notas = {}

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
        self._notas[(materia, semestre)] = nota

    def aprueba(self, materia: str, semestre: str) -> bool:
        """
        Consulta si una materia ha sido aprobada en un semestre.

        Args:
            materia (str): Nombre de la materia.
            semestre (str): Identificador del semestre.

        Returns:
            bool: True si la nota es >= 3.0, False de lo contrario.

        Raises:
            KeyError: Si no hay nota registrada para la materia en el semestre.
        """
        clave = (materia, semestre)
        if clave not in self._notas:
            raise KeyError(f"No hay nota registrada para '{materia}' en '{semestre}'")
        return self._notas[clave] >= 3.0

    def promedio(self) -> float:
        """
        Calcula el promedio de todas las notas registradas.

        Returns:
            float: Promedio de las notas, o 0.0 si no hay notas registradas.
        """
        if not self._notas:
            return 0.0
        return sum(self._notas.values()) / len(self._notas)
