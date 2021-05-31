import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'[0]['main']]
    temp = int(json_data['main]['temp] )


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("My Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")


textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)   #getWeather is a function


label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

canvas.mainloop()