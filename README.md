# Weather App Documentation

## Overview

The Weather App is a simple graphical user interface (GUI) application built with the Tkinter library in Python. It allows users to input a city name, and it retrieves and displays the current temperature of that city using the OpenWeatherMap API. The application also includes a feature that changes the background color of the window every 3.5 seconds for a visually appealing experience.

## Requirements

To run the Weather App, you need the following:

1. Python: Make sure you have Python installed on your system (Python 3.x is recommended).

2. Internet Connection: The Weather App requires an active internet connection to fetch the weather data from the OpenWeatherMap API.

## Installation

1. Clone the repository or download the Python script containing the Weather App code.

2. Ensure you have the necessary libraries installed. If you don't have them already, you can install them using pip:

```
pip install requests
```

## How to Use

1. Run the Python script containing the Weather App code.

2. The main window of the Weather App will appear, titled "Weather App."

3. Enter the name of the city for which you want to know the weather in the "Enter City" input field.

4. Click the "Update Temperature" button to fetch and display the current temperature of the entered city.

5. The temperature will be shown in Celsius. The text color of the temperature label will change based on the temperature range:
   - Blue: Temperature below 10°C
   - Green: Temperature between 10°C and 19.99°C
   - Red: Temperature 20°C and above

6. The background color of the window will change every 3.5 seconds, cycling through a predefined list of colors, creating a visually dynamic effect.

7. You can close the application by clicking the window's close button (X).

## Code Explanation

1. The `get_temperature` function takes an API key and a city name as input and makes a request to the OpenWeatherMap API to get the temperature of the specified city. It then processes the API response and returns the temperature in Celsius.

2. The `update_temperature` function is responsible for updating the temperature label in the GUI. It uses the `get_temperature` function to fetch the temperature and then updates the label text accordingly. It also changes the text color of the label based on the temperature range.

3. The application starts by creating a Tkinter window and setting its title to "Weather App." The window size is set to 500x600 pixels, and resizing is disabled.

4. The GUI is organized into two frames:
   - `city_frame`: Contains a label and an entry widget to input the city name.
   - `temperature_frame`: Contains a label to display the temperature.

5. A button labeled "Update Temperature" is created, which, when clicked, triggers the `update_temperature` function to fetch and display the temperature.

6. The background color of the window is set to change every 3.5 seconds using the `change_background_color` function and a list of predefined colors.

7. The `mainloop` method is called to start the main event loop of the Tkinter application, enabling user interaction.

## Limitations and Improvements

- The application currently displays the temperature in Celsius only. It could be enhanced to provide options to display the temperature in Fahrenheit or other temperature units.
- Error handling for invalid city names or API request failures can be improved to provide more informative messages to the user.
- The background color cycle could be made more visually appealing by customizing the color list or using gradient transitions.
- The application does not handle internationalization and localization. It could be adapted to support different languages and regions.
- The current implementation updates the temperature on button click only. It could be further enhanced to automatically update the temperature at regular intervals for a real-time weather experience.

## Conclusion

The Weather App provides a simple and visually engaging way to check the current temperature of a city. It utilizes the OpenWeatherMap API to fetch weather data and the Tkinter library to create the graphical user interface. With further improvements and enhancements, it has the potential to become a more comprehensive and user-friendly weather application.
