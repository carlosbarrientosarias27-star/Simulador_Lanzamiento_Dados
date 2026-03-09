import sys
import os
import unittest

# 1. Configuración robusta del Path
# Esto permite ejecutar el test desde CUALQUIER carpeta
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_PATH = os.path.join(BASE_DIR, '..', 'src')
sys.path.append(SRC_PATH)

# 2. Importaciones
try:
    from logica import realizar_serie_tiradas
    from estadisticas import calcular_estadisticas
    from persistencia import guardar_en_historial
except ImportError as e:
    print(f"Error: No se pudieron importar los módulos desde {SRC_PATH}")
    print(f"Detalle: {e}")
    sys.exit(1)

class TestSimuladorDados(unittest.TestCase):

    ## --- Pruebas de Lógica ---
    def test_realizar_serie_tiradas_cantidad(self):
        """Verifica que se devuelva el número correcto de tiradas y dados."""
        n_dados = 3
        n_reps = 5
        caras = 6 
        resultado = realizar_serie_tiradas(caras, n_dados, n_reps)
        
        self.assertEqual(len(resultado), n_reps, "La cantidad de repeticiones es incorrecta.")
        self.assertEqual(len(resultado[0]), n_dados, "La cantidad de dados por tirada es incorrecta.")

    def test_rango_valores_dados(self):
        """Verifica que ningún dado sea menor a 1 o mayor a sus caras."""
        caras = 4
        # Aumentamos a 100 para tener más cobertura estadística
        resultado = realizar_serie_tiradas(caras, 1, 100) 
        for tirada in resultado:
            for dado in tirada:
                self.assertGreaterEqual(dado, 1, f"Dado {dado} menor a 1")
                self.assertLessEqual(dado, caras, f"Dado {dado} mayor a {caras}")

    ## --- Pruebas de Estadísticas ---
    def test_calcular_estadisticas_basicas(self):
        """Verifica que los cálculos coincidan con la lógica de negocio."""
        # Simulamos dos tiradas: [2, 4] (suma 6) y [1, 3] (suma 4)
        datos_prueba = [[2, 4], [1, 3]] 
        stats = calcular_estadisticas(datos_prueba)
        
        # Total: 6 + 4 = 10
        self.assertEqual(stats['total'], 10)
        # Media: 10 / 2 = 5.0
        self.assertAlmostEqual(float(stats['media']), 5.0)
        # Máximo de las sumas: max(6, 4) = 6
        self.assertEqual(stats['maximo'], 6)
        # Mínimo de las sumas: min(6, 4) = 4
        self.assertEqual(stats['minimo'], 4)
        
        # Verificamos que los índices de las tiradas sean correctos
        # (Si tu lógica usa índices 1-based)
        self.assertIn(1, stats['tiradas_max'])
        self.assertIn(2, stats['tiradas_min'])

    ## --- Pruebas de Persistencia ---
    def test_archivo_creado(self):
        """Verifica si la lógica de guardado genera un archivo físico y lo limpia."""
        stats_ficticias = {
            "total": 6, "media": 6.0, "maximo": 6, "minimo": 6,
            "tiradas_max": [1], "tiradas_min": [1]
        }
        
        ruta = None
        try:
            # Intentamos guardar
            ruta = guardar_en_historial("D6", 1, [[6]], stats_ficticias)
            
            # Verificamos si la ruta es válida y el archivo existe
            self.assertIsNotNone(ruta, "La función no devolvió una ruta válida.")
            self.assertTrue(os.path.exists(ruta), f"El archivo {ruta} no fue creado.")
            
        finally:
            # Limpieza: Pase lo que pase, intentamos borrar el archivo de test
            if ruta and os.path.exists(ruta):
                os.remove(ruta)

if __name__ == "__main__":
    unittest.main()