# listbox = a listing of selectable text items within it's own container

from tkinter import *

def submit():
  food = []

  for index in listbox.curselection():
    food.insert(index, listbox.get(index))

  print(f"You have ordered:")
  for index in food:
    print(index)

  # current_selection = listbox.get(listbox.curselection())

def add():
  listbox.insert(listbox.size(), entry_box.get())
  listbox.config(height=listbox.size())

def delete():
  # listbox.delete(listbox.curselection())
  for index in reversed(listbox.curselection()):
    listbox.delete(index)
    
  listbox.config(height=listbox.size())

window = Tk()

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia",35),
                  width=12,
                  fg="black",
                  selectmode=MULTIPLE
                  )
listbox.pack()

listbox.insert(1,"pizza")
listbox.insert(2,"pasta")
listbox.insert(3,"garlic bread")
listbox.insert(4,"soup")
listbox.insert(5,"salad")

# change the size of listbox
listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submitButton = Button(window, text="submit", command=submit)
submitButton.pack()

addButton = Button(window, text="add", command=add)
addButton.pack()

deleteButton = Button(window, text="delete", command=delete)
deleteButton.pack()

window.mainloop()