import streamlit as st
st.title("Titanic app")
st.header("Titanic Graphs")
st.write("Rodrigo Torres | A01703521")

import pandas as pd
titanic_link = "titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.hist(titanic_data.Fare)
st.header("Histograma del Titanic")
st.pyplot(fig)

fig, ax = plt.subplots()
ax.hist(titanic_data.Age)
st.header("Histograma del Titanic- columna Age ")
st.pyplot(fig)

st.markdown("___")

fig2, ax2 = plt.subplots()
y_pos = titanic_data["Pclass"]
x_pos = titanic_data["Fare"]
ax2.barh(y_pos, x_pos)
ax2.set_ylabel("Class")
ax2.set_xlabel("Fare")
ax2.set_title("¿Cuánto pagaron las clases del titanic?")

