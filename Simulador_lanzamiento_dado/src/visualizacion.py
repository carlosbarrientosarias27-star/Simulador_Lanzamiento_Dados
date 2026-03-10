import os
from collections import Counter

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo[cite: 136]."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_histograma(valores):
    """Dibuja un histograma de frecuencia usando el carácter '*'[cite: 111, 115]."""
    frecuencias = Counter(valores)
    if not frecuencias: return
    
    max_frecuencia = max(frecuencias.values())
    print("\n--- HISTOGRAMA DE FRECUENCIAS ---")
    for valor in sorted(frecuencias.keys()):
        # Escala las barras proporcionalmente [cite: 112]
        barra = "*" * frecuencias[valor]
        print(f"Valor {valor:2}: {barra} ({frecuencias[valor]})")

def mostrar_resultados(historial):
    """Muestra las tiradas numeradas con enumerate()[cite: 99, 161]."""
    for i, tirada in enumerate(historial, 1):
        print(f"Tirada {i}: {tirada} -> Suma: {sum(tirada)}")