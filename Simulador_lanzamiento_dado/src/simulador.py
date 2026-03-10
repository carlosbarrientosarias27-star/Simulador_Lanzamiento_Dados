import random

def obtener_caras_dado(tipo_dado):
    """Mapea el nombre del dado a su valor numérico de caras[cite: 73]."""
    dados = {
        "D4": 4, "D6": 6, "D8": 8, 
        "D10": 10, "D12": 12, "D20": 20
    }
    return dados.get(tipo_dado.upper())

def lanzar_dados(caras, cantidad):
    """Genera una lista de N lanzamientos usando comprensión de listas[cite: 85]."""
    return [random.randint(1, caras) for _ in range(cantidad)]

def realizar_sesion(caras, cantidad, repeticiones):
    """Ejecuta múltiples tiradas y las almacena en una lista de listas[cite: 92, 98]."""
    historial_sesion = []
    for _ in range(repeticiones):
        tiro = lanzar_dados(caras, cantidad)
        historial_sesion.append(tiro)
    return historial_sesion