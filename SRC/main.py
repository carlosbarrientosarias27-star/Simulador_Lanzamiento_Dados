import os
import sys

from SRC.visualizacion import limpiar_pantalla, mostrar_histograma
from SRC.logica import realizar_serie_tiradas
from SRC.estadisticas import calcular_estadisticas

def menu():
    """Bucle principal del simulador[cite: 129, 133]."""
    dados_validos = { "D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20 }
    
    while True:
        limpiar_pantalla()
        print("--- SIMULADOR DE DADOS ---")
        # Aquí iría la lógica de pedir datos al usuario (input) [cite: 157-160]
        # Y llamar a las funciones de los otros archivos.
        
        opcion = input("\n¿Nueva tirada? (s/n): ")
        if opcion.lower() != 's':
            break

if __name__ == "__main__":
    menu()