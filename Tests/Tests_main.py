import unittest
import sys
import os

# Subimos un nivel desde /Tests para llegar a la raíz del proyecto
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ruta_raiz)

# Importamos DESDE la carpeta src
from SRC.logica import realizar_serie_tiradas
from SRC.estadisticas import calcular_estadisticas

class TestSimuladorDados(unittest.TestCase):

    def test_rango_dados(self):
        """Verifica que los resultados de D6 estén entre 1 y 6."""
        caras = 6
        n_dados = 2
        n_tiradas = 5
        resultados = realizar_serie_tiradas(caras, n_dados, n_tiradas)
        
        for tirada in resultados:
            for valor in tirada:
                # El stop de range no es inclusivo, usamos + 1
                self.assertTrue(1 <= valor <= caras, f"Valor {valor} fuera de rango")

    def test_calculo_estadisticas(self):
        """Prueba que la suma y la media sean correctas."""
        datos_ejemplo = [[5, 5], [10, 10]] # Total = 30, Media = 15.0
        stats = calcular_estadisticas(datos_ejemplo)
        
        self.assertEqual(stats['total'], 30)
        self.assertEqual(stats['media'], 15.0)

if __name__ == "__main__":
    # El verbo 'verbosity=2' te dará más detalles de qué está pasando
    unittest.main(verbosity=2)