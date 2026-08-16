from config import API_KEY
from datetime import datetime
import requests
import tkinter as tk

root=tk.Tk()
root.title("Weather App")
root.geometry("450x500")
root.configure(bg="#CFEFFF")
def get_weather():
    city = city_entry.get()
    if city=="":
           weather_label.config(text="Please enter a city.")
           return

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response=requests.get(url)
    data=response.json()
    if data["cod"]!=200:
           weather_label.config(text="City not found")
           return
    
    temperature=data["main"]["temp"]
    humidity=data["main"]["humidity"]
    wind=data["wind"]["speed"]
    feels_like=data["main"]["feels_like"]
    description=data["weather"][0]["description"]
    print(description)
    if "clear" in description:
        emoji = "☀️"
        bg_color="#FFF4B2"
    elif "cloud" in description:
            emoji = "☁️"
            bg_color="#DDEAF6"
    elif "rain" in description:
            emoji = "🌧️"
            bg_color="#B8D8F8"
    elif "thunderstorm" in description:
            emoji = "⛈️"
            bg_color="#233B5F"
    elif "snow" in description:
            emoji = "❄️"
            bg_color="#F5F9FF"
    elif "mist" in description or "fog" in description:
            emoji = "🌫️"
            bg_color="#CFEFFF"
    else:
            emoji = "🌍"
            bg_color="#CFEFFF"
    root.configure(bg=bg_color)
    title.config(bg=bg_color)
    weather_label.config(bg=bg_color)
    weather_label.config(
        text=(
        f"📍 City: {city}\n\n"
        f"🌡 Temperature: {temperature}°C\n"
        f"🥵 Feels like: {feels_like}°C\n"
        f"{emoji}Weather: {description.title()}\n"
        f"💧 Humidity: {humidity}%\n"
        f"💨 Wind: {wind} m/s"
    )
)
    city_entry.delete(0,tk.END)

title = tk.Label(
    root,
    text="🌤 Weather App",
    font=("Bodoni MT", 24, "bold"),
    bg="#CFEFFF",
    fg="#246BCE"
)
title.pack(pady=20)
city_entry=tk.Entry(
    root,
    font=("Times New Roman",18),
    width=20
)
city_entry.pack(pady=10)
city_entry.bind("<Return>",lambda event: get_weather())
search_button=tk.Button(
    root,
    text=("Search"),
    font=("Times New Roman",16),
    bg="#81C9FA",
    fg="white",
    command=get_weather
)
search_button.pack(pady=10)
weather_label=tk.Label(
    root,
    text="",
    font=("Times New Roman",16),
    bg="#CFEFFF",
    fg="#246BCE",
    justify="left"
)
weather_label.pack(pady=20)
root.mainloop()