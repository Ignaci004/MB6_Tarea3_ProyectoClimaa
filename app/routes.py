from app import app
from flask import render_template, request
from app.api import get_weather

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    error = None

    if request.method == "POST":
        city = request.form["city"].strip()

        # Validación: que no sea un número
        if city.isdigit():
            error = "⚠️ Por favor ingrese una ciudad válida, no un número."
        else:
            weather_data = get_weather(city)
            if not weather_data:
                error = f"No se encontró información para la ciudad: {city}"

    return render_template("index.html", weather=weather_data, error=error)
