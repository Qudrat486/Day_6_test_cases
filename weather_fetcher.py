import requests

def fetch_weather_data(base_url, city, api_key):
    try:
        response = requests.get(f"{base_url}q={city}&appid={api_key}&units=metric")
        response.raise_for_status()
        weather_data = response.json()
        return {
            'temperature': weather_data['main']['temp'],
            'humidity': weather_data['main']['humidity'],
            'weather_description': weather_data['weather'][0]['description']
        }
    except requests.exceptions.HTTPError as http_err:
        return {"error": f"HTTP Error: {http_err}"}
    except Exception as err:
        return {"error": f"Error: {err}"}


    except requests.RequestException as e:
        # Handle network issues
        print(f"Network error occurred: {e}")
        return None
    except (KeyError, IndexError) as e:
        # Handle issues with the API response structure
        print(f"Error processing API response: {e}")
        return None

def display_weather(data):
    if data:
        print(f"Temperature: {data['temperature']}°C")
        print(f"Humidity: {data['humidity']}%")
        print(f"Weather Description: {data['weather_description']}")
    else:
        print("No weather data available")

# Example usage
if __name__ == "__main__":
    # Enter your API key here
    api_key = "1517ed8b6e93dae5197a90c3e4754de1"

    # Base URL to store the weather API endpoint
    base_url = "http://api.openweathermap.org/data/2.5/weather?"

    # Give city name
    city_name = input("Enter city name: ")
    
    # Fetch and display weather data
    weather_data = fetch_weather_data(base_url, city_name, api_key)
    display_weather(weather_data)
