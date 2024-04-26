import streamlit as st
st.title("Titanic app")
st.header("Titanic Graphs")
st.write("Rodrigo Torres | A01703521")

import pandas as pd
titanic_link = "titanic.csv"
titanic_data = pd.read_csv(titanic_link)
st.dataframe(titanic_data)

#import matplotlib.pyplot as plt

#fig, ax = plt.subplots()
#ax.hist(titanic_data.Fare)
#st.header("Histograma del Titanic")
#st.pyplot(fig)
