# Registro de Asistencia de Inteligencia Artificial

Este documento detalla la interacción con modelos de IA para el desarrollo del proyecto **Simulador de Lanzamiento de Dados**. Se documentan los prompts utilizados para la arquitectura, lógica de negocio y pruebas unitarias.

---

## 1. Arquitectura y Estructura del Proyecto
**Prompt:**
> "Genera una estructura de carpetas para un proyecto de Python que simule el lanzamiento de dados. Necesito separar la lógica del simulador, el manejo de estadísticas, la persistencia de datos (guardado de resultados) y la visualización. Incluye una carpeta de pruebas usando PyTest."

---

## 2. Lógica del Simulador (`src/simulador.py`)
**Prompt:**
> "Crea una clase en Python llamada `Simulador` que permita lanzar un dado de N caras. Debe incluir un método para realizar múltiples lanzamientos y devolver una lista con los resultados. Asegúrate de manejar errores si el número de caras es menor a 2."

---

## 3. Estadísticas y Visualización (`src/estadisticas.py` y `src/visualizacion.py`)
**Prompt:**
> "Escribe una función que reciba una lista de resultados de lanzamientos de dados y calcule la frecuencia de cada cara, el promedio y la desviación estándar. Además, genera un prompt para Matplotlib que cree un histograma simple con estos datos."

---

## 4. Persistencia de Datos (`src/persistencia.py`)
**Prompt:**
> "Crea un módulo para guardar los resultados de las simulaciones en un archivo JSON y en un CSV. El sistema debe permitir cargar un historial previo para no sobrescribir los datos antiguos."

---

## 5. Pruebas Unitarias (`test/src/`)
**Prompt:**
> "Genera pruebas unitarias utilizando `pytest` para los siguientes módulos:
> 1. `Test_simulador.py`: Verificar que los resultados estén en el rango correcto.
> 2. `Test_estadisticas.py`: Validar cálculos con una lista de datos conocida.
> 3. `Test_persistencia.py`: Probar la escritura y lectura de archivos usando mocks para no crear archivos reales."

---

## 6. Documentación y Casos de Borde
**Prompt:**
> "¿Qué casos de borde (edge cases) debería considerar para un simulador de dados? Ayúdame a redactar un archivo `Caso Edge.md` que explique cómo manejar entradas no numéricas o dados con 0 caras."