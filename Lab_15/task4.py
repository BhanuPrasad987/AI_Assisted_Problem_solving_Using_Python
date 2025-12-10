#write a python function that display weather details of a city using weather api with error handling. Display weather details in user friendly format
import requests
def get_weather_details(city_name):
    api_key = "ed99cb434a09730eeab0e25524bb7754"  # Replace with your actual API key
    base_url = "https://api.openweathermap.org/data/2.5/weather?"   
    complete_url = f"{base_url}q={city_name}&appid={api_key}&units=metric"
    try:    
        response = requests.get(complete_url)
        response.raise_for_status()  # Raise an error for bad responses
        weather_data = response.json()
        if weather_data.get("cod") != 200:
            print("Error: City not found. Please enter a valid city.")
        else:
            city = weather_data.get("name")
            temperature = weather_data["main"].get("temp")
            humidity = weather_data["main"].get("humidity")
            description = weather_data["weather"][0].get("description")
            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description.capitalize()}")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
# Example usage
city = input("Enter city name: ")   
get_weather_details(city)
