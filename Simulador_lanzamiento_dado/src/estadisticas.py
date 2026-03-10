def calcular_estadisticas(historial_sesion):
    """
    Calcula métricas estadísticas generales de la sesión de lanzamientos.

    Args:
        historial_sesion (list): Lista de listas, donde cada sublista contiene los 
                                 resultados de una tirada individual.

    Returns:
        dict: Diccionario con la suma total, media de la sesión, valor máximo, 
              valor mínimo y la lista aplanada de todos los resultados.
    """
    todos_los_valores = [valor for tirada in historial_sesion for valor in tirada]
    sumas_por_tirada = [sum(tirada) for tirada in historial_sesion]
    
    total = sum(todos_los_valores)
    media = total / len(historial_sesion) if historial_sesion else 0
    
    # Manejo de listas vacías para evitar ValueError
    max_valor = max(sumas_por_tirada) if sumas_por_tirada else 0
    min_valor = min(sumas_por_tirada) if sumas_por_tirada else 0
    
    return {
        "total": total,
        "media": round(media, 2),
        "maximo": max_valor,
        "minimo": min_valor,
        "valores_planos": todos_los_valores
    }