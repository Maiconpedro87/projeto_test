import streamlit as st
import pandas as pd

st.title("Leitura do Banco de Dados")

url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/refs/heads/main/dataset_tratado.csv"

df = pd.read_csv(url)

st.dataframe(df)

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Dashboard do Banco de Dados")

url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/main/dataset_tratado.csv"
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

st.markdown("---")
st.header("📊 Gráficos Interativos")

# Exemplo: gráfico de dispersão
num_cols = df.select_dtypes(include=['int64', 'float64']).columns
if len(num_cols) >= 2:
    fig = px.scatter(df, x=num_cols[0], y=num_cols[1], title=f"{num_cols[0]} vs {num_cols[1]}")
    st.plotly_chart(fig)

# Exemplo: histograma
fig = px.histogram(df, x=num_cols[0], nbins=20, title=f"Distribuição de {num_cols[0]}")
st.plotly_chart(fig)


# 3. Gráfico de linhas (se tiver datas ou tempo)
if "data" in df.columns:
    st.subheader("Evolução ao longo do tempo")
    fig, ax = plt.subplots()
    df.set_index("data")[num_cols].plot(ax=ax)
    st.pyplot(fig)
