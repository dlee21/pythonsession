import tkinter as tk
import requests
import time

print('Starting MyWeather App')

def getWeather(canvas):
    final_info = 'abc'
    final_data = '123'
    label1.config(text = final_info)
    label2.config(text = final_data)


canvas = tk.Tk()
canvas.geometry("800x600")
canvas.title("My Weather App")

f = ("poppins", 15, "bold")
t = ("new time roman", 35, "italic")

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.focus()
#textField.bind('<Return>', getWeather)


getWeather(canvas)

canvas.mainloop()