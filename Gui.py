import tkinter as tk

window = tk.Tk()
#label = tk.Label(text="Python rocks!")

label = tk.Label(
    text="Hello, Tkinter",
    foreground="yellow",  # Set the text color to white
    background="blue", # Set the background color to black
    borderwidth=1,
    width=30,
    height=10
)
label.pack()

button = tk.Button(text = "Enter" , bg="pink")
button.pack()

entry = tk.Entry(fg="yellow", bg="blue", width=50)
entry.pack()
entryValue = entry.get()


print("Entered Value: " + entryValue)



window.mainloop()