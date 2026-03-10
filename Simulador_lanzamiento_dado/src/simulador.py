import random

def obtener_caras_dado(tipo_dado):
    """
    Mapea el nombre corto de un dado a su número de caras correspondiente.

    Args:
        tipo_dado (str): Identificador del dado (ej. 'D6', 'D20').

    Returns:
        int: Número de caras del dado o None si el tipo no es válido.
    """
    dados = {
        "D4": 4, "D6": 6, "D8": 8, 
        "D10": 10, "D12": 12, "D20": 20
    }
    return dados.get(tipo_dado.upper())

def lanzar_dados(caras, cantidad):
    """
    Simula el lanzamiento de una cantidad específica de dados.

    Args:
        caras (int): Número de caras del dado a lanzar.
        cantidad (int): Cuántos dados se deben lanzar simultáneamente.

    Returns:
        list: Lista de enteros con los resultados de cada dado.
    """
    return [random.randint(1, caras) for _ in range(cantidad)]

def realizar_sesion(caras, cantidad, repeticiones):
    """
    Ejecuta una serie de múltiples tiradas de dados.

    Args:
        caras (int): Número de caras del dado.
        cantidad (int): Cantidad de dados por tirada.
        repeticiones (int): Número de veces que se repetirá el lanzamiento.

    Returns:
        list: Matriz (lista de listas) con el historial completo de la sesión.
    """
    historial_sesion = []
    for _ in range(repeticiones):
        tiro = lanzar_dados(caras, cantidad)
        historial_sesion.append(tiro)
    return historial_sesion