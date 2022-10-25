# radio button = similar to checkbox, but you can only select on from a group

from cgitb import handler
from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
  if(x.get() == 0):
    print("You ordered pizza!")
  elif(x.get() == 1):
    print("You ordered hamburger!")
  elif(x.get() == 2):
    print("You ordered hotdog!")
  else:
    print("huh?")

window = Tk()

pizzaImage = PhotoImage(file="./assets/pizza-svgrepo-com.png", height=325, width=325)
hamburgerImage = PhotoImage(file="./assets/hamburger.png", height=325, width=325)
hotdogImage = PhotoImage(file="./assets/hotdog.png", height=325, width=325)
foodImages = [pizzaImage,hamburgerImage,hotdogImage]

x = IntVar()

for index in range(len(food)):
  radio_button = Radiobutton(window,
                             text=food[index], # adds text to radio buttons
                             variable=x,       # groups radiobuttons together if they share the same variable
                             value=index,      # assigns each radiobutton a diff. value
                             padx= 25,
                             font= ("Impact", 50),
                             image=foodImages[index],    #adds image to radiobutton
                             compound="left",            #adds image & left (left-side)
                             indicatoron=0,              #eliminate circle indicators
                             width=650,                  # sets width of radio buttons
                             command=order               # sets radiobutton to function 
                             )
  radio_button.pack(anchor=W)

window.mainloop()