from tkinter import *
from ball import *
import time

window = Tk()

WIDTH = 550
HEIGHT = 500

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volleyBall = Ball(canvas,0,0,100,1,1,"white")
tennisBall = Ball(canvas,0,0,50,4,3,"yellow")
basketBall = Ball(canvas,0,0,125,8,7,"orange")

while True:
  volleyBall.move()
  tennisBall.move()
  basketBall.move()
  window.update()
  time.sleep(0.01)

window.mainloop()