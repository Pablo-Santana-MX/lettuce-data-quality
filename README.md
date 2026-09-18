<div align="center">
  <h1>🌱 Agritech Decision Intelligence: Lettuce Yield Optimization</h1>
  <p><i>From Data Governance to Predictive Modeling and Prescriptive Recommendations</i></p>
  
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Machine_Learning-scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Streamlit-Live_App-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
</div>

## 🔬 1. Project Overview
Traditional agriculture relies heavily on human intuition. This project transforms raw hydroponic/soil lettuce growth data into an automated **Decision Intelligence System**. It not only enforces strict data quality protocols but also predicts final crop yield and provides actionable biochemical/environmental recommendations to farmers.

## 🧪 2. Architecture & Methodology

### Phase 1: Data Governance & ETL
*   **Objective:** Sanitize raw sensor and manual entry data.
*   **Process:** Automated anomaly detection (e.g., impossible pH levels, extreme humidity outliers) ensuring robust data integrity before entering the modeling phase.

### Phase 2: Predictive Analytics (Machine Learning)
*   **Objective:** Forecast final lettuce yield (grams/head) based on early-stage environmental variables (Temperature, Humidity, pH, Water Volume).
*   **Model:** Implementation of a regression algorithm (Random Forest / XGBoost) to capture non-linear biological and chemical relationships.

### Phase 3: Prescriptive Recommendation Engine
*   **Objective:** Move beyond prediction to prescribe actionable operational changes.
*   **Mechanism:** An optimization algorithm that analyzes the current crop state and prescribes specific adjustments (e.g., *"Reduce pH by 0.5 and increase irrigation by 10% to achieve a +15% yield increase"*).

## 📊 3. Interactive Dashboard
The entire pipeline is designed to be deployed via an interactive **Streamlit** dashboard. This allows non-technical agricultural stakeholders to input current greenhouse metrics and instantly receive yield predictions and operational recommendations.

## 🚀 4. Repository Structure
```text
├── data/                  # Raw and sanitized datasets
├── notebooks/             
│   ├── 01_ETL_and_Data_Quality.ipynb
│   ├── 02_Yield_Prediction_Model.ipynb
│   └── 03_Recommendation_Engine.ipynb
├── app/                   # Streamlit dashboard source code
└── README.md
```
## 📬 5. Contact
**Pablo Alberto Santana Flores**
*Data Scientist | PhD in Marine Sciences | Decision Intelligence | Chemical Engineer*

* 💼 **LinkedIn:** [linkedin.com/in/pablo-santana-mx](https://www.linkedin.com/in/pablo-santana-mx)
* 🐙 **GitHub:** [github.com/Pablo-Santana-MX](https://github.com/Pablo-Santana-MX)
