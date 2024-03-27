import tkinter as tk
import requests

def get_weather(city):
    api_key = "a3df8b98916e10ca5c2d2c70ed94bdca"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    
    response = requests.get(complete_url)
    
    if response.status_code == 200:
        data = response.json()
        if data.get("main"):
            main_data = data["main"]
            weather_data = data["weather"][0]
            temperature = main_data["temp"]
            humidity = main_data["humidity"]
            description = weather_data["description"]
            display_weather(city, temperature, humidity, description)
        else:
            display_error("City data not found.")
    else:
        display_error(f"Error fetching data. Status code: {response.status_code}")

def display_weather(city, temperature, humidity, description):
    result_label.config(text=f"Weather in {city}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nDescription: {description}")

def display_error(message):
    result_label.config(text=message, fg="red")

def fetch_weather(event=None):
    city = city_entry.get()
    if city:
        get_weather(city)
    else:
        display_error("Please enter a city name.")

root = tk.Tk()
root.title("Weather App")

city_label = tk.Label(root, text="Enter city name:", font=("Helvetica", 12))
city_label.grid(row=0, column=0, padx=10, pady=10)

city_entry = tk.Entry(root, font=("Helvetica", 12))
city_entry.grid(row=0, column=1, padx=10, pady=10)
city_entry.bind("<Return>", fetch_weather)

fetch_button = tk.Button(root, text="Fetch Weather", font=("Helvetica", 12), command=fetch_weather)
fetch_button.grid(row=0, column=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()
