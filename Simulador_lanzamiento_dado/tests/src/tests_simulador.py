import unittest
import sys
import os

# Ajuste de ruta para detectar la carpeta 'src' desde 'Test/src'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
sys.path.insert(0, ruta_raiz)

from src.simulador import obtener_caras_dado, lanzar_dados, realizar_sesion

class TestSimulador(unittest.TestCase):

    def test_obtener_caras_dado_valido(self):
        """Verifica que el mapeo de dados sea correcto."""
        self.assertEqual(obtener_caras_dado("D6"), 6)
        self.assertEqual(obtener_caras_dado("d20"), 20)
        self.assertEqual(obtener_caras_dado("D12"), 12)

    def test_obtener_caras_dado_invalido(self):
        """Verifica que devuelva None si el dado no existe."""
        self.assertIsNone(obtener_caras_dado("D100"))

    def test_lanzar_dados_rango_y_cantidad(self):
        """Valida que los resultados estén en rango y la lista tenga el tamaño correcto."""
        caras = 6
        cantidad = 10
        resultados = lanzar_dados(caras, cantidad)
        
        self.assertEqual(len(resultados), cantidad)
        for valor in resultados:
            self.assertTrue(1 <= valor <= caras)

    def test_realizar_sesion_estructura(self):
        """Verifica que se cree una lista de listas con el historial."""
        caras, cantidad, repeticiones = 6, 2, 5
        sesion = realizar_sesion(caras, cantidad, repeticiones)
        
        # Debe haber tantas listas como repeticiones
        self.assertEqual(len(sesion), repeticiones)
        # Cada sub-lista debe tener el tamaño de 'cantidad'
        self.assertEqual(len(sesion[0]), cantidad)

if __name__ == '__main__':
    unittest.main()