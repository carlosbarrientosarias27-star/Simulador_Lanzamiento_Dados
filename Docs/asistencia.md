# Registro de Asistencia de IA - Simulador de Lanzamiento 

Este documento detalla la interacción con la IA para el desarrollo del proyecto SIMULADOR_LANZAMIENTO_DADOS, cubriendo desde la estructura lógica hasta la visualización y persistencia.

# 🤖 Resumen de Interacción

Modelo: Gemini 

Fecha de Inicio: 9 de marzo de 2026

Objetivo: Crear un simulador modular de lanzamientos de dados con análisis estadístico y persistencia de datos.

# 🛠️ Prompts Utilizados 

## 1. Definición de Arquitectura 

Prompt: "Genera la estructura de carpetas para un proyecto de Python de simulación de dados. Necesito separar la lógica, la visualización, la persistencia de datos y las estadísticas en módulos diferentes dentro de una carpeta SRC. También incluye una carpeta Tests para pruebas unitarias."

## 2. Lógica del Simulador (logica.py) 

Prompt: "Escribe una clase en Python llamada Simulador que permita lanzar dados de N caras. Debe incluir métodos para lanzamientos individuales y múltiples, devolviendo una lista de resultados."

## 3. Estadísticas y Visualización (estadisticas.py y visualizacion.py) 

Prompt: "Crea una función que reciba una lista de resultados de dados y calcule la frecuencia, el promedio y la moda."

## 4. Persistencia de Datos (persistencia.py) 

Prompt: "Necesito una función para guardar los resultados de cada sesión en un archivo .txt dentro de una carpeta llamada Historial. El nombre del archivo debe incluir un timestamp con el formato tiradas_YYYYMMDD_HHMMSS.txt."

## 5. Pruebas Unitarias (Tests/) 

Prompt: "Genera pruebas unitarias usando unittest para los módulos de lógica y estadística. Asegúrate de probar casos de borde como dados de 1 sola cara o listas de resultados vacías."

# 📋 Convenciones de Código Sugeridas

Durante la asistencia, se establecieron las siguientes reglas:

Uso de Docstrings en todas las funciones.

Manejo de excepciones en la lectura/escritura de archivos.

Seguimiento del estándar PEP 257.