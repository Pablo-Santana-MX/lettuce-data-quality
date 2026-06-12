<h3 style="text-align: center; color: gray;">
Author: Pablo Alberto Santana Flores • June 2026
</h3>

## 📌 Description (English)

This project documents the **data cleaning and preparation process** for lettuce growth analysis.  
The goal is to showcase best practices in *data quality* and *data preparation* for a professional portfolio.

### 🔹 Main Steps
- Column renaming and standardization
- Missing value handling
- Duplicate removal
- Date normalization
- Data type conversion
- Derived variables (`humidity_class`, `temperature_class`)
- Numeric scaling for analysis and models

### 🔹 Files
- `data/raw/lettuce_growth_raw.csv` → Raw data
- `notebooks/lettuce_growth_analysis.ipynb` → Cleaning pipeline notebook
- `README.md` → Project documentation

---

## 🚀 Cómo correr el proyecto / How to run the project

```bash
# Clonar el repositorio
git clone https://github.com/Pablo-Santana-MX/lettuce-data-quality.git

# Entrar al directorio
cd lettuce-data-quality

# Abrir el notebook en JupyterLab
jupyter lab notebooks/lettuce_growth_analysis.ipynb