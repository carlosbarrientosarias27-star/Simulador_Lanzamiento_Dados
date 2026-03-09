import sys
from visualizacion import limpiar_pantalla, mostrar_histograma
from logica import realizar_serie_tiradas
from estadisticas import calcular_estadisticas
from persistencia import guardar_en_historial

def mostrar_bienvenida():
    """Muestra el título y los dados disponibles."""
    print("==========================================")
    print("🎲 SIMULADOR DE LANZAMIENTO DE DADOS 🎲")
    print("==========================================")
    print("Dados disponibles: D4, D6, D8, D10, D12, D20\n")

def ejecutar_simulacion(dados_validos):
    """Lógica para la opción 'Nueva tirada'."""
    tipo = input("Elige un tipo de dado: ").upper()
    if tipo not in dados_validos:
        print("❌ Error: Tipo de dado no válido.")
        return None

    try:
        n_dados = int(input("¿Cuántos dados? (1-10): "))
        n_tiradas = int(input("¿Cuántas tiradas? (1-20): "))

        if not (1 <= n_dados <= 10 and 1 <= n_tiradas <= 20):
            print("❌ Cantidades fuera de rango.")
            return None

        # Ejecución
        resultados = realizar_serie_tiradas(dados_validos[tipo], n_dados, n_tiradas)
        
        # Mostrar resultados individuales
        print("\n--- RESULTADOS ---")
        for i, tirada in enumerate(resultados, 1):
            print(f"Tirada {i}: {tirada} -> Suma: {sum(tirada)}")

        # Estadísticas e Histograma
        stats = calcular_estadisticas(resultados)
        print(f"\nSuma total: {stats['total']} | Media: {stats['media']:.2f}")
        
        valores_planos = [d for t in resultados for d in t]
        mostrar_histograma(valores_planos)
        
        return {"tipo": tipo, "n": n_dados, "res": resultados, "stats": stats}

    except ValueError:
        print("❌ Error: Introduce números enteros.")
        return None

def menu():
    """Bucle principal con las opciones requeridas."""
    dados_validos = {"D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20}
    ultima_sesion = None

    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        print("1. Nueva tirada")
        print("2. Ver resultados de la última tirada")
        print("3. Guardar en historial")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción: ")

        if opcion == "1":
            ultima_sesion = ejecutar_simulacion(dados_validos)
            input("\nPresiona Enter para volver al menú...")
        
        elif opcion == "2":
            if ultima_sesion:
                print(f"\nÚltima tirada ({ultima_sesion['tipo']}): {ultima_sesion['res']}")
            else:
                print("\n⚠️ No hay datos en esta sesión aún.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            if ultima_sesion:
                ruta = guardar_en_historial(
                    ultima_sesion['tipo'], 
                    ultima_sesion['n'], 
                    ultima_sesion['res'], 
                    ultima_sesion['stats']
                )
                print(f"✅ Guardado en: {ruta}")
            else:
                print("\n⚠️ Nada que guardar.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            print("¡Hasta luego! 🎲")
            break
        
        else:
            print("❌ Opción no válida.")
            input("\nPresiona Enter para reintentar...")

if __name__ == "__main__":
    menu()