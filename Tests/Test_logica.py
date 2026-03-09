import unittest
import sys
import os

# 1. Localizamos la carpeta raíz del proyecto
# __file__ es la ubicación de Tests_main.py. 
# '..' nos sube a la carpeta Simulador_Lanzamiento_Dados
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_raiz = os.path.abspath(os.path.join(directorio_actual, '..'))

# 2. Añadimos tanto la raíz como la carpeta 'src' al path
sys.path.insert(0, directorio_raiz)
sys.path.insert(0, os.path.join(directorio_raiz, 'src'))

# 3. Importaciones (Ahora Python sabe dónde buscar)
try:
    from logica import realizar_serie_tiradas, lanzar_dados
    print("✅ Módulos cargados correctamente desde 'src'")
except ImportError as e:
    print(f"❌ Error crítico: No se pudo encontrar logica.py. Error: {e}")
    sys.exit(1)

class TestLogicaDados(unittest.TestCase):

    def test_lanzar_dados_rango(self):
        """Verifica que un dado (ej. D6) devuelva valores entre 1 y 6."""
        caras = 6
        cantidad = 10
        resultado = lanzar_dados(caras, cantidad)
        
        self.assertEqual(len(resultado), cantidad)
        for valor in resultado:
            self.assertTrue(1 <= valor <= caras, f"El valor {valor} está fuera del rango 1-{caras}")

    def test_serie_tiradas_estructura(self):
        """Verifica que realizar_serie_tiradas devuelva la cantidad correcta de tiradas."""
        caras = 10
        cantidad_dados = 3
        repeticiones = 5
        resultados = realizar_serie_tiradas(caras, cantidad_dados, repeticiones)
        
        # Debe haber 5 listas de tiradas
        self.assertEqual(len(resultados), repeticiones)
        # Cada tirada debe tener 3 dados
        self.assertEqual(len(resultados[0]), cantidad_dados)

if __name__ == "__main__":
    unittest.main()