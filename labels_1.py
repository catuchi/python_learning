# label = an area widget that holds text and/or an image within a window

from tkinter import *

window = Tk()
# window.config(bg="#5cfcff")

# create a photo image
photo = PhotoImage(file="sharingan.png")

# instantiate a label
label = Label(window,
              text="Hello World",
              font=("Arial",40,"bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound='top')
# add label to window
label.pack()
# another way to add a label to a window
# label.place(x=0,y=0)

window.mainloop()