import streamlit as st
import pandas as pd

st.title("Leitura do Banco de Dados")

url = "https://raw.githubusercontent.com/Maiconpedro87/projeto_test/refs/heads/main/dataset_tratado.csv"

df = pd.read_csv(url)

st.dataframe(df)
