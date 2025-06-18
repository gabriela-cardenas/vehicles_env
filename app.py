import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar datos
car_data = pd.read_csv('vehicles_us.csv')

# Título
st.header('Análisis interactivo de anuncios de autos usados')

# Botón 1: Histograma
if st.button('Mostrar histograma del odómetro'):
    st.write('Histograma de la columna "odometer"')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón 2: Gráfico de dispersión
if st.button('Mostrar gráfico de dispersión precio vs. odómetro'):
    st.write('Gráfico de dispersión entre "odometer" y "price"')
    fig = px.scatter(car_data, x='odometer', y='price')
    st.plotly_chart(fig, use_container_width=True)

