# entry widget = textbox that accepts a single line of user input

from tkinter import *
from turtle import right

def submit():
  username = entry.get()
  print(f"Hello {username}")
  entry.config(state=DISABLED)

def delete():
  entry.delete(0,END)

def backspace():
  entry.delete(len(entry.get())-1, END)

window = Tk()

entry = Entry(window,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black")
              # show="*"    # use to show a different character input, very useful when typing passwords

# entry.insert(0,"Spongebob")     # insert some defaut text for entry box
entry.pack(side=LEFT)

submit_button = Button(window, text="submit", command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window, text="delete", command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window, text="backspace", command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()