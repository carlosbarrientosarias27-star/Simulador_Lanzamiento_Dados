# 🎲 Simulador de Lanzamiento de Dados

Un simulador de lanzamiento de dados en Pyhton que tengan un soporte para análisis estadístico, visualización de resultados, persistencia de historial y pruebas automatizadas.

---

# 📋 Descripción del Proyecto

Este proyecto implementa un "Similador de lanzamiento de dados" que permite realizar tiradas individuales y múltiples, registrar los resultados, analizarlos estadísticamente y visualizarlos gráficamente y guarda un historial de todas las partidas realizas.

## Objetivos

- **Simular** lanzamientos de uno o varios dados con distintas configuraciones (número de caras, cantidad de dados).
- **Analizar** estadísticamente los resultados: media, mediana, moda, desviación estándar y distribución de frecuencias.
- **Visualizar** los resultados mediante gráficas y representaciones gráficas en consola o ventana.
- **Persistir** el historial de tiradas en archivos de texto para consultas futuras.
- **Garantizar** la calidad del código mediante una suite completa de pruebas unitarias.

---

# 🗂️ Estructura del Proyecto

```
SIMULADOR_LANZAMIENTO_DADOS/
├── Docs/
│   ├── asistencia.md           # Documentación de asistencia / ayuda
│   └── Caso Edge.md            # Casos límite y comportamientos especiales
├── Historial/
│   ├── tiradas_YYYYMMDD_HHMMSS.txt  # Archivos de historial de tiradas
│   └── .gitkeep
├── SRC/
│   ├── estadisticas.py         # Cálculos estadísticos sobre los resultados
│   ├── logica.py               # Lógica principal del simulador de dados
│   ├── main.py                 # Punto de entrada de la aplicación
│   ├── persistencia.py         # Lectura/escritura del historial en disco
│   └── visualizacion.py        # Generación de gráficas y representaciones visuales
├── Tests/
│   ├── Test_estadisticas.py    # Tests para el módulo de estadísticas
│   ├── Test_logica.py          # Tests para la lógica del simulador
│   ├── Test_pesistencia.py     # Tests para la persistencia de datos
│   ├── Tests_main.py           # Tests de integración del módulo principal
│   └── Tests_visualizacion.py  # Tests para el módulo de visualización
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# ⚙️ Requisitos

- Python 3.14
- Las dependencias listadas en `requirements.txt`


# 🚀 Instrucciones de Uso

## 1. Clonar el repositorio

```
git clone <url-del-repositorio>
cd SIMULADOR_LANZAMIENTO_DADOS
```

---

# 🎮 Ejemplos de Ejecución

## Ejemplo 1 – Lanzamiento básico

```
python SRC/main.py
```

```
=== Simulador de Lanzamiento de Dados ===
Número de dados: 2
Número de caras por dado: 6
Número de tiradas: 10

Resultados:
  Tirada  1: [3, 5] → Suma: 8
  Tirada  2: [1, 6] → Suma: 7
  Tirada  3: [4, 4] → Suma: 8
  ...

Estadísticas:
  Media:              7.40
  Mediana:            7.50
  Moda:               8
  Desviación típica:  1.85

Historial guardado en: Historial/tiradas_20260309_120847.txt
```

## Ejemplo 2 – Módulo de estadísticas por separado

```python
from SRC.estadisticas import calcular_estadisticas

resultados = [7, 8, 5, 9, 6, 7, 8, 7, 10, 4]
stats = calcular_estadisticas(resultados)
print(stats)
# {'media': 7.1, 'mediana': 7.0, 'moda': 7, 'desviacion': 1.73}
```

## Ejemplo 3 – Leer historial guardado

```python
from SRC.persistencia import cargar_historial

tiradas = cargar_historial("Historial/tiradas_20260309_120847.txt")
print(tiradas)
```

## Ejemplo 4 – Visualización de distribución

```python
from SRC.visualizacion import mostrar_distribucion

resultados = [2, 3, 5, 7, 7, 8, 9, 6, 7, 8, 5, 4]
mostrar_distribucion(resultados)
```

---

## 🧪 Ejecución de Tests

## Ejecutar un módulo de tests específico

```
# Tests de estadísticas
python -m pytest Tests/Test_estadisticas.py -v

# Tests de lógica
python -m pytest Tests/Test_logica.py -v

# Tests de persistencia
python -m pytest Tests/Test_pesistencia.py -v

# Tests de integración
python -m pytest Tests/Tests_main.py -v

# Tests de visualización
python -m pytest Tests/Tests_visualizacion.py -v
```

### Ver cobertura de tests

```
pip install pytest-cov
python -m pytest Tests/ --cov=SRC --cov-report=term-missing
```

---

# 📁 Archivos de Historial

Cada ejecución genera automáticamente un archivo de texto en la carpeta `Historial/` con el formato:

```
tiradas_YYYYMMDD_HHMMSS.txt
```

Ejemplo de contenido:

```
Fecha: 2026-03-09 12:08:47
Dados: 2 × D6
Tiradas: 10
---
Tirada 1: [3, 5] = 8
Tirada 2: [1, 6] = 7
...
---
Media: 7.40 | Moda: 8 | Desv.típica: 1.85
```

---

# 📄 Licencia

Este proyecto está licenciado bajo los términos del archivo [LICENSE](LICENSE).

---

# 📚 Documentación Adicional

- [`Docs/asistencia.md`](Docs/asistencia.md) — Guía de ayuda y referencia rápida.
- [`Docs/Caso Edge.md`](Docs/Caso%20Edge.md) — Casos límite documentados y cómo se manejan.