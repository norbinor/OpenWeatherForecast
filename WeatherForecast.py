import requests

class WeatherForecast:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather?"

    def get_weather_data(self, city):
        """Fetches weather data for a specified city."""
        url = f"{self.base_url}appid={self.api_key}&q={city}&units=metric"
        response = requests.get(url)
        return response.json()

    def parse_weather_data(self, data):
        """Parses and returns key weather details from the API response."""
        try:
            weather_details = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'description': data['weather'][0]['description'],
                'humidity': data['main']['humidity']
            }
            return weather_details
        except KeyError:
            return None

    def display_weather(self, city):
        """Fetches, parses, and displays weather information for a specified city."""
        data = self.get_weather_data(city)
        weather_details = self.parse_weather_data(data)
        if weather_details:
            print(f"Weather in {weather_details['city']}:")
            print(f"Temperature: {weather_details['temperature']}°C")
            print(f"Description: {weather_details['description']}")
            print(f"Humidity: {weather_details['humidity']}%")
        else:
            print("Weather data could not be retrieved.")

if __name__ == "__main__":
    API_KEY = "YOUR_API_KEY_HERE"
    city = input("Enter a city name to get its weather forecast: ")
    weather_forecast = WeatherForecast(API_KEY)
    weather_forecast.display_weather(city)
