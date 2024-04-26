import streamlit as st
st.title("Titanic app")
st.header("Demo Titanic App")
st.write("Gráficas de titanic")

import pandas as pd
titanic_link = "titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

