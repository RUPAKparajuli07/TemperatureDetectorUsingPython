import requests
import tkinter as tk
from tkinter import font
import time
import itertools

API_KEY = "bc295a4bc8727b69c6df749ba9cc88be"

def get_temperature(api_key, city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data["main"]["temp"] - 273.15
        return temperature
    else:
        return "Error: Could not retrieve temperature data."

def update_temperature():
    temperature = get_temperature(API_KEY, city_entry.get())
    if isinstance(temperature, str):
        temperature_label.config(text=temperature, fg="black")
    else:
        temperature_label.config(text=f"{temperature:.2f}°C")
        if temperature < 10:
            temperature_label.config(fg="blue")
        elif temperature < 20:
            temperature_label.config(fg="green")
        else:
            temperature_label.config(fg="red")

# Define a list of colors for the background
background_colors = ["dark blue", "light blue", "orange", "green", "red", "purple", "yellow", "pink", "cyan", "magenta", "brown", "gray"]
background_cycle = itertools.cycle(background_colors)

# Create the main window
window = tk.Tk()
window.title("Weather App")

# Set the screen size and disable maximize and minimize buttons
window.geometry("500x600")
window.resizable(0, 0)

# Create a frame for the city entry and label
city_frame = tk.Frame(window)
city_frame.grid(row=0, column=0, padx=10, pady=10)

# Create the city entry and label
city_label = tk.Label(city_frame, text="Enter City:", font=("Bell MT", 20), fg="orange")
city_label.grid(row=0, column=0)
city_entry = tk.Entry(city_frame, width=20, font=("Bell MT", 20), fg="orange")
city_entry.grid(row=0, column=1, padx=5)
city_entry.focus()

# Create a frame for the temperature label
temperature_frame = tk.Frame(window)
temperature_frame.grid(row=1, column=0, padx=10, pady=10)

# Create the temperature label
temperature_font = font.Font(size=24)
temperature_label = tk.Label(temperature_frame, text="", font=temperature_font)
temperature_label.pack()

# Create the button to update the temperature
update_button = tk.Button(window, text="Update Temperature", command=update_temperature, font=("Georgia", 20), bg="sky blue")
update_button.grid(row=2, column=0, padx=10, pady=10)

# Function to change the background color every 3.5 seconds
def change_background_color():
    background_color = next(background_cycle)
    window.configure(background=background_color)
    window.after(3500, change_background_color)

# Call the function to start changing the background color
change_background_color()

# Make the window resizable
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.columnconfigure(0, weight=1)

# Start the main loop
window.mainloop()
