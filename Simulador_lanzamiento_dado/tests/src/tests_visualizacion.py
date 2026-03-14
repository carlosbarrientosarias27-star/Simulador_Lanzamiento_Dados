import unittest
from io import StringIO
from unittest.mock import patch
import sys
import os

# Subimos DOS niveles para llegar a la raíz del proyecto: "Simulador_lanzamiento_dado"
# Desde ahí, Python podrá ver la carpeta /src/ donde está visualizacion.py
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ruta_raiz)

# Ahora el import debería funcionar
from src.visualizacion import mostrar_histograma, mostrar_resultados

class TestVisualizacion(unittest.TestCase):

    def test_mostrar_resultados_formato(self):
        """Verifica que mostrar_resultados imprima el formato esperado."""
        historial = [(1, 2), (3, 4)]
        # Capturamos la salida de la consola
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mostrar_resultados(historial)
            output = fake_out.getvalue()
            
            self.assertIn("Tirada 1: (1, 2) -> Suma: 3", output)
            self.assertIn("Tirada 2: (3, 4) -> Suma: 7", output)

    def test_mostrar_histograma_vacio(self):
        """Verifica que no explote si se le pasan valores vacíos."""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mostrar_histograma([])
            self.assertEqual(fake_out.getvalue(), "")

    def test_mostrar_histograma_frecuencia(self):
        """Verifica que el histograma dibuje los asteriscos correctos."""
        valores = [5, 5, 5]
        with patch('sys.stdout', new=StringIO()) as fake_out:
            mostrar_histograma(valores)
            output = fake_out.getvalue()
            # El valor 5 debe tener 3 asteriscos
            self.assertIn("Valor  5: *** (3)", output)

    @patch('os.system')
    def test_limpiar_pantalla(self, mock_system):
        """Prueba que os.system se llame para limpiar la consola."""
        from src.visualizacion import limpiar_pantalla
        limpiar_pantalla()
        self.assertTrue(mock_system.called)

if __name__ == '__main__':
    unittest.main()