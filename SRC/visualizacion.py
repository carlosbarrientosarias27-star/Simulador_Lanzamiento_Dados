import os
from collections import Counter

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo[cite: 134, 136]."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_histograma(resultados_planos):
    """Dibuja un histograma de frecuencias con caracteres de texto[cite: 111, 115]."""
    frecuencias = Counter(resultados_planos)
    print("\nFRECUENCIA DE VALORES:")
    for valor in sorted(frecuencias.keys()):
        barra = "█" * frecuencias[valor]
        print(f"{valor}: {barra} ({frecuencias[valor]})")