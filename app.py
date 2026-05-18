import streamlit as st
import pandas as pd

st.title("Leitura do Banco de Dados")

url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/refs/heads/main/dataset_tratado.csv"

df = pd.read_csv(url)

st.dataframe(df)

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard do Banco de Dados")

# URL do CSV no GitHub
url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/main/dataset_tratado.csv"

# Lendo o CSV
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

st.markdown("---")
st.header("📊 Gráficos Automáticos")

# 1. Histograma de todas as colunas numéricas
st.subheader("Distribuição das variáveis numéricas")
num_cols = df.select_dtypes(include=['int64', 'float64']).columns

for col in num_cols:
    fig, ax = plt.subplots()
    sns.histplot(df[col], kde=True, ax=ax)
    ax.set_title(f"Distribuição de {col}")
    st.pyplot(fig)

# 2. Correlação entre variáveis
st.subheader("Mapa de Correlação")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(df[num_cols].corr(), annot=True, cmap="Blues", ax=ax)
st.pyplot(fig)

# 3. Gráfico de linhas (se tiver datas ou tempo)
if "data" in df.columns:
    st.subheader("Evolução ao longo do tempo")
    fig, ax = plt.subplots()
    df.set_index("data")[num_cols].plot(ax=ax)
    st.pyplot(fig)
