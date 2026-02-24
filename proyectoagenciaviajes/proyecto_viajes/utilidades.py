
# Funciones auxiliares compartidas entre módulos.

def input_seguro(prompt=""):
    """
    Lee entrada del usuario. Captura Ctrl+C (KeyboardInterrupt) y EOF.
    Devuelve None si el usuario cancela la entrada.
    """
    try:
        return input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
