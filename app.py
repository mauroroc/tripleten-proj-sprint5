import pandas as pd
import plotly.express as px
import streamlit as st
     
car_data = pd.read_csv('vehicles_us.csv') 

st.header("Dashboard Anúncios de Vendas de Veículos nos EUA") 

hist_chkbox = st.checkbox('Ver histograma') 
if hist_chkbox: 
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

disp_chkbox = st.checkbox('Ver gráfico de dispersão')
if disp_chkbox:
    st.write('Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carros')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)