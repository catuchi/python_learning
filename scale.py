from tkinter import *

def submit():
  print(f"The temperature is: {scale.get()} degrees C")

window = Tk()

scale = Scale(window, 
              from_=100, 
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas",20),
              tickinterval=10,
              showvalue=0,
              resolution=5,
              troughcolor='#69eaff',
              fg="#ff1c00",
              bg="#111111"
              )
scale.set(((scale['from']-scale['to'])/2)+scale['to'])          # set default value to middle value

scale.pack()

button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()