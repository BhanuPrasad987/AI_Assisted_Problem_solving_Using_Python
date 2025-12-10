#write a python function that display weather details of a city using weather api with error handling.
#  Display weather details as JSON output. Store the weather details in current directory as text file, 
# every run output will append
'''
Expected Output:
o	A local file results.json is created/updated with stored responses like:
o	[
o	  {"city": "London", "temp": 18, "humidity": 60, "weather": "Clear sky"},
o	  {"city": "New York", "temp": 22, "humidity": 55, "weather": "Few clouds"}
'''
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
            city = weather_data.get("name")
            temperature = weather_data["main"].get("temp")
            humidity = weather_data["main"].get("humidity")
            description = weather_data["weather"][0].get("description")
            print(f"City: {city}")
            print(f"Temperature: {temperature}°C")
            print(f"Humidity: {humidity}%")
            print(f"Weather: {description.capitalize()}")

            # Prepare data to be saved
            weather_record = {
                "city": city,
                "temp": temperature,
                "humidity": humidity,
                "weather": description.capitalize()
            }

            # Append data to results.txt
            with open("results.txt", "a") as file:
                file.write(json.dumps(weather_record) + "\n")
    except requests.RequestException as e:
        print(f"An error occurred: {e}")
# Example usage
city = input("Enter city name: ")
get_weather_details(city)
