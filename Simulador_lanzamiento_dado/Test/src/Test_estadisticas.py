import unittest
import sys
import os

# 1. Configuración de rutas para encontrar la carpeta 'src'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_raiz = os.path.abspath(os.path.join(directorio_actual, '..'))

if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)
ruta_src = os.path.join(directorio_raiz, 'src')
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

# 2. Importación del módulo
try:
    from estadisticas import calcular_estadisticas
except ImportError:
    from SRC.estadisticas import calcular_estadisticas

class TestEstadisticas(unittest.TestCase):

    def setUp(self):
        """Preparamos datos de prueba consistentes."""
        # Tirada 1: suma 10 | Tirada 2: suma 20 | Tirada 3: suma 15
        self.datos_prueba = [[5, 5], [10, 10], [7, 8]]
        self.stats = calcular_estadisticas(self.datos_prueba)

    def test_calculo_total_y_media(self):
        """Verifica que la suma global y el promedio sean exactos."""
        # Total: 10 + 20 + 15 = 45
        # Media: 45 / 3 = 15.0
        self.assertEqual(self.stats['total'], 45)
        self.assertEqual(self.stats['media'], 15.0)

    def test_maximos_y_minimos(self):
        """Verifica que identifique correctamente los valores extremos."""
        self.assertEqual(self.stats['maximo'], 20)
        self.assertEqual(self.stats['minimo'], 10)

    def test_indices_tiradas(self):
        """Verifica que los índices de tirada coincidan (empezando en 1)."""
        # El máximo (20) está en la segunda tirada -> [2]
        # El mínimo (10) está en la primera tirada -> [1]
        self.assertEqual(self.stats['tiradas_max'], [2])
        self.assertEqual(self.stats['tiradas_min'], [1])

    def test_empate_en_extremos(self):
        """Verifica el comportamiento cuando hay dos tiradas con el mismo valor máximo."""
        datos_empate = [[10, 10], [5, 5], [10, 10]] # Máximo 20 en tiradas 1 y 3
        stats_empate = calcular_estadisticas(datos_empate)
        self.assertEqual(stats_empate['tiradas_max'], [1, 3])

if __name__ == "__main__":
    unittest.main(verbosity=2)