from tkinter import *

window = Tk()

def moveUp(event):
  canvas.move(img,0,-10)
def moveDown(event):
  canvas.move(img,0,10)
def moveLeft(event):
  canvas.move(img,-10,0)
def moveRight(event):
  canvas.move(img,10,0)

window.bind("<w>", moveUp)
window.bind("<s>", moveDown)
window.bind("<a>", moveLeft)
window.bind("<d>", moveRight)
window.bind("<Up>", moveUp)
window.bind("<Down>", moveDown)
window.bind("<Left>", moveLeft)
window.bind("<Right>", moveRight)

canvas = Canvas(window, width=500, height=500)
canvas.pack()

myImage = PhotoImage(file="./assets/racecar.png")
img = canvas.create_image(0,0,image=myImage,anchor=NW)

window.mainloop()