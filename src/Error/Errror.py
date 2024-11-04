class MyCustomError(Exception):
    """Clase de excepción personalizada."""
    def __init__(self, message):
        super().__init__(message)