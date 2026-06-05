# FIFA World Cup 2026 Prediction

Proyecto de análisis de datos que busca predecir el ganador del Mundial 2026 usando datos históricos, machine learning y simulaciones.

## Objetivo

Construir un sistema que permita:

- Estimar la fuerza real de selecciones nacionales mediante Elo Ratings dinámicos
- Predecir el resultado de un partido ingresando dos equipos
- Simular enfrentamientos del FIFA World Cup 2026
- Comparar desempeño de modelos de Machine Learning vs baseline Elo

## Demo de la App

La aplicación permite predecir el resultado de un partido entre dos selecciones:

- Entrada:
  - Equipo local
  - Equipo visitante

- Salida:
  - Probabilidad de victoria del equipo local
  - Probabilidad de empate
  - Probabilidad de victoria del equipo visitante

## 🚀 Demo en vivo

[![Abrir app](https://img.shields.io/badge/Abrir%20App-Streamlit-red)](https://world-cup-2026-predictor-iwqgg7em6hngzhtlsd2zjc.streamlit.app/)
    
## Dataset

- Más de 47,000 partidos internacionales (1872–2024)
- Incluye:
  - Resultados históricos
  - Torneos oficiales y amistosos
  - Local/visitante
  - Partidos en cancha neutral

## Metodología

- **Elo Rating System**
  - Cálculo dinámico de fuerza de cada selección
  - Ajustado por:
    - Importancia del partido
    - Diferencia de goles
    - Tipo de torneo

- **Feature Engineering**
  - Diferencia de Elo entre equipos
  - Forma reciente
  - Tipo de partido

- **Modelos utilizados**
  - Logistic Regression (baseline)
  - Comparación con sistema Elo clásico

- **Evaluación**
  - Accuracy
  - Log Loss
  - Comparación contra baseline

## Aplicación Web (Streamlit)

La app permite ingresar dos equipos y obtener una predicción en tiempo real usando un modelo entrenado previamente.

## Tecnologías

- Python
- Pandas
- NumPy
- Scikit-learn
- RapidFuzz
- Joblib
- Streamlit
- Jupyter Notebook

## Dataset
Fuente: Kaggle – Global Football Results: (1872–2024) - Match Results