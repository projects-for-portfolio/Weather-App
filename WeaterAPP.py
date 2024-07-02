import requests
import tkinter as tk
from tkinter import messagebox
import json

def get_weather():
    api_key = "34c12c891c7e4b91aea120919242806"
    city_name = city_entry.get()
    
    if not city_name:
        messagebox.showerror("Error", "Please enter a city name")
        return
    
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city_name}&appid={api_key}"
    
    try:
        response = requests.get(complete_url)
        file_name = "weather_data.json"
        if response.status_code == 200:
            data = response.json()
            with open(file_name, 'w') as json_file:
                json.dump(data, json_file)
            
            main = data['main']
            weather = data['weather'][0]

            weather_info = f"City: {city_name}\n"
            weather_info += f"Temperature: {main['temp']}°K\n"
            weather_info += f"Weather: {weather['description']}"
            messagebox.showinfo("Weather Information", weather_info)
        else:
            messagebox.showerror("Error", "City not found")
    except Exception as e:
        messagebox.showerror("Error", str(e))


# Setting up the GUI
root = tk.Tk()
root.title("Weather App")

root.geometry("300x275")

city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()


get_weather_button = tk.Button(root, text="Enter", command=get_weather)
get_weather_button.pack()

root.mainloop()



