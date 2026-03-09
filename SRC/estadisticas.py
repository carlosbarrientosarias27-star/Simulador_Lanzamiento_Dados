def calcular_estadisticas(todas_las_tiradas):
    """
    Calcula estadísticas detalladas sobre todas las tiradas de la sesión.
    
    Args:
        todas_las_tiradas (list): Una lista de listas, donde cada sublista 
                                  contiene los resultados de una tirada.
    Returns:
        dict: Diccionario con total, media, máximo, mínimo y sus índices.
    """
    # Calculamos la suma de cada tirada individual
    sumas_por_tirada = [sum(tirada) for tirada in todas_las_tiradas]
    
    total_global = sum(sumas_por_tirada) 
    media = total_global / len(todas_las_tiradas) 
    
    # Obtenemos los valores máximo y mínimo 
    valor_maximo = max(sumas_por_tirada)
    valor_minimo = min(sumas_por_tirada)
    
    # Identificamos en qué tirada (número) ocurrió el máximo y mínimo 
    # Usamos i + 1 porque las tiradas se muestran al usuario empezando en 1 
    indices_max = [i + 1 for i, v in enumerate(sumas_por_tirada) if v == valor_maximo]
    indices_min = [i + 1 for i, v in enumerate(sumas_por_tirada) if v == valor_minimo]
    
    return {
        "total": total_global,
        "media": media,
        "maximo": valor_maximo,
        "minimo": valor_minimo,
        "tiradas_max": indices_max,
        "tiradas_min": indices_min,
        "sumas": sumas_por_tirada
    }