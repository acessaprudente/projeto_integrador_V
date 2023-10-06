import streamlit as st
import pandas as pd
from dataset import df
from PIL import Image
from datetime import date, datetime
from utils import convert_csv, mensagem_sucesso



colunasUteis = ['created_at','Umidade','Temperatura','Pressao_Absoluta','Pressao_Relativa','Qualidade_do_Ar']
df = df[colunasUteis]

st.dataframe(df)   


#sidebar
with st.sidebar:
    logo_teste = Image.open('static/img/clima_logo.png')
    st.image(logo_teste, use_column_width=True)
#
checkbox_mostrar_tabela = st.sidebar.checkbox('Mostrar tabela')
if checkbox_mostrar_tabela:
    st.sidebar.markdown('## Filtro para a tabela')
    colunas = list(df.columns)
    colunas.append('Todas')
    coluna = st.sidebar.selectbox('Selecione a coluna  para apresentar na tabela', options = colunas)
    

st.markdown(f' Dataset possui :blue[{df.shape[0]}] linhas e :blue[{df.shape[1]}] colunas')

st.markdown('Escreva um nome do arquivo')



coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input(
        '',
        label_visibility='collapsed'
    )
    nome_arquivo += '.csv'
with coluna2:
    st.download_button(
        'Baixar arquivo',
        data=convert_csv(df),
        file_name=nome_arquivo,
        mime='text/csv',
        on_click=mensagem_sucesso
    )


 




















