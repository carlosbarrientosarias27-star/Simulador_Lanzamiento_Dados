import unittest
from unittest.mock import patch
import sys
import os

# Buscamos la carpeta raíz del proyecto (subiendo niveles desde donde esté este archivo)
# Si el archivo está en tests/src/tests_main.py, necesitamos subir DOS niveles para llegar a la raíz
ruta_actual = os.path.dirname(os.path.abspath(__file__))
ruta_raiz = os.path.abspath(os.path.join(ruta_actual, '..', '..')) 
ruta_src = os.path.join(ruta_raiz, 'src')

if ruta_src not in sys.path:
    sys.path.append(ruta_src)

# Ahora las importaciones funcionarán porque Python ya conoce la carpeta 'src'
try:
    import simulador
    import estadisticas
except ImportError as e:
    print(f"Error: No se pudo encontrar el módulo. Ruta buscada: {ruta_src}")
    raise e

class TestSimuladorDados(unittest.TestCase):
    # ... (el resto de tus tests igual)
    
    def test_obtener_caras_dado_valido(self):
        """Prueba que el simulador devuelva el número correcto de caras."""
        # Nota: Asegúrate de que en simulador.py la función se llame exactamente así
        self.assertEqual(simulador.obtener_caras_dado("D6"), 6)

    @patch('builtins.input', side_effect=['4'])
    def test_menu_principal_salir(self, mock_input):
        import main
        main.menu_principal()

if __name__ == '__main__':
    unittest.main()