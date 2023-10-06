from folium import Icon
import streamlit as st
import requests
API_KEY = "ff56f71acf9ecb958146e73645e9821e"

def find_current_weather(city):
    base_url  = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid={}' .format(cidade,chave)
    weather_data = requests.get(base_url).json()
    try:
        general = weather_data['weather'][0]['main']
        icon_id = weather_data['weather'][0]['icon']
        temperature = round(weather_data['main']['temp'])
        icon = f"http://openweathermap.org/img/wn/{icon_id}@2x.png"
    except KeyError:
        st.error("City Not Found")
        st.stop()
    return general,temperature,Icon





def main():
    st.header("Find the Weather")
    city = st.text_input("Enter the City").lower()
    if st.button("Find"):
        general,temperature,icon = find_current_weather(city)
        col_1,col_2 = st.columns(2)
        with col_1:
            st.metric(label = "Temperature",value=f"{temperature}°C")
        with col_2:
            st.write(general)
            st.image(icon)
    



    
if __name__ == '__main__':
    main()