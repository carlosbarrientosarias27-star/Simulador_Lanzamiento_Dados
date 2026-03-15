# 🎲 Proyecto de Simulación de Dados

Repositorio unificado que contiene dos proyectos relacionados con la simulación y prueba de lanzamiento de dados.

---

# 📁 Estructura del Repositorio

```
├── Proyecto de Prueba/
│   ├── __init__.py
│   ├── Readme.md
│   └── simulador.py
│
├── Simulador_lanzamiento_dado/
│   ├── Docs/
│   │   ├── asistencia.md
│   │   └── Caso Edge.md
│   ├── Historial/
│   │   └── .gitkeep
│   ├── src/
│   │   ├── __pycache__/
│   │   ├── __init__.py
│   │   ├── estadisticas.py
│   │   ├── main.py
│   │   ├── persistencia.py
│   │   ├── simulador.py
│   │   └── visualizacion.py
│   ├── tests/
│   │   └── src/
│   │       ├── __pycache__/
│   │       ├── __init__.py
│   │       ├── tests_estadisticas.py
│   │       ├── tests_main.py
│   │       ├── tests_pesistencia.py
│   │       ├── tests_simulador.py
│   │       └── tests_visualizacion.py
│   ├── __init__.py
│   ├── .gitignore
│   ├── LICENSE
│   ├── README.md
│   └── requirements.txt
```

---

# 📦 Proyectos

## 1. Proyecto de Prueba

Proyecto inicial y simplificado para validar la lógica básica del simulador de dados.

**Archivos principales:**

| Archivo | Descripción |
|---|---|
| `simulador.py` | Implementación básica del simulador de lanzamiento de dado |
| `__init__.py` | Inicialización del módulo |
| `Readme.md` | Documentación interna del proyecto de prueba |

---

## 2. Simulador\_lanzamiento\_dado

Proyecto completo y modular para simular lanzamientos de dados, con soporte para estadísticas, persistencia de datos y visualización de resultados.

### 🔧 Módulos (`src/`)

| Módulo | Descripción |
|---|---|
| `main.py` | Punto de entrada principal de la aplicación |
| `simulador.py` | Lógica central de simulación de lanzamientos |
| `estadisticas.py` | Cálculo y análisis estadístico de los resultados |
| `persistencia.py` | Almacenamiento y carga de resultados en disco |
| `visualizacion.py` | Generación de gráficas y visualizaciones de datos |

### 🧪 Tests (`tests/src/`)

| Test | Descripción |
|---|---|
| `tests_simulador.py` | Pruebas unitarias del módulo simulador |
| `tests_estadisticas.py` | Pruebas del módulo de estadísticas |
| `tests_pesistencia.py` | Pruebas del módulo de persistencia |
| `tests_visualizacion.py` | Pruebas del módulo de visualización |
| `tests_main.py` | Pruebas de integración del flujo principal |

### 📄 Documentación (`Docs/`)

- **`asistencia.md`** — Guía de asistencia y soporte del proyecto.
- **`Caso Edge.md`** — Documentación de casos límite identificados y su tratamiento.

---

# 🚀 Instalación

## Requisitos previos

- Python 3.14


## Clonar el repositorio

```
git clone <url-del-repositorio>
cd <nombre-del-repositorio>
```
---

# ▶️ Uso

## Ejecutar el simulador completo

```bash
cd Simulador_lanzamiento_dado
python src/main.py
```

## Ejecutar el proyecto de prueba

```bash
cd Proyecto\ de\ Prueba
python simulador.py
```

---

# 🧪 Ejecución de Tests

Desde la raíz del proyecto:

```
cd Simulador_lanzamiento_dado
python -m pytest tests/
```

O para ejecutar un test específico:

```
python -m pytest tests/src/tests_simulador.py
```

---

# 📊 Funcionalidades Principales

- ✅ Simulación de lanzamientos de uno o varios dados
- ✅ Cálculo de estadísticas: media, moda, distribución de frecuencias
- ✅ Persistencia de resultados en archivo
- ✅ Visualización gráfica de los resultados
- ✅ Cobertura completa con tests unitarios e integración
- ✅ Documentación de casos edge

---

# 📝 Licencia

Este proyecto está bajo los términos descritos en el archivo [LICENSE](Simulador_lanzamiento_dado/LICENSE MIT).

---