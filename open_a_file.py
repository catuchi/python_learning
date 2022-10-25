from tkinter import *
from tkinter import filedialog

def openFile():
  filepath = filedialog.askopenfilename(initialdir='/Users/catuchi/lighthouse/python/tutorial', 
                                        title="Open File",
                                        filetypes=(("text files","*.txt"),("all files","*.*")))
  file = open(filepath, 'r')
  print(file.read())
  file.close()

window = Tk()

button = Button(text="Open", command=openFile)
button.pack()

window.mainloop()