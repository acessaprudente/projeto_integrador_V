import json
import pandas as pd
import streamlit as st
import plotly.express as px
from dataset import df
from utils import format_number 
from graficos import grafico_analise_IoT, grafico_analise_IoT_Pressoes, grafico_umidade_x_temperatura, grafico_analise_IoT_Pressoes2, grafico_qualidade_do_ar 

st.set_page_config(page_title="Dashboard  de Clima Presidente Prudente -SP 	🌦️",layout='wide')
st.markdown("<h1 style='text-align:center;'> Dashboard  de Clima Presidente Prudente -SP 🌦️ </h1>",unsafe_allow_html= True)
st.markdown('---')

aba1,aba2,aba3,aba4,aba5,aba6 = st.tabs(['Dataset','Umidade','Temperatuta','Pressão_Relativa','Pressão_Absoluta','Qualidade_do_Ar'])
                
with aba1:
    st.dataframe(df)

    
with aba2:
    st.metric( 'Media Umidade (%)', format_number(df['Umidade'].median()))
    st.metric( 'Desvio Padrao ', format_number(df['Umidade'].std()))
    st.plotly_chart(grafico_analise_IoT, use_container_width=True)
        


        
with aba3:
    st.metric( 'Temperatura Media (°C )', format_number(df['Temperatura'].median()))
    st.metric( 'Desvio Padrao ', format_number(df['Temperatura'].std()))
    st.plotly_chart(grafico_umidade_x_temperatura, use_container_width=True)
        

    

with aba4:
    st.metric( 'Pressao_Relativa', format_number(df['Pressao_Relativa'].median()))
    st.metric( 'Desvio Padrao ', format_number(df['Pressao_Relativa'].std()))
    st.plotly_chart(grafico_analise_IoT_Pressoes, use_container_width=True)

with aba5:
    st.metric( 'Pressao_Absoluta', format_number(df['Pressao_Absoluta'].median()))
    st.metric( 'Desvio Padrao ', format_number(df['Pressao_Absoluta'].std()))
    st.plotly_chart(grafico_analise_IoT_Pressoes2, use_container_width=True)
  
with aba6:
    st.metric( 'Qualidade_do_Ar', format_number(df['Qualidade_do_Ar'].median()))
    st.metric( 'Desvio Padrao ', format_number(df['Qualidade_do_Ar'].std()))
    st.plotly_chart(grafico_qualidade_do_ar , use_container_width=True)






