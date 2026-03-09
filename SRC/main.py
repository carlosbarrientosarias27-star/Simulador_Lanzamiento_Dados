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

def ejecutar_caso_prueba(tipo, n_dados, n_reps, dados_validos):
    """Función auxiliar para ejecutar y mostrar casos específicos sin input manual."""
    print(f"\n🚀 EJECUTANDO PRUEBA: {n_reps} tiradas de {n_dados}{tipo}...")
    
    resultados = realizar_serie_tiradas(dados_validos[tipo], n_dados, n_reps)
    stats = calcular_estadisticas(resultados)
    
    # Mostrar resumen rápido
    for i, t in enumerate(resultados[:5], 1): # Solo mostramos las primeras 5 para no saturar
        print(f"  Tirada {i}: {t} -> Suma: {sum(t)}")
    if n_reps > 5: print(f"  ... ({n_reps - 5} tiradas más)")
    
    valores_planos = [d for tirada in resultados for d in tirada]
    mostrar_histograma(valores_planos)
    
    return {
        "tipo": tipo,
        "n_dados": n_dados,
        "resultados": resultados,
        "stats": stats
    }

def menu():
    """Bucle principal con el menú de opciones requerido."""
    dados_validos = {"D4": 4, "D6": 6, "D8": 8, "D10": 10, "D12": 12, "D20": 20}
    ultima_tirada = None

    while True:
        limpiar_pantalla()
        mostrar_bienvenida()
        
        print("1. Nueva tirada (Manual)")
        print("2. Ver historial de esta sesión")
        print("3. Guardar última tirada en archivo")
        print("4. Ejecutar Casos Edge (Pruebas automáticas)")
        print("5. Salir")
        
        opcion = input("\nSelecciona una opción (1-5): ")

        if opcion == "1":
            # ... (Mantiene tu lógica original de input manual)
            tipo = input("Elige un tipo de dado: ").upper()
            if tipo not in dados_validos:
                print("❌ Tipo de dado no válido.")
                input("Enter para continuar...")
                continue
            try:
                n_dados = int(input("¿Cuántos dados? (1-10): "))
                n_reps = int(input("¿Cuántas tiradas? (1-20): "))
                if 1 <= n_dados <= 10 and 1 <= n_reps <= 20:
                    ultima_tirada = ejecutar_caso_prueba(tipo, n_dados, n_reps, dados_validos)
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
                print("\n⚠️ No se han realizado tiradas.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "3":
            if ultima_tirada:
                ruta = guardar_en_historial(
                    ultima_tirada['tipo'], 
                    ultima_tirada['n_dados'], 
                    ultima_tirada['resultados'], 
                    ultima_tirada['stats']
                )
                print(f"✅ Guardado en: {ruta}")
            else:
                print("\n⚠️ Nada que guardar.")
            input("\nPresiona Enter para continuar...")

        elif opcion == "4":
            print("\n--- INICIANDO TESTS DE BORDES ---")
            
            # Caso 1: Mínimo absoluto (1 dado D4, 1 tirada)
            print("\n[TEST 1] Límite Inferior")
            ultima_tirada = ejecutar_caso_prueba("D4", 1, 1, dados_validos)
            
            # Caso 2: Máximo de dados (10 dados D20, 5 tiradas)
            print("\n[TEST 2] Límite Superior de Dados")
            ultima_tirada = ejecutar_caso_prueba("D20", 10, 5, dados_validos)
            
            # Caso 3: Máximo de repeticiones (1 dado D6, 20 tiradas)
            print("\n[TEST 3] Límite Superior de Repeticiones")
            ultima_tirada = ejecutar_caso_prueba("D6", 1, 20, dados_validos)
            
            print("\n✅ Pruebas finalizadas. La última prueba quedó en memoria.")
            input("\nPresiona Enter para volver al menú...")

        elif opcion == "5":
            print("¡Gracias por usar el simulador!🎲")
            break
        
        else:
            print("❌ Opción no válida.")
            input("Presiona Enter para reintentar...")

if __name__ == "__main__":
    menu()