# GUI = graphical user interface

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as a container to hold or contain these widgets

from tkinter import *

window = Tk()                     # instantiate an instance of a window
window.geometry("420x420")        # set size of window
window.title("Bro Code first GUI Program")

# icon = PhotoImage(file='sharingan.png')     # didnt work for some reason
icon = PhotoImage('sharingan.png')
window.iconphoto(True,icon)
window.config(background="#5cfcff")

window.mainloop()                 # place window on computer screen, listen for events