import requests
import streamlit as st
import streamlit.components.v1 as components

path_to_html = "./index.html" 

# Read file and keep in variable
with open(path_to_html,'r') as f: 
    html_data = f.read()

## Show in webpage
st.header("Analise por Parametro")
st.components.v1.html(html_data,height=1000, width=1000 ,scrolling=True) # type: ignore
