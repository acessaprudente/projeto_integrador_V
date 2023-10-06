
import pandas as pd
import numpy as np
import plotly.express as px
from dataset import df







































"""
st.header("Grafico de Area1")
chart_data = pd.DataFrame(df['Umidade'])
st.scatter_chart(chart_data)

st.header("Grafico de Area2")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])

st.line_chart(chart_data)


st.header("Grafico de Area3")
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=["a", "b", "c"])
st.scatter_chart(chart_data)





st.header("Grafico de Area4")
df = px.data.tips()
fig = px.ecdf(df, x="total_bill", color="sex")
fig.show()

print(df[df['Umidade'] >= 90])
"""





############################################################################################################
"""
with st.sidebar:
    logo_teste = Image.open('static/img/clima_logo.png')
    st.image(logo_teste, use_column_width=True)
    st.subheader('Filtros')
#

    fUmidade = st.selectbox(
        "Umidade:",
        options=df['Umidade'].unique()
    )
    fTemperatura = st.selectbox(
        "Temperatura:",
        options=df['Temperatura'].unique()
    )
    fPresssa_Relativa = st.selectbox(
        "Pressao_Relativa:",
        options=df['Pressao_Relativa'].unique()
    )
    fPressao_Absoluta = st.selectbox(
        "Pressao_Absoluta:",
        options=df['Pressao_Absoluta'].unique()
    )
    fQualidade_do_Ar= st.selectbox(
        "Qualidade_do_Ar:",
        options=df['Qualidade_do_Ar'].unique()
    )
dadosUsuario = df.loc[(df['Umidade'] ==fUmidade) &
                      (df['Temperatura'] == fTemperatura) 

]


"""

