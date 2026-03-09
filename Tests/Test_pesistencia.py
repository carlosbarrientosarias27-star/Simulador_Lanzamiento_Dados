import unittest
from unittest.mock import patch, mock_open
import sys
import os

# 1. Configuración de rutas para encontrar 'src'
directorio_actual = os.path.dirname(os.path.abspath(__file__))
directorio_raiz = os.path.abspath(os.path.join(directorio_actual, '..'))

if directorio_raiz not in sys.path:
    sys.path.insert(0, directorio_raiz)
ruta_src = os.path.join(directorio_raiz, 'src')
if ruta_src not in sys.path:
    sys.path.insert(0, ruta_src)

# 2. Importación del módulo
try:
    from persistencia import guardar_en_historial
except ImportError:
    from SRC.persistencia import guardar_en_historial

class TestPersistencia(unittest.TestCase):

    def setUp(self):
        """Configuración de datos de ejemplo para las pruebas."""
        self.tipo_dado = "D6"
        self.cantidad = 2
        self.tiradas = [[1, 6], [3, 4]]
        self.stats = {
            'total': 14,
            'media': 7.0,
            'maximo': 7,
            'minimo': 7
        }

    @patch('os.makedirs') # Evita que se creen carpetas reales durante el test
    @patch('builtins.open', new_callable=mock_open)
    def test_guardar_en_historial_llamada_open(self, mock_file, mock_makedirs):
        """Verifica que se genere una ruta válida y se abra el archivo para escritura."""
        # Ejecutamos la función. os.path.join funcionará normalmente devolviendo un string.
        ruta_result = guardar_en_historial(
            self.tipo_dado, self.cantidad, self.tiradas, self.stats
        )
        
        # Ahora ruta_result es una cadena de texto real, no un MagicMock
        self.assertIn("historial", ruta_result)
        
        # Verificamos que se llamó a abrir el archivo generado en modo escritura ('w')
        mock_file.assert_called_once_with(ruta_result, "w", encoding="utf-8")

    @patch('os.makedirs')
    @patch('builtins.open', new_callable=mock_open)
    def test_contenido_escrito(self, mock_file, mock_makedirs):
        """Verifica que el contenido del archivo incluya los datos clave formateados."""
        guardar_en_historial(self.tipo_dado, self.cantidad, self.tiradas, self.stats)
        
        # Obtenemos todo lo que se intentó escribir en el archivo simulado
        handle = mock_file()
        contenido_escrito = "".join(call.args[0] for call in handle.write.call_args_list)
        
        # Comprobamos la presencia de datos críticos en el contenido
        self.assertIn("D6", contenido_escrito)
        self.assertIn("Suma total: 14", contenido_escrito)
        self.assertIn("Tirada 1: [1, 6]", contenido_escrito)

if __name__ == "__main__":
    unittest.main(verbosity=2)