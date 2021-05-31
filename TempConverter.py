import tkinter as tk

window = tk.Tk()
window.title("Temperature Converter")
window.geometry("300x200")
window.resizable(width=False, height=False)


def fahrenheit_to_celsius():
    fahrenheit = ent_temperature.get()
    """Convert the value for Fahrenheit to Celsius and insert the
    result into lbl_result.
    """
    celsius = (5/9) * (float(fahrenheit) - 32)
    lbl_result["text"] = f"{round(celsius, 2)} \N{DEGREE CELSIUS}"


def celsius_to_fahrenheit():
    celsius = ent_temperature2.get()
    fahrenheit = (float((celsius)) / (5/9)) + 32
    lbl_result2["text"] = f"{round(fahrenheit, 2)} \N{DEGREE FAHRENHEIT}"


# Create the Fahrenheit entry frame with an Entry
# widget and label in it
frm_entry = tk.Frame(master=window)
ent_temperature = tk.Entry(master=frm_entry, width=10)
lbl_temp = tk.Label(master=frm_entry, text="\N{DEGREE FAHRENHEIT}")

frm_entry2 = tk.Frame(master=window)
ent_temperature2 = tk.Entry(master=frm_entry2, width=10)
lbl_temp2 = tk.Label(master=frm_entry2, text="\N{DEGREE CELSIUS}")


# Layout the temperature Entry and Label in frm_entry
# using the .grid() geometry manager
ent_temperature.grid(row=0, column=0, sticky="e")
lbl_temp.grid(row=0, column=1, sticky="w")

ent_temperature2.grid(row=1, column=0, sticky="e")
lbl_temp2.grid(row=1, column=1, sticky="w")

# Create the conversion Button and result display Label
btn_convert = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=fahrenheit_to_celsius
)
lbl_result = tk.Label(master=window, text="\N{DEGREE CELSIUS}",foreground="blue")

btn_convert2 = tk.Button(
    master=window,
    text="\N{RIGHTWARDS BLACK ARROW}",
    command=celsius_to_fahrenheit
)
lbl_result2 = tk.Label(master=window, text="\N{DEGREE FAHRENHEIT}", foreground="green" )


# Set-up the layout using the .grid() geometry manager
frm_entry.grid(row=0, column=0, padx=10)
btn_convert.grid(row=0, column=1, pady=10)
lbl_result.grid(row=0, column=2, padx=10)

frm_entry2.grid(row=1, column=0, padx=10)
btn_convert2.grid(row=1, column=1, pady=10)
lbl_result2.grid(row=1, column=2, padx=10)

# Run the application
window.mainloop()