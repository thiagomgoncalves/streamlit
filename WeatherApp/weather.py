import requests
import streamlit as st

# API key for OpenWeatherMap
API_KEY = "your_api_key_here"

# URL for OpenWeatherMap API
API_URL = "https://api.openweathermap.org/data/2.5/weather"

# Streamlit app title
st.title("Weather App")

# User input for city name
city = st.text_input("Enter city name:")

# Make API call to OpenWeatherMap
if city:
    params = {"q": city, "appid": API_KEY, "units": "metric"}
    response = requests.get(API_URL, params=params)
    data = response.json()

    # Extract temperature information from JSON response
    temperature = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]

    # Display temperature information to user
    st.write(f"Temperature in {city}: {temperature}°C")
    st.write(f"Feels like: {feels_like}°C") 
    