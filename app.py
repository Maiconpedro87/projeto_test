import streamlit as st
import pandas as pd

st.title("Leitura do CSV no Streamlit")

# URL do arquivo CSV no GitHub (RAW)
url = "https://github.com/amdbraz/PI_G36/blob/main/dataset_tratado.csv"

# Lendo o CSV
df = pd.read_csv(url)

st.subheader("Prévia dos dados")
st.dataframe(df)

