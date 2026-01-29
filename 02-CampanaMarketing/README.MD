# Marketing Campaign Analysis & Predictive Modeling

## 📌 Descripción del proyecto
Este proyecto analiza el desempeño de campañas de marketing digital a lo largo del funnel completo  
(**Impressions - Clicks - Leads - Applications - Enrollments**) y desarrolla modelos de *Machine Learning* con un enfoque práctico, orientado a la toma de decisiones reales como si se tratara de un cliente.

El objetivo principal es **entender qué variables influyen en el rendimiento de las campañas** y **construir modelos predictivos utilizando únicamente variables controlables**, evitando métricas derivadas que no pueden ser manipuladas directamente (como CTR o ROI).

---

## 🎯 Objetivos
- Analizar el comportamiento del funnel de marketing.
- Identificar cuellos de botella mediante tasas de conversión.
- Explorar segmentaciones mediante *clustering*.
- Evaluar la viabilidad de modelos predictivos para:
  - ROI
  - Enrollments
  - Impressions
- Construir un modelo final predictivo de **Impressions** usando variables controlables.
- Simular un escenario real de uso del modelo (input - predicción).

---

## 🗂️ Estructura del análisis

### 1️⃣ Exploratory Data Analysis (EDA)
- Análisis de distribuciones (histogramas).
- Revisión de escalas y asimetrías.
- Evaluación de estabilidad de métricas como *Impressions*.

---

### 2️⃣ Funnel de Marketing
- Construcción del funnel promedio.
- Cálculo de tasas:
  - CTR
  - Lead Rate
  - Application Rate
  - Enrollment Rate
- Identificación de cuellos de botella.
- Comparación por plataforma, audiencia, campaña y tiempo.

---

### 3️⃣ Clustering (K-Means)
- Uso del método del codo y silueta.
- Inclusión de variables numéricas y transformaciones temporales.
- Evaluación crítica de resultados (silueta baja).
- Uso exploratorio para detectar patrones, no segmentación definitiva.

---

### 4️⃣ Feature Engineering
- Conversión de rangos de edad a valores numéricos.
- Transformación cíclica del tiempo:
  - `month_sin`
  - `month_cos`
- Selección de variables relevantes para modelos supervisados.

---

### 5️⃣ Machine Learning Supervisado
- Impressions 

Modelos utilizados:
- Regresión Lineal
- Random Forest
- Random Forest con GridSearch

📌 **Modelo final**:
- Target: `Impressions`
- Features:
  - `Cost (₹)`
  - `month_sin`
  - `month_cos`
  - `age_numeric`

**Resultados:**
- R² ≈ 0.72  
- MAE ≈ 30.000  
- Error relativo ≈ 18% respecto a la media

---

##  Uso del modelo (caso cliente)
Se implementó una función de predicción que permite estimar impresiones futuras a partir de:
- Presupuesto
- Mes de la campaña
- Rango etario objetivo

Esto simula cómo un cliente podría **estimar resultados antes de lanzar una campaña**.

---

## 🧠 Conclusiones clave
- Las impresiones son una variable estable, controlable y altamente explicada por el costo.
- La transformación cíclica del tiempo mejora la representación temporal.
- El enfoque por bloques (Impressions - Funnel - ROI) es más realista que un modelo único.
- El *Machine Learning* debe responder a decisiones reales, no solo a métricas altas.

---

## 🛠️ Tecnologías utilizadas
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Scikit-learn  
- Jupyter Notebook  

---

## 📁 Notebook
El análisis completo puede encontrarse en:

➡️ `./Notebook/marketingCampaignData.ipynb.ipynb`