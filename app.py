import streamlit as st
import pandas as pd

st.title("Leitura do CSV no Streamlit")

# URL do arquivo CSV no GitHub (RAW)
url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/main/Untitled0.csv"

# Lendo o CSV
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

