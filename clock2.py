from tkinter import *
from tkinter.ttk import *
from time import strftime

tk = Tk()
tk.title("Smart-Clock")

label = Label(tk, font=("ds-digital", 80), background="black", foreground="cyan")
label.pack(anchor='center')

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

def startClock():
    time()
    tk.mainloop()

startClock()

print('hello')