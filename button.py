# button = you click it, then it does stuff

from tkinter import *

count = 0

def click():
  global count   
  count+=1                   #list variable as global
  print(count)

window = Tk()

photo = PhotoImage(file='./yami_no_sharingan.png',height=400,width=400)

button = Button(window,
                text="click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="top")
button.pack()

window.mainloop()