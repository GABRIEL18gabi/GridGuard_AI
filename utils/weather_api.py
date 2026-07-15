import requests

API_KEY = "fc7d2f5616118256718001e61013f9a3"


def get_weather_by_coordinates(lat, lon):

    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    try:

        response = requests.get(url)

        if response.status_code != 200:
            return None

        data = response.json()

        return {
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "wind": data["wind"]["speed"],
            "weather": data["weather"][0]["main"],
            "description": data["weather"][0]["description"]
        }

    except:
        return None