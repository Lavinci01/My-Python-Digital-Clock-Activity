from tkinter import *
from tkinter.ttk import *

from time import strftime

root = Tk()
root.title("MAYORAL DIGITAL CLOCK")

def time():
    string = strftime("%H:%M:%S %p MAYORAL")
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("courier new", 50), background="black", foreground="red")
label.pack(anchor="s")
time()

mainloop()
