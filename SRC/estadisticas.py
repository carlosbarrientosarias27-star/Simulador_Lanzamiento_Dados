def calcular_estadisticas(todas_las_tiradas):
    """Calcula suma, media, máximo y mínimo de la sesión[cite: 104, 106]."""
    sumas_por_tirada = [sum(tirada) for tirada in todas_las_tiradas]
    
    total_global = sum(sumas_por_tirada)
    media = total_global / len(todas_las_tiradas)
    maximo = max(sumas_por_tirada)
    minimo = min(sumas_por_tirada)
    
    return {
        "total": total_global,
        "media": media,
        "maximo": maximo,
        "minimo": minimo,
        "sumas": sumas_por_tirada
    }