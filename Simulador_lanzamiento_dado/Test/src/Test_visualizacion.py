import unittest
from unittest.mock import patch
import sys
import os
import io

# 1. Configuración de rutas (Ruta absoluta para evitar confusiones)
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_raiz = os.path.abspath(os.path.join(directorio_actual, '..'))

# Añadimos la raíz y la carpeta 'src' al path de búsqueda
if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)
ruta_src = os.path.join(directorio_raiz, 'src')
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

# 2. Importación protegida
try:
    from Simulador_lanzamiento_dado.src.visualizacion import limpiar_pantalla, mostrar_histograma
except ImportError:
    # Intento alternativo si los archivos están estrictamente en src/
    from Simulador_lanzamiento_dado.src.visualizacion import limpiar_pantalla, mostrar_histograma

class TestVisualizacion(unittest.TestCase):

    @patch('os.system')
    def test_limpiar_pantalla_windows(self, mock_system):
        """Verifica que se use 'cls' si el sistema simulado es Windows (nt)."""
        with patch('os.name', 'nt'):
            limpiar_pantalla()
            mock_system.assert_called_once_with('cls')

    @patch('os.system')
    def test_limpiar_pantalla_unix(self, mock_system):
        """Verifica que se use 'clear' en sistemas Linux/Mac."""
        with patch('os.name', 'posix'):
            limpiar_pantalla()
            mock_system.assert_called_once_with('clear')

    def test_histograma_vacio(self):
        """Verifica el mensaje cuando no hay datos para el histograma."""
        captura_salida = io.StringIO()
        with patch('sys.stdout', captura_salida):
            mostrar_histograma([])
        self.assertIn("No hay datos", captura_salida.getvalue())

    def test_histograma_con_datos(self):
        """Verifica la impresión de frecuencias y el carácter '█'."""
        captura_salida = io.StringIO()
        with patch('sys.stdout', captura_salida):
            # Simulamos datos: tres 1s y un 2
            mostrar_histograma([1, 1, 1, 2])
        
        salida = captura_salida.getvalue()
        self.assertIn("FRECUENCIA DE VALORES", salida)
        self.assertIn("Valor  1", salida)
        self.assertIn("█", salida)

if __name__ == "__main__":
    unittest.main(verbosity=2)