import unittest
from unittest.mock import patch
# En test/src/Test_main.py
import sys
import os

# Sube dos niveles: de 'test/src' a la raíz 'Simulador_lanzamiento_dado'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

import src.main as main

class TestMain(unittest.TestCase):

    @patch('src.visualizacion.limpiar_pantalla')
    @patch('builtins.input')
    @patch('builtins.print')
    def test_menu_salir(self, mock_print, mock_input, mock_limpiar):
        """Verifica que la opción 4 termine el programa correctamente."""
        # Simulamos que el usuario presiona '4'
        mock_input.side_effect = ["4"]
        
        main.menu_principal()
        
        # Verificamos que se mostró el mensaje de despedida
        mock_print.assert_any_call("¡Hasta luego!")

    @patch('src.simulador.realizar_sesion')
    @patch('src.estadisticas.calcular_estadisticas')
    @patch('src.visualizacion.mostrar_resultados')
    @patch('builtins.input')
    def test_flujo_nueva_tirada(self, mock_input, mock_viz, mock_stats, mock_sim):
        """Prueba que la opción 1 llame a las funciones de simulación y cálculo."""
        # Simulamos: 1 (Nueva tirada), D6, 2 dados, 5 reps, Enter, 4 (Salir)
        mock_input.side_effect = ["1", "D6", "2", "5", "", "4"]
        
        # Configuramos mocks para que devuelvan valores coherentes
        mock_sim.return_value = [[1, 2]]
        mock_stats.return_value = {"total": 3}

        main.menu_principal()

        # Verificamos que se llamó al simulador con los datos del input
        # Nota: obtener_caras_dado se llama internamente en main
        self.assertTrue(mock_sim.called)
        self.assertTrue(mock_stats.called)
        mock_viz.assert_called_with([[1, 2]])

    @patch('src.persistencia.guardar_historial')
    @patch('builtins.input')
    def test_guardar_sin_datos(self, mock_input, mock_guardar):
        """Verifica que no se intente guardar si no hay una sesión activa."""
        # Simulamos: 3 (Guardar), Enter, 4 (Salir)
        mock_input.side_effect = ["3", "", "4"]
        
        main.menu_principal()
        
        # No debería llamarse a la persistencia porque sesion_actual está vacía
        mock_guardar.assert_not_called()

if __name__ == '__main__':
    unittest.main()