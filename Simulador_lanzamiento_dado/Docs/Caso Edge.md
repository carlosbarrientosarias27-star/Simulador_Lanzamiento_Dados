# 🧪 Pruebas de Casos Edge

## 1. Un solo dado D4 (Mínimo de caras útil)

Este caso verifica que el sistema no falle al tener un rango de resultados muy pequeño (1-4).

- Módulo a probar: logica.py.
- Validación: El resultado debe ser un entero $x$ tal que $1 \le x \le 4$.
- Impacto en visualización: El histograma en visualizacion.py debe mostrar solo 4 columnas.

## 2. Diez dados D20 (Alta denominación)

Verifica que el generador de números aleatorios maneje correctamente dados de 20 caras y que la agregación de resultados sea correcta.

- Módulo a probar: estadisticas.py.
- Validación: La suma total debe estar en el rango $[10, 200]$.
- Análisis: Es un buen momento para verificar que la moda y el promedio se calculen correctamente con una muestra pequeña (10 datos) pero de rango amplio.

## 3. Veinte tiradas seguidas (Persistencia y Volumen)

Este caso pone a prueba la capacidad de escritura en disco y la generación de archivos en la carpeta Historial.

- Módulo a probar: persistencia.py.
- Validación: Verificar que se generen los archivos .txt con el timestamp correcto, similares a los ya existentes (ej. tiradas_20260309_123956.txt).
- Carga: Asegurarse de que el sistema no bloquee el archivo si se intenta escribir ráfagas de datos rápidamente.