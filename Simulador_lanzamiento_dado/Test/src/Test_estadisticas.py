import unittest
import sys
import os

# Ajuste de ruta para detectar la carpeta 'src'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from src.estadisticas import calcular_estadisticas

class TestEstadisticas(unittest.TestCase):

    def test_calculos_basicos(self):
        """Verifica que los cálculos de suma, media, max y min sean exactos."""
        # Simulamos 2 tiradas de 2 dados cada una
        historial = [[1, 5], [3, 3]] 
        # Sumas por tirada: 6 y 6. Total global: 12. Media: 12/2 = 6.0
        
        resultado = calcular_estadisticas(historial)
        
        self.assertEqual(resultado["total"], 12)
        self.assertEqual(resultado["media"], 6.0)
        self.assertEqual(resultado["maximo"], 6)
        self.assertEqual(resultado["minimo"], 6)
        # Verifica el aplanado de la lista
        self.assertEqual(resultado["valores_planos"], [1, 5, 3, 3])

    def test_sesion_vacia(self):
        """Verifica que el simulador no falle si no hay datos."""
        resultado = calcular_estadisticas([])
        
        self.assertEqual(resultado["total"], 0)
        self.assertEqual(resultado["media"], 0)
        self.assertEqual(resultado["maximo"], 0) # Ahora debería ser 0 en lugar de error
        self.assertEqual(resultado["minimo"], 0)

    def test_media_decimal(self):
        """Verifica que la media se redondee a 2 decimales."""
        historial = [[1, 2], [4, 5], [1, 1]] # Sumas: 3, 9, 2. Total: 14. 
        # Media: 14 / 3 = 4.6666... -> redondeado a 4.67
        
        resultado = calcular_estadisticas(historial)
        self.assertEqual(resultado["media"], 4.67)

if __name__ == '__main__':
    unittest.main()