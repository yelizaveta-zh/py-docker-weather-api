import os
import requests


API_KEY = os.getenv("API_KEY")
CITY = os.getenv("CITY", "Paris")
BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather() -> None:
    params = {
        "key": API_KEY,
        "q": CITY,
        "aqi": "no"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        temp_c = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]
        print(f"Weather in {CITY}: {temp_c}°C, {condition}")
    else:
        print(f"Failed to get weather data: "
              f"{response.status_code}, "
              f"{response.text}")


if __name__ == "__main__":
    get_weather()
