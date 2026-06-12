import streamlit as st
import pandas as pd
import plotly.express as px

# ============================================
# 1. Cargar dataset limpio
# ============================================
DATA_CLEAN = "data/cleaned/lettuce_growth_clean.csv"
df = pd.read_csv(DATA_CLEAN, encoding="latin1")
# Renombrar columnas para que sean consistentes
df.rename(columns={
    "temperature_(Â°c)": "temperature_c",
    "Humidity (%)": "humidity_percent",
    "TDS Value (ppm)": "tds_ppm",
    "pH Level": "ph_level",
    "Growth Days": "growth_days",
    "Plant_ID": "plant_id",
    "Date": "date"
}, inplace=True)

print("✅ Columnas normalizadas:", df.columns)
# ============================================
# 2. Título y descripción
# ============================================
st.title("🌱 Dashboard de Crecimiento de Lechugas")
st.markdown("""
Este dashboard interactivo permite explorar las condiciones ambientales
y su relación con el crecimiento de las lechugas.
""")

# ============================================
# 3. Selector de variable para histogramas
# ============================================
variable = st.selectbox(
    "Selecciona variable para analizar:",
    ["temperature_c", "humidity_percent", "ph_level", "tds_ppm", "growth_days"]
)

fig_hist = px.histogram(df, x=variable, nbins=20, title=f"Distribución de {variable}")
st.plotly_chart(fig_hist)

# ============================================
# 4. Boxplots interactivos
# ============================================
fig_box = px.box(df, y=variable, title=f"Boxplot de {variable}")
st.plotly_chart(fig_box)

# ============================================
# 5. Scatterplot dinámico
# ============================================
x_var = st.selectbox("Variable en eje X:", ["temperature_c", "growth_days", "tds_ppm"])
y_var = st.selectbox("Variable en eje Y:", ["ph_level", "humidity_percent", "tds_ppm"])

fig_scatter = px.scatter(df, x=x_var, y=y_var, color="humidity_class",
                         title=f"Relación {x_var} vs {y_var}")
st.plotly_chart(fig_scatter)

# ============================================
# 6. Series temporales
# ============================================
time_var = st.selectbox("Variable temporal:", ["temperature_c", "humidity_percent"])
fig_time = px.line(df, x="date", y=time_var, title=f"{time_var} a lo largo del tiempo")
st.plotly_chart(fig_time)
