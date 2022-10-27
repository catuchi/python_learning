from tkinter import *

def moveUp(event):
  label.place(x=label.winfo_x(),y=label.winfo_y()-10)
def moveDown(event):
  label.place(x=label.winfo_x(),y=label.winfo_y()+10)
def moveLeft(event):
  label.place(x=label.winfo_x()-10,y=label.winfo_y())
def moveRight(event):
  label.place(x=label.winfo_x()+10,y=label.winfo_y())

window = Tk()
window.geometry("500x500")

window.bind("<w>",moveUp)
window.bind("<s>",moveDown)
window.bind("<a>",moveLeft)
window.bind("<d>",moveRight)
window.bind("<Up>",moveUp)
window.bind("<Down>",moveDown)
window.bind("<Left>",moveLeft)
window.bind("<Right>",moveRight)

myImage = PhotoImage(file="./assets/racecar.png")
label = Label(window,image=myImage,bg="red")
label.place(x=0,y=0)



window.mainloop()