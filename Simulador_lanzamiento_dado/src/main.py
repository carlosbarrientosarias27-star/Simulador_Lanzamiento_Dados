# En src/main.py
import simulador
import estadisticas
import visualizacion
import persistencia
def menu_principal():
    """
    Gestiona el flujo principal del programa y la interfaz de usuario por consola.
    """
    sesion_actual = []
    stats_actuales = {}
    config_actual = {}

    while True:
        visualizacion.limpiar_pantalla()
        print("=== SIMULADOR DE LANZAMIENTO DE DADOS ===")
        print("1. Nueva tirada")
        print("2. Ver estadísticas y gráfico")
        print("3. Guardar sesión")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")

        if opcion == "1":
            tipo = input("Tipo de dado (D4, D6, D8, D10, D12, D20): ").upper()
            caras = simulador.obtener_caras_dado(tipo)
            if not caras:
                print("Error: Dado no válido."); input(); continue
                
            cant = int(input("¿Cuántos dados? (1-10): "))
            reps = int(input("¿Cuántas tiradas? (1-20): "))
            
            config_actual = {"tipo": tipo, "cantidad": cant, "repeticiones": reps}
            sesion_actual = simulador.realizar_sesion(caras, cant, reps)
            stats_actuales = estadisticas.calcular_estadisticas(sesion_actual)
            
            visualizacion.mostrar_resultados(sesion_actual)
            input("\nPresione Enter para continuar...")

        elif opcion == "2":
            if not sesion_actual:
                print("No hay datos en esta sesión."); input(); continue
            print(f"\nESTADÍSTICAS: {stats_actuales}")
            visualizacion.mostrar_histograma(stats_actuales['valores_planos'])
            input("\nPresione Enter para volver...")

        elif opcion == "3":
            if not sesion_actual:
                print("Nada que guardar."); input(); continue
            nombre = persistencia.guardar_historial(sesion_actual, stats_actuales, config_actual)
            print(f"Guardado exitoso: {nombre}")
            input(); 

        elif opcion == "4":
            print("¡Hasta luego!"); break

if __name__ == "__main__":
    menu_principal()