import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard Completo do Banco de Dados")

# Lendo o CSV
url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/main/dataset_tratado.csv"
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

# -----------------------------
# 1. HISTOGRAMAS
# -----------------------------
st.header("📌 Histogramas")

num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    fig = px.histogram(df, x=col, nbins=20, title=f"Distribuição de {col}")
    st.plotly_chart(fig)

# -----------------------------
# 2. DISPERSÕES
# -----------------------------
st.header("📌 Gráficos de Dispersão")

if "daily_calories_consumed" in df.columns and "weight_change_(lbs)" in df.columns:
    fig = px.scatter(df, x="daily_calories_consumed", y="weight_change_(lbs)",
                     color="gender", title="Calorias Consumidas vs Mudança de Peso")
    st.plotly_chart(fig)

if "daily_caloric_surplus/deficit" in df.columns and "weight_change_(lbs)" in df.columns:
    fig = px.scatter(df, x="daily_caloric_surplus/deficit", y="weight_change_(lbs)",
                     color="physical_activity_level",
                     title="Superávit/Déficit Calórico vs Mudança de Peso")
    st.plotly_chart(fig)

# -----------------------------
# 3. BOXPLOTS
# -----------------------------
st.header("📌 Boxplots")

if "physical_activity_level" in df.columns:
    fig = px.box(df, x="physical_activity_level", y="weight_change_(lbs)",
                 title="Mudança de Peso por Nível de Atividade Física")
    st.plotly_chart(fig)

if "sleep_quality" in df.columns:
    fig = px.box(df, x="sleep_quality", y="weight_change_(lbs)",
                 title="Mudança de Peso por Qualidade do Sono")
    st.plotly_chart(fig)

# -----------------------------
# 4. CORRELAÇÃO
# -----------------------------
st.header("📌 Mapa de Correlação")

corr = df[num_cols].corr()
fig = px.imshow(corr, text_auto=True, color_continuous_scale="Blues",
                title="Correlação entre Variáveis Numéricas")
st.plotly_chart(fig)

# -----------------------------
# 5. BARRAS
# -----------------------------
st.header("📌 Gráficos de Barras")

if "gender" in df.columns:
    fig = px.bar(df.groupby("gender")["weight_change_(lbs)"].mean().reset_index(),
                 x="gender", y="weight_change_(lbs)",
                 title="Mudança de Peso por Gênero")
    st.plotly_chart(fig)

if "stress_level" in df.columns:
    fig = px.bar(df.groupby("stress_level")["weight_change_(lbs)"].mean().reset_index(),
                 x="stress_level", y="weight_change_(lbs)",
                 title="Mudança de Peso por Nível de Estresse")
    st.plotly_chart(fig)

# -----------------------------
# 6. LINHA
# -----------------------------
st.header("📌 Gráfico de Linha")

if "duration_(weeks)" in df.columns:
    fig = px.line(df.sort_values("duration_(weeks)"),
                  x="duration_(weeks)", y="weight_change_(lbs)",
                  title="Mudança de Peso ao Longo das Semanas")
    st.plotly_chart(fig)

