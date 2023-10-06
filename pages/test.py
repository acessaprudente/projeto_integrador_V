import streamlit as st
import requests
from datetime import datetime
import pytz
import pycountry_convert as pc


chave ='ff56f71acf9ecb958146e73645e9821e'
cidade = 'Presidente Prudente'
#api_link = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={}'.format(chave)
api_link = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}' .format(cidade,chave)

r = requests.get(api_link)
#dados = r #.json()
dados = r .json()
#print(dados)

pais_codigo = dados['sys']['country']
zona_fuso = pytz.country_timezones[pais_codigo]
pais = pytz.country_names[pais_codigo]
zona = pytz.timezone(zona_fuso[7])
zona_horas = datetime.now(zona)
zona_horas = zona_horas.strftime("%d %m %Y|%M:%M:%S %p")


#print(zona_horas)

tempo = dados['main']['temp']
pressao = dados['main']['pressure']
umidade = dados['main']['humidity']
velocidade = dados['wind']['speed']
descricao = dados['weather'][0]['description']

#print(tempo)


def country_to_continent(country_name):
    country_alpha2 = pc.country_name_to_country_alpha2(country_name)
    country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
    country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
    return country_continent_name

# Example
country_name = 'Brazil'
#print(country_to_continent(country_name))


















