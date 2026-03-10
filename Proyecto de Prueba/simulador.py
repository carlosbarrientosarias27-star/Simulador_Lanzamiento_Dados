import random
import os
from datetime import datetime
from collections import Counter

def limpiar_pantalla():
    """Limpia la terminal según el sistema operativo[cite: 134, 136]."""
    os.system('cls' if os.name == 'nt' else 'clear')

def mostrar_bienvenida():
    """Muestra el encabezado del programa[cite: 134, 156]."""
    print("=" * 40)
    print("  🎲 SIMULADOR DE LANZAMIENTO DE DADOS 🎲  ")
    print("=" * 40)

def obtener_tipo_dado():
    """Permite al usuario elegir un tipo de dado válido[cite: 68, 73]."""
    dados_validos = {"D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20}
    print(f"Tipos disponibles: {' '.join(dados_validos.keys())}")
    
    while True:
        seleccion = input("Elige un tipo de dado: ").upper()
        if seleccion in dados_validos:
            return dados_validos[seleccion], seleccion
        print("❌ Error: Tipo de dado no válido. Intenta de nuevo.")

def solicitar_entero(mensaje, minimo, maximo):
    """Valida que la entrada sea un entero dentro de un rango[cite: 70, 83]."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(f"❌ Debe ser un número entre {minimo} y {maximo}.")
        except ValueError:
            print("❌ Entrada inválida. Por favor, introduce un número.")

def generar_histograma(todos_los_dados):
    """Representa la frecuencia de los valores con barras de texto[cite: 107, 111, 115]."""
    print("\n📊 FRECUENCIA DE VALORES (HISTOGRAMA)")
    frecuencias = Counter(todos_los_dados)
    if not frecuencias:
        return
    
    max_frecuencia = max(frecuencias.values())
    # Ordenar por el valor del dado para la visualización
    for valor in sorted(frecuencias.keys()):
        barra = "█" * frecuencias[valor]
        print(f"Valor {valor}: {barra} ({frecuencias[valor]})")

def mostrar_estadisticas(historial_sesion):
    """Calcula y muestra media, máximo, mínimo y suma total[cite: 16, 104, 181]."""
    if not historial_sesion:
        return

    sumas_tiradas = [sum(tirada) for tirada in historial_sesion]
    total_global = sum(sumas_tiradas)
    media = total_global / len(sumas_tiradas)
    max_valor = max(sumas_tiradas)
    min_valor = min(sumas_tiradas)

    # Identificar en qué tiradas ocurrieron los hitos [cite: 104]
    indices_max = [i + 1 for i, v in enumerate(sumas_tiradas) if v == max_valor]
    indices_min = [i + 1 for i, v in enumerate(sumas_tiradas) if v == min_valor]

    print("\n" + "=" * 15 + " ESTADÍSTICAS " + "=" * 15)
    print(f"Suma total:     {total_global}")
    print(f"Media/tirada:   {media:.2f}")
    print(f"Máximo:         {max_valor} (Tirada/s: {', '.join(map(str, indices_max))})")
    print(f"Mínimo:         {min_valor} (Tirada/s: {', '.join(map(str, indices_min))})")

def guardar_historial(tipo_nombre, num_dados, historial_sesion):
    """Guarda los resultados en la carpeta historial/ con marca de tiempo[cite: 125, 128]."""
    if not os.path.exists('historial'):
        os.makedirs('historial')

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nombre_archivo = f"historial/tiradas_{timestamp}.txt"

    try:
        with open(nombre_archivo, 'w', encoding='utf-8') as f:
            f.write(f"SIMULADOR DE DADOS - {datetime.now()}\n")
            f.write(f"Tipo de dado: {tipo_nombre} | Cantidad: {num_dados}\n")
            f.write("-" * 40 + "\n")
            for i, tirada in enumerate(historial_sesion, 1):
                f.write(f"Tirada {i}: {tirada} | Suma: {sum(tirada)}\n")
        print(f"\n✅ Historial guardado correctamente en: {nombre_archivo}")
    except Exception as e:
        print(f"❌ Error al guardar el archivo: {e}")

def simulador_principal():
    """Bucle principal de ejecución del programa[cite: 129, 133]."""
    historial_acumulado = []
    
    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        # 1. Configuración de la tirada
        caras, nombre_dado = obtener_tipo_dado()
        num_dados = solicitar_entero(f"¿Cuántos dados? (1-10): ", 1, 10)
        num_tiradas = solicitar_entero(f"¿Cuántas tiradas? (1-20): ", 1, 20)
        
        sesion_actual = []
        todos_los_dados_planos = []

        # 2. Ejecución de lanzamientos [cite: 81, 92]
        print("\n🎲 LANZANDO...")
        for i in range(1, num_tiradas + 1):
            # Uso de random.randint para cada dado [cite: 56, 60]
            tirada = [random.randint(1, caras) for _ in range(num_dados)]
            sesion_actual.append(tirada)
            todos_los_dados_planos.extend(tirada)
            
            # Formato visual similar al ejemplo [cite: 161, 165]
            dados_str = " ".join([f"[{d}]" for d in tirada])
            print(f"Tirada {i}:  {dados_str}  →  Suma: {sum(tirada)}")

        # 3. Mostrar resultados de la serie
        mostrar_estadisticas(sesion_actual)
        generar_histograma(todos_los_dados_planos)
        
        # 4. Opciones de guardado y salida [cite: 124, 129]
        print("\n" + "-" * 40)
        opcion = input("¿Deseas guardar esta sesión? (s/n): ").lower()
        if opcion == 's':
            guardar_historial(nombre_dado, num_dados, sesion_actual)
        
        continuar = input("\n¿Realizar otra serie de lanzamientos? (s/n): ").lower()
        if continuar != 's':
            print("¡Gracias por usar el simulador! 👋")
            break

if __name__ == "__main__":
    simulador_principal()