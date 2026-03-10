import os
from collections import Counter

def limpiar_pantalla():
    """
    Limpia el terminal de comandos detectando el sistema operativo actual.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_histograma(valores):
    """
    Representa gráficamente la frecuencia de los resultados en la consola.

    Args:
        valores (list): Lista simple de enteros con todos los resultados obtenidos.
    """
    frecuencias = Counter(valores)
    if not frecuencias: return
    
    print("\n--- HISTOGRAMA DE FRECUENCIAS ---")
    for valor in sorted(frecuencias.keys()):
        barra = "*" * frecuencias[valor]
        print(f"Valor {valor:2}: {barra} ({frecuencias[valor]})")

def mostrar_resultados(historial):
    """
    Imprime en pantalla el desglose de cada tirada y su suma total.

    Args:
        historial (list): Lista de listas con los resultados de la sesión.
    """
    for i, tirada in enumerate(historial, 1):
        print(f"Tirada {i}: {tirada} -> Suma: {sum(tirada)}")