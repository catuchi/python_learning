# label = an area widget that holds text and/or an image within a window

from tkinter import *
from turtle import bgcolor

window = Tk()
# window.config(bg="#5cfcff")

# instantiate a label
label = Label(window,text="Hello World")
# add label to window
# label.pack()
# another way to add a label to a window
label.place(x=0,y=0)

window.mainloop()