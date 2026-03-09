import os
from datetime import datetime

def guardar_en_historial(tipo_dado, cantidad_dados, todas_las_tiradas, estadisticas):
    """
    Guarda el historial completo de la sesión en un archivo de texto.
    
    Args:
        tipo_dado (str): El tipo de dado usado (ej: D6).
        cantidad_dados (int): Número de dados por tirada.
        todas_las_tiradas (list): Lista de listas con los resultados.
        estadisticas (dict): Diccionario con los cálculos de la sesión.
    """
    # 1. Crear nombre dinámico basado en fecha y hora [cite: 125, 128]
    ahora = datetime.now()
    nombre_historial = ahora.strftime("tiradas_%Y%m%d_%H%M%S.txt")
    
    # 2. Asegurar que la ruta apunte a la carpeta historial/ [cite: 34]
    ruta_completa = os.path.join("historial", nombre_historial)
    
    # 3. Formatear el contenido a escribir detalladamente [cite: 126]
    contenido = [
        "--- HISTORIAL DE LANZAMIENTO DE DADOS ---",
        f"Fecha: {ahora.strftime('%Y-%m-%d %H:%M:%S')}",
        f"Configuración: {cantidad_dados} dados tipo {tipo_dado}\n",
        "DETALLE DE TIRADAS:"
    ]
    
    for i, tirada in enumerate(todas_las_tiradas, 1):
        contenido.append(f"Tirada {i}: {tirada} -> Suma: {sum(tirada)}")
    
    contenido.extend([
        "\nESTADÍSTICAS GLOBALES:",
        f"Suma total: {estadisticas['total']}",
        f"Media/tirada: {estadisticas['media']:.2f}",
        f"Máximo: {estadisticas['maximo']}",
        f"Mínimo: {estadisticas['minimo']}",
        "------------------------------------------"
    ])
    
    # 4. Escribir en el archivo [cite: 128]
    with open(ruta_completa, "w", encoding="utf-8") as f:
        f.write("\n".join(contenido))
        
    return ruta_completa