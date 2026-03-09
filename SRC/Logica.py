import random

def lanzar_dados(caras, cantidad):
    """
    Simula el lanzamiento de una cantidad específica de dados de N caras.
    
    Args:
        caras (int): Número de caras del dado (D4, D6, etc.).
        cantidad (int): Cuántos dados se lanzan a la vez (1-10).
        
    Returns:
        list: Una lista con los resultados enteros de cada dado.
    """
    # Se utiliza random.randint para generar un número entre 1 y el número de caras.
    return [random.randint(1, caras) for _ in range(cantidad)]

def realizar_serie_tiradas(caras, cantidad, repeticiones):
    """
    Ejecuta una serie de tiradas automáticas y almacena los resultados.
    
    Args:
        caras (int): Número de caras de los dados seleccionados.
        cantidad (int): Cantidad de dados por cada tirada.
        repeticiones (int): Cuántas veces se repite el proceso (1-20).
        
    Returns:
        list: Una lista de listas que contiene el historial de la sesión.
    """
    return [lanzar_dados(caras, cantidad) for _ in range(repeticiones)]