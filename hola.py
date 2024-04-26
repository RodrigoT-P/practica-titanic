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

st.header("Grafica de Barras del Titanic")
st.pyplot(fig2)

st.markdown("___")

fig3, ax3 = plt.subplots()
ax3.scatter(titanic_data.Age, titanic_data.Fare)
ax3.set_xlabel("Edad")
ax3.set_ylabel("Tarifa")
st.header("Gráfica de Dispersión del Titanic")
st.pyplot(fig3)

st.markdown("___")

fig4, ax4 = plt.subplots()
ax4 = titanic_data.boxplot(["Age"])
ax4.set_ylabel("Edad")
st.header("Gráfica de cajas por Edad")
st.pyplot(fig4)

st.markdown("___")

import numpy as np
fig5, ax5 = plt.subplots()
hist_class = np.histogram(titanic_data["Pclass"], bins=3, range=(1,3))[0]

labels = ["Clase 1", "Clase 2", "Clase 3"]
colors = ["tab:blue", "tab:red", "tab:green"]
explode = [0, 0, 0.2]

ax5.pie(hist_class, 
        labels = labels, 
        colors = colors, 
        explode = explode, 
        shadow = True)

st.header("Gráfica de pastel - Clase social")
st.pyplot(fig5)
st.dataframe(hist_class)