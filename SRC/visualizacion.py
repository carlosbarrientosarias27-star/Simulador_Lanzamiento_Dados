import os
from collections import Counter

def limpiar_pantalla():
    """
    Limpia la terminal según el sistema operativo (Windows o Linux/Mac).
    [cite: 134, 136]
    """
    # 'cls' para Windows (nt), 'clear' para sistemas basados en Unix
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_histograma(resultados_planos):
    """
    Dibuja un histograma de frecuencias en la terminal usando el carácter '█'.
    Escala las barras proporcionalmente al valor más frecuente.
    [cite: 111, 112, 115]
    """
    if not resultados_planos:
        print("No hay datos para mostrar el histograma.")
        return

    # Contamos la frecuencia de cada valor obtenido [cite: 116]
    frecuencias = Counter(resultados_planos)
    
    # Identificamos la frecuencia máxima para el escalado 
    max_frecuencia = max(frecuencias.values())
    ancho_maximo = 20  # Definimos un ancho máximo de barra para que no se rompa la terminal

    print("\n--- FRECUENCIA DE VALORES ---")
    
    # Ordenamos los valores de menor a mayor (del 1 al máximo del dado)
    for valor in sorted(frecuencias.keys()):
        frec = frecuencias[valor]
        
        # Cálculo del escalado proporcional 
        # (Frecuencia actual / Frecuencia máxima) * Ancho máximo deseado
        longitud_barra = int((frec / max_frecuencia) * ancho_maximo)
        
        # Usamos el carácter '█' para representar la barra [cite: 111, 154]
        barra = "█" * (longitud_barra if longitud_barra > 0 else 1)
        
        print(f"Valor {valor:2}: {barra} ({frec})")