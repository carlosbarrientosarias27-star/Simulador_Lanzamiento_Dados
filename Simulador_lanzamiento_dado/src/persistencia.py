import datetime
import os

def guardar_historial(datos_sesion, estadisticas, config):
    """
    Exporta los resultados de la sesión a un archivo de texto en la carpeta 'Historial'.

    Args:
        datos_sesion (list): Historial de tiradas realizadas.
        estadisticas (dict): Diccionario con los cálculos procesados de la sesión.
        config (dict): Configuración utilizada (tipo de dado, cantidad y repeticiones).

    Returns:
        str: Nombre del archivo generado con marca de tiempo.
    """
    ruta_Historial = "Historial"
    if not os.path.exists(ruta_Historial):
        os.makedirs(ruta_Historial)
        
    fecha_str = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"tiradas_{fecha_str}.txt"
    ruta_archivo = os.path.join(ruta_Historial, nombre_archivo)
    
    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(f"SIMULACIÓN DE DADOS - {fecha_str}\n")
        f.write(f"Configuración: {config['cantidad']} {config['tipo']} x {config['repeticiones']} veces\n")
        f.write("-" * 30 + "\n")
        for i, t in enumerate(datos_sesion, 1):
            f.write(f"Tirada {i}: {t} (Suma: {sum(t)})\n")
        f.write("-" * 30 + "\n")
        f.write(f"Estadísticas: {estadisticas}\n")
        
    return nombre_archivo