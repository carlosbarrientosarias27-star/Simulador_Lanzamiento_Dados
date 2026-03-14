import unittest
import os
import sys
import shutil
import time

# Ajuste de ruta para detectar la carpeta 'src'
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ruta_raiz not in sys.path:
    sys.path.insert(0, ruta_raiz)

from src.persistencia import guardar_historial

class TestPersistencia(unittest.TestCase):

    def setUp(self):
        """Configuración inicial antes de cada test."""
        self.test_dir = "Historial"
        self.datos = [[1, 6], [3, 4]]
        self.stats = {"promedio": 3.5}
        self.config = {
            'cantidad': 2,
            'tipo': 'D6',
            'repeticiones': 2
        }

    def tearDown(self):
        """Limpieza robusta después de cada test."""
        # Damos un momento para que el SO cierre descriptores de archivos
        time.sleep(0.1) 
        
        if os.path.exists(self.test_dir):
            # Función auxiliar para forzar el borrado de archivos de solo lectura
            def remove_readonly(func, path, excinfo):
                os.chmod(path, 0o777)
                func(path)

            try:
                shutil.rmtree(self.test_dir, onerror=remove_readonly)
            except Exception as e:
                print(f"\n[Aviso] No se pudo borrar {self.test_dir}: {e}")

    def test_creacion_directorio_y_archivo(self):
        """Verifica que se cree la carpeta y el archivo de texto."""
        nombre_archivo = guardar_historial(self.datos, self.stats, self.config)
        ruta_completa = os.path.join(self.test_dir, nombre_archivo)
        
        self.assertTrue(os.path.exists(ruta_completa))

    def test_contenido_archivo(self):
        """Verifica que el contenido escrito sea el correcto."""
        nombre_archivo = guardar_historial(self.datos, self.stats, self.config)
        ruta_completa = os.path.join(self.test_dir, nombre_archivo)
        
        # El bloque 'with' asegura que el archivo se cierre tras leerlo
        with open(ruta_completa, "r", encoding="utf-8") as f:
            contenido = f.read()
            self.assertIn("SIMULACIÓN DE DADOS", contenido)
            self.assertIn("Configuración: 2 D6 x 2 veces", contenido)
            self.assertIn("Tirada 1: [1, 6] (Suma: 7)", contenido)

if __name__ == '__main__':
    unittest.main()