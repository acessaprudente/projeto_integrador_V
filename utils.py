import pandas as pd
import streamlit as st
import time
from dataset import df

def format_number(value, prefix = ''):
    for unit in ['', '']:
        if value < 1000:
            return f'{prefix} {value:.2f} {unit}'
        value /= 1000
    return f'{prefix} {value:.2f} milhões'


df_t=(df[['Umidade','created_at']])

df_u=(df[['Pressao_Relativa','created_at']])

df_a=(df[['Pressao_Absoluta','created_at']])

df_l =(df[['Qualidade_do_Ar','created_at']])

df_x=(df[['Temperatura','created_at']])


@st.cache_data
def convert_csv(df):
    return df.to_csv(index=False).encode('utf-8')

def mensagem_sucesso():
    success = st.success(
        'Arquivo baixado com sucesso',
        icon="✅"
        )
    time.sleep(3)
    success.empty()