#Prompt: write a python function that display weather details of a city using weather api with error handling. 
# Display weather details as JSON output
import requests
import json
def get_weather_details(city_name):
    api_key = "ed99cb434a09730eeab0e25524bb7754"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"       
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    try:
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an error for bad responses
        weather_data = response.json()
        if weather_data.get("cod") != 200:
            print(f"Error fetching data: {weather_data.get('message', 'Unknown error')}")
        else:
            print(json.dumps(weather_data, indent=4))
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
# Example usage
city = input("Enter city name: ")
get_weather_details(city)
    