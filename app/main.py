import os

import requests
from dotenv import load_dotenv


def get_weather() -> None:
    load_dotenv()
    api_key = os.getenv("API_KEY")
    print(api_key)

    payload = {"key": api_key, "q": "Paris"}

    response = requests.get(
        "http://api.weatherapi.com/v1/current.json",
        params=payload,
    )

    result = response.json()

    location = result.get("location")
    current = result.get("current")
    condition = current.get("condition")

    city = location.get("name")
    country = location.get("country")
    current_time = location.get("localtime")
    temperature = current.get("temp_c")
    weather = condition.get("text")

    print(f"{city}/{country} {current_time} "
          f"Weather: {temperature} Celsius, {weather}")


if __name__ == "__main__":
    get_weather()
