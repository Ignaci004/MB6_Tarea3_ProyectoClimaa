from dotenv import load_dotenv
import requests
import os

# Cargar variables del archivo .env
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    try:
        params = {
            "q": city,
            "appid": API_KEY,
            "units": "metric",  # temperatura en °C
            "lang": "es"        # respuestas en español
        }
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if response.status_code != 200 or data.get("cod") != 200:
            return None  # ciudad no encontrada o error

        # Validación: que el nombre sea exacto
        # Normalizo quitando espacios y mayúsculas/minúsculas
        if data["name"].strip().lower() != city.strip().lower():
            return None

        weather = {
            "city": data["name"],
            "temp": round(data["main"]["temp"], 1),
            "state": data["weather"][0]["description"].capitalize(),
            "humidity": data["main"]["humidity"],
            "icon": f"http://openweathermap.org/img/wn/{data['weather'][0]['icon']}@2x.png"
        }
        return weather

    except Exception as e:
        print(f"Error al obtener clima: {e}")
        return None