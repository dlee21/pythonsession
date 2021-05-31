import tkinter as tk

window = tk.Tk()

greeting = tk.Label(text="Python rocks!", width=50, foreground="white", background="blue",height=10)
greeting.pack()

entry = tk.Entry()
entry.pack()

def myClick():
    text = entry.get()
    myLabel = tk.Label(window,text=text)
    myLabel.pack()

button = tk.Button(text="Enter", command=myClick)
button.pack()

window.mainloop()