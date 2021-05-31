from tkinter import *

root = Tk()

e = Entry(root,width=50)
e.pack()

def myClick():
    name = e.get()
    hello = "Hello there " + name
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name",command=myClick)
myButton.pack()

root.mainloop()