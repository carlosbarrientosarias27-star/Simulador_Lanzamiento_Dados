# 🎲 Simulador de Lanzamiento de Dado

Un simulador estadístico de lanzamientos de dado desarrollado en Python, con capacidades de análisis estadístico, persistencia de datos, visualización de resultados y una suite completa de pruebas automatizadas.

---

# 📋 Tabla de Contenidos

- [Descripcion del Proyecto](#-descripcion-del-proyecto)
- [Objetivos](#-objetivos)
- [Caracteristicas](#-caracteristicas)
- [Estructura del Proyecto](#️-estructura-del-proyecto)
- [Requisitos](#️-requisitos)
- [Instalacion](#️-instalacion)
- [Uso](#-uso)
- [Ejemplos de Ejecucion](#-ejemplos-de-ejecucion)
- [Pruebas](#-pruebas)
- [Documentacion](#-documentacion)
- [Licencia](#-licencia)
---

# 📖 Descripcion del Proyecto

El **Simulador de Lanzamiento de Dado** es una aplicación Python que permite simular el lanzamiento de dados, registrar los resultados, calcular estadísticas descriptivas y visualizar la distribución de los datos. El sistema incluye persistencia de historial de lanzamientos, facilitando el análisis de sesiones anteriores.

El proyecto sigue principios de diseño modular, con separación clara de responsabilidades entre la lógica de simulación, el cálculo estadístico, la visualización y el almacenamiento de datos.

---

# 🎯 Objetivos

## Objetivos Principales

1. **Simular lanzamientos de dado** de forma aleatoria y reproducible, permitiendo configurar el número de caras y la cantidad de tiradas.

2. **Calcular estadísticas descriptivas** sobre los resultados obtenidos: media, mediana, moda, varianza, desviación estándar y frecuencias relativas.

3. **Visualizar los resultados** mediante gráficos de distribución de frecuencias que faciliten la interpretación de los datos.

4. **Persistir el historial** de lanzamientos para permitir análisis comparativos entre sesiones.

# Objetivos Secundarios

- Garantizar la **calidad del código** mediante pruebas unitarias automatizadas para cada módulo.
- Proporcionar una **interfaz de usuario clara** e intuitiva desde la línea de comandos.
- Documentar el comportamiento esperado del sistema ante **casos borde** (lanzamientos con valor mínimo, máximo, sesiones vacías, etc.).

---

# ✨ Caracteristicas

- 🎲 Simulación de dados con número configurable de caras (por defecto: 6)
- 📊 Análisis estadístico completo de los resultados
- 📈 Visualización gráfica de distribuciones de frecuencia
- 💾 Persistencia del historial de lanzamientos en disco
- 🧪 Suite de pruebas unitarias para todos los módulos
- 🖥️ Interfaz de línea de comandos intuitiva

---

# 🗂️ Estructura del Proyecto

```
Historial/                             # Directorio externo donde se guardan las tiradas
Simulador_lanzamiento_dado/
├── Docs/
│   ├── asistencia.md          # Documentación de asistencia y soporte
│   └── Caso Edge.md           # Casos borde documentados
├── Historial/
│   └── .gitkeep               # Marca el directorio en el repositorio (vacío)
├── src/
│   ├── __init__.py
│   ├── main.py                # Punto de entrada principal de la aplicación
│   ├── simulador.py           # Lógica de simulación de lanzamientos
│   ├── estadisticas.py        # Cálculo de estadísticas descriptivas
│   ├── visualizacion.py       # Generación de gráficos y visualizaciones
│   └── persistencia.py        # Carga y guardado del historial
├── test/
│   └── src/
│       ├── __init__.py
│       ├── Test_simulador.py       # Pruebas del módulo simulador
│       ├── Test_estadisticas.py    # Pruebas del módulo estadísticas
│       ├── Test_pesistencia.py     # Pruebas del módulo persistencia
│       └── Test_visualizacion.py  # Pruebas del módulo visualización
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

---

# 🛠️ Requisitos

- Python 3.14

---

# ⚙️ Instalacion

1. **Clonar el repositorio:**
   ```
   git clone https://github.com/tu-usuario/Simulador_lanzamiento_dado.git
   cd Simulador_lanzamiento_dado
   ```

2. **Crear y activar un entorno virtual (recomendado):**
   ```
   python -m venv venv

   # En Windows:
   venv\Scripts\activate

   # En macOS/Linux:
   source venv/bin/activate
   ```
---

# 🚀 Uso

Ejecuta la aplicación principal desde la raíz del proyecto:

```
python src/main.py
```

## Opciones disponibles

La aplicación acepta argumentos opcionales desde la línea de comandos:

```
# Simulación básica con configuración por defecto (1 dado de 6 caras, 10 lanzamientos)
python src/main.py

# Especificar número de lanzamientos
python src/main.py --lanzamientos 100

# Especificar número de caras del dado
python src/main.py --caras 12

# Combinación de parámetros
python src/main.py --lanzamientos 50 --caras 20

# Ver el historial de sesiones anteriores
python src/main.py --historial

# Mostrar ayuda
python src/main.py --help
```

---

# 📌 Ejemplos de Ejecucion

## Ejemplo 1 — Simulación básica (10 lanzamientos, dado de 6 caras)

```
$ python src/main.py --lanzamientos 10
```

**Salida esperada:**
```
=== Simulador de Lanzamiento de Dado ===
Dado de 6 caras | 10 lanzamientos

Resultados: [3, 6, 1, 4, 2, 6, 5, 3, 4, 2]

--- Estadísticas ---
Media:              3.60
Mediana:            3.50
Moda:               3, 6, 4, 2  (aparecen 2 veces)
Varianza:           2.64
Desviación Estándar: 1.62

Historial guardado en: Historial/sesion_20240315_143022.json
```

---

## Ejemplo 2 — Simulación extensa (1000 lanzamientos)

```
$ python src/main.py --lanzamientos 1000
```

**Salida esperada:**
```
=== Simulador de Lanzamiento de Dado ===
Dado de 6 caras | 1000 lanzamientos

--- Estadísticas ---
Media:              3.52
Mediana:            4.00
Moda:               3  (aparece 178 veces)
Varianza:           2.91
Desviación Estándar: 1.71

Frecuencias relativas:
  1: ████████████████  16.3%
  2: █████████████████ 17.1%
  3: ██████████████████ 17.8%
  4: █████████████████ 16.9%
  5: ████████████████  16.2%
  6: █████████████████ 15.7%

[Se abre gráfico de barras de distribución]
Historial guardado en: Historial/sesion_20240315_143055.json
```

---

## Ejemplo 3 — Dado de 20 caras

```
$ python src/main.py --lanzamientos 50 --caras 20
```

**Salida esperada:**
```
=== Simulador de Lanzamiento de Dado ===
Dado de 20 caras | 50 lanzamientos

Resultados: [14, 7, 19, 2, 11, ...]

--- Estadísticas ---
Media:              10.44
Mediana:            10.50
Moda:               7  (aparece 5 veces)
Varianza:           33.17
Desviación Estándar: 5.76

Historial guardado en: Historial/sesion_20240315_143120.json
```

---

## Ejemplo 4 — Consultar historial de sesiones

```bash
$ python src/main.py --historial
```

**Salida esperada:**
```
=== Historial de Sesiones ===
[1] sesion_20240315_143022.json  |  10 lanzamientos  |  Dado 6 caras  |  Media: 3.60
[2] sesion_20240315_143055.json  | 1000 lanzamientos  |  Dado 6 caras  |  Media: 3.52
[3] sesion_20240315_143120.json  |  50 lanzamientos  |  Dado 20 caras  |  Media: 10.44
```

---

# 🧪 Pruebas

Para ejecutar la suite completa de pruebas unitarias:

```
# Desde la raíz del proyecto
python -m pytest test/ -v
```

Para ejecutar las pruebas de un módulo específico:

```
python -m pytest test/src/Test_simulador.py -v
python -m pytest test/src/Test_estadisticas.py -v
python -m pytest test/src/Test_pesistencia.py -v
python -m pytest test/src/Test_visualizacion.py -v
```

**Salida esperada:**
```
============================= test session starts ==============================
test/src/Test_simulador.py::test_lanzamiento_en_rango PASSED
test/src/Test_simulador.py::test_numero_lanzamientos PASSED
test/src/Test_estadisticas.py::test_media PASSED
test/src/Test_estadisticas.py::test_mediana PASSED
test/src/Test_estadisticas.py::test_desviacion_estandar PASSED
test/src/Test_pesistencia.py::test_guardar_historial PASSED
test/src/Test_pesistencia.py::test_cargar_historial PASSED
test/src/Test_visualizacion.py::test_genera_grafico PASSED
============================== 8 passed in 0.42s ===============================
```

---

# 📚 Documentacion

La documentación adicional del proyecto se encuentra en el directorio `Docs/`:

- **`Docs/asistencia.md`** — Guía de soporte y resolución de problemas comunes.
- **`Docs/Caso Edge.md`** — Descripción y comportamiento esperado ante casos borde (0 lanzamientos, dado de 1 cara, valores extremos, archivos de historial corruptos, etc.).

---

# 📄 Licencia

Este proyecto está licenciado bajo los términos descritos en el archivo [LICENSE](LICENSE MIT).

---