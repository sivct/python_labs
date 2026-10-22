import requests
from typing import Optional






class Geocoder:
    BASE_URL = "https://geocoding-api.open-meteo.com/v1/search"


    def __init__(self, session: requests.Session) -> None:
        self._session: requests.Session = session

    def find(self, city: str) -> Optional[dict]:
        params: dict = {
            "name": city,
            "count": 1,
            "format": "json",
        }

        response: requests.Response = self._session.get(self.BASE_URL, params=params)
        data: dict = response.json()

        if "results" not in data:
            return None


        place: dict = data["results"][0]
        return{
            "name": str(place["name"]),
            "country": str(place.get("country", "")),
            "latitude": float(place["latitude"]),
            "longitude": float(place["longitude"]),
        }







class WeatherClient:
    BASE_URL = "https://api.open-meteo.com/v1/forecast"

    def __init__(self, session: requests.Session) -> None:
        self._session: requests.Session = session



    def get_current(self, latitude: float, longitude: float) -> dict:
        params: dict = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,wind_speed_10m",
            "timezone": "auto"
        }
        response: requests.Response = self._session.get(self.BASE_URL, params=params)
        data: dict = response.json()
        current = data["current"]

        return {
            "temperature": float(current["temperature_2m"]),
            "humidity": int(current["relative_humidity_2m"]),
            "wind": float(current["wind_speed_10m"]),
        }


class WeatherApp:
    def __init__(self) -> None:
        self._session: requests.Session = requests.Session()
        self.geocoder: Geocoder = Geocoder(self._session)
        self.weather: WeatherClient = WeatherClient(self._session)

    def start(self) -> None:
        city: str = input("Enter the city: ")

        place: Optional[dict] = self.geocoder.find(city)
        if place is None:
            print("this city is not found.")
            return

        current: dict = self.weather.get_current(latitude=place["latitude"], longitude=place["longitude"])

        print(f"the weather in {place['name']}, {place['country']}:")
        print(f"temperature: {current['temperature']}°C")
        print(f"humidity: {current['humidity']}%")
        print(f"wind: {current['wind']} km/h")







if __name__ == "__main__":
    app: WeatherApp = WeatherApp()
    app.start()