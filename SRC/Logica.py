import random

def lanzar_dados(caras, cantidad):
    """Genera una lista de resultados de dados[cite: 85, 143]."""
    return [random.randint(1, caras) for _ in range(cantidad)]

def realizar_serie_tiradas(caras, cantidad, repeticiones):
    """Ejecuta múltiples tiradas y las guarda en una lista de listas[cite: 92, 98]."""
    return [lanzar_dados(caras, cantidad) for _ in range(repeticiones)]