from visualizacion import limpiar_pantalla, mostrar_histograma
from logica import realizar_serie_tiradas
from estadisticas import calcular_estadisticas
from persistencia import guardar_en_historial

def mostrar_bienvenida():
    """Muestra el título del programa y los dados disponibles."""
    print("==========================================")
    print("🎲 SIMULADOR DE LANZAMIENTO DE DADOS 🎲")
    print("==========================================")
    print("Dados disponibles: D4, D6, D8, D10, D12, D20\n")

def menu():
    """Bucle principal con el menú de opciones requerido."""
    dados_validos = {"D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20}
    # Variable para almacenar los datos de la última tirada realizada
    ultima_tirada = None

    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        print("1. Nueva tirada")
        print("2. Ver historial de esta sesión (última tirada)")
        print("3. Guardar última tirada en archivo")
        print("4. Salir")
        
        opcion = input("\nSelecciona una opción (1-4): ")

        if opcion == "1":
            tipo = input("Elige un tipo de dado: ").upper()
            if tipo not in dados_validos:
                print("❌ Tipo de dado no válido.")
                input("Enter para continuar...")
                continue

            try:
                n_dados = int(input("¿Cuántos dados? (1-10): "))
                n_reps = int(input("¿Cuántas tiradas? (1-20): "))

                if 1 <= n_dados <= 10 and 1 <= n_reps <= 20:
                    # Lógica y Estadísticas
                    resultados = realizar_serie_tiradas(dados_validos[tipo], n_dados, n_reps)
                    stats = calcular_estadisticas(resultados)
                    
                    # Guardamos en memoria para las opciones 2 y 3
                    ultima_tirada = {
                        "tipo": tipo,
                        "n_dados": n_dados,
                        "resultados": resultados,
                        "stats": stats
                    }

                    # Visualización inmediata
                    print("\n--- RESULTADOS ---")
                    for i, t in enumerate(resultados, 1):
                        print(f"Tirada {i}: {t} -> Suma: {sum(t)}")
                    
                    valores_planos = [d for tirada in resultados for d in tirada]
                    mostrar_histograma(valores_planos)
                else:
                    print("❌ Cantidades fuera de rango.")
            except ValueError:
                print("❌ Introduce números enteros válidos.")
            input("\nPresiona Enter para volver al menú...")

        elif opcion == "2":
            if ultima_tirada:
                print(f"\nÚltima configuración: {ultima_tirada['n_dados']} {ultima_tirada['tipo']}")
                print(f"Resultados: {ultima_tirada['resultados']}")
            else:
                print("\n⚠️ No se han realizado tiradas en esta sesión.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            if ultima_tirada:
                ruta = guardar_en_historial(
                    ultima_tirada['tipo'], 
                    ultima_tirada['n_dados'], 
                    ultima_tirada['resultados'], 
                    ultima_tirada['stats']
                )
                print(f"✅ Guardado con éxito en: {ruta}")
            else:
                print("\n⚠️ No hay datos para guardar. Realiza una tirada primero.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            print("¡Gracias por usar el simulador!🎲")
            break
        
        else:
            print("❌ Opción no válida.")
            input("Presiona Enter para reintentar...")

if __name__ == "__main__":
    menu()