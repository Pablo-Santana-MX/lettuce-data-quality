<div align="center">
  <h1>🌱 Agritech Decision Intelligence: Hydroponic Lettuce Yield Optimization</h1>
  <p><i>An End-to-End Machine Learning Pipeline: From Data Governance to Prescriptive Analytics</i></p>
  
  <img src="https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/Data_Engineering-Pandas%20%7C%20NumPy-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="Data Engineering" />
  <img src="https://img.shields.io/badge/Machine_Learning-XGBoost%20%7C%20scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="Scikit-Learn" />
  <img src="https://img.shields.io/badge/Deployment-Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white" alt="Streamlit" />
</div>

## 📌 1. Executive Summary
Traditional agriculture relies heavily on human intuition and heuristic rules. This project transforms raw hydroponic and soil-based growth data into an automated **Decision Intelligence System**. By enforcing strict data quality protocols and leveraging advanced machine learning, this system predicts final crop yields and generates actionable, prescriptive recommendations to optimize biochemical and environmental parameters.

**Business Impact:** Transitions farming operations from reactive monitoring to proactive, data-driven yield maximization.

## 🏗️ 2. Architecture & Methodology

### Phase 1: Data Governance & Feature Engineering (ETL)
*   **Objective:** Guarantee data integrity and extract meaningful signals from raw sensor logs and manual entries.
*   **Process:** Automated anomaly detection (e.g., filtering impossible pH levels or extreme humidity spikes), missing value imputation, and feature engineering to capture temporal growth dynamics before feeding data into the modeling pipeline.

### Phase 2: Predictive Analytics (Machine Learning)
*   **Objective:** Forecast final lettuce yield (grams/head) utilizing early-stage environmental variables (Temperature, Humidity, pH, Electrical Conductivity, Water Volume).
*   **Modeling:** Implementation and hyperparameter tuning of ensemble regression algorithms (Random Forest / XGBoost) to effectively capture complex, non-linear biological and chemical relationships.

### Phase 3: Prescriptive Recommendation Engine
*   **Objective:** Move beyond mere forecasting to prescribe actionable operational interventions.
*   **Mechanism:** An optimization layer that evaluates the current crop state and outputs specific, quantifiable adjustments (e.g., *"Decrease pH by 0.5 and increase nutrient flow by 10% to achieve an estimated +15% yield increase"*).

## 📊 3. Interactive Application & Deployment
The end-to-end pipeline is deployed as an interactive **Streamlit** web application. This interface empowers non-technical agricultural stakeholders and agronomists to input current greenhouse metrics and instantly receive real-time yield predictions alongside prescriptive operational recommendations.

## 🚀 4. Repository Structure
```text
├── data/                  # Raw, intermediate, and processed datasets
├── notebooks/             
│   ├── 01_ETL_Data_Governance.ipynb      # Cleaning, EDA, and Anomaly Detection
│   ├── 02_Yield_Prediction_Model.ipynb   # Model training, evaluation, and tuning
│   └── 03_Prescriptive_Engine.ipynb      # Optimization and recommendation logic
├── src/                   # Modularized Python scripts (utils, models, pipeline)
├── app/                   # Streamlit dashboard source code and UI components
├── requirements.txt       # Environment dependencies
└── README.md

```
## 📬 5. About the Author
**Pablo Alberto Santana Flores**  
*Data Scientist | PhDc in Marine Sciences | Chemical Engineer*  
Passionate about bridging the gap between complex biological systems and scalable decision intelligence.

* 💼 **LinkedIn:** [linkedin.com/in/pablo-santana-mx](https://www.linkedin.com/in/pablo-santana-mx)
* 🐙 **GitHub:** [github.com/Pablo-Santana-MX](https://github.com/Pablo-Santana-MX)
