import plotly.express as px
from utils import df_t , df_u , df_a, df_l, df_x





grafico_analise_IoT = px.scatter(
    df_t,
    x='created_at',
    y='Umidade',
    color="Umidade",
    width=400,
    height=800,
    title = 'Fonte: Sensor NODEMCU-ESP8266'
)


grafico_analise_IoT_Pressoes = px.scatter(
    df_u.head(200),
    x='created_at', 
    y='Pressao_Relativa',
    color='Pressao_Relativa',
    width=400,
    height=800,
    title = 'Fonte: Sensor NODEMCU-ESP8266'
)


grafico_umidade_x_temperatura = px.bar(
    df_x,
    x = 'created_at',
    y = 'Temperatura', barmode='group',
    color='Temperatura',
    width=400,
    height=400,
    title = 'Fonte: Sensor NODEMCU-ESP8266'

)



grafico_analise_IoT_Pressoes2 = px.scatter(
    df_a.head(200),
    x='created_at', 
    y='Pressao_Absoluta',
    width=400,
    height=800,
    title = 'Fonte: Sensor NODEMCU-ESP8266'
)



grafico_qualidade_do_ar = px.bar(
    df_l.head(200),
    x='created_at',
    y='Qualidade_do_Ar',
    width=400,
    height=800,
    title = 'Fonte: Sensor NODEMCU-ESP8266'
)



