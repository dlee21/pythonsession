import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city + "&appid=06c921750b9a82d8f5d1294e1586276f"

    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    tempType="°F"
    temp = int(json_data['main']['temp'] - 273.15)
    temp = getFahrenheitFromCelcius(temp)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    min_temp = getFahrenheitFromCelcius(min_temp)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    max_temp = getFahrenheitFromCelcius(max_temp)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))

    final_info = condition + "\n" + str(temp) + tempType
    final_data = "\n" + "Min Temp: " + str(min_temp) + tempType + "\n" \
                 + "Max Temp: " + str(max_temp) + tempType + "\n" \
                 + "Pressure: " + str(pressure) + "\n" \
                 + "Humidity: " + str(
        humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" \
                            + "Sunrise: " + sunrise + "am" + "\n" \
                            + "Sunset: " + sunset + "pm"
    label1.config(text=final_info)
    label2.config(text=final_data)


#(0°C × 9/5) + 32 = 32°F
#(32°F - 32) x 5/9 = 0°C
def getFahrenheitFromCelcius(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit


canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("My Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font=t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()


#  https://www.youtube.com/watch?v=Sz0_2fp27Q0&t=186s