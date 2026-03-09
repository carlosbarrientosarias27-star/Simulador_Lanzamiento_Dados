from datetime import datetime
import os

def guardar_en_archivo(datos_texto):
    """Guarda el historial con nombre dinámico por fecha y hora[cite: 125, 128]."""
    fecha_hora = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"historial/tiradas_{fecha_hora}.txt"
    
    with open(nombre_archivo, "w", encoding="utf-8") as f:
        f.write(datos_texto)
    return nombre_archivo