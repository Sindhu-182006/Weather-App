import streamlit as st
import requests

st.title("🌦️ Weather Forecast App (WeatherAPI)")
st.write("Enter a city name to get current weather data.")

# Input
city = st.text_input("Enter city name").strip()

# WeatherAPI key (replace this with your real key)
API_KEY = "86f1c2ee5134443abed94611253006"

# Function to get weather
def get_weather(city):
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=no"
    response = requests.get(url)
    try:
        data = response.json()
        return data
    except Exception as e:
        return {"error": {"message": str(e)}}

# Display weather
if city:
    data = get_weather(city)

    # Debug output
    st.write("🔍 API Raw Response:")
    st.json(data)

    if "current" in data:
        st.success(f"✅ Weather in {data['location']['name']}, {data['location']['country']}")

        temp = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        icon = data["current"]["condition"]["icon"]
        humidity = data["current"]["humidity"]
        wind = data["current"]["wind_kph"]

        st.image("https:" + icon)
        st.write(f"**Temperature:** {temp} °C")
        st.write(f"**Condition:** {condition}")
        st.write(f"**Humidity:** {humidity}%")
        st.write(f"**Wind Speed:** {wind} km/h")

    else:
        st.error(f"❌ Error: {data.get('error', {}).get('message', 'Unknown error')}")
