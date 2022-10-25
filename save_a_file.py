from tkinter import *
from tkinter import filedialog

def saveFile():
  file = filedialog.asksaveasfile(initialdir='/Users/catuchi/lighthouse/python/tutorial',
                                  defaultextension='.txt',
                                  filetypes=[
                                    ("Text file", ".txt"),
                                    ("HTML file", ".html"),
                                    ("All files", ".*")
                                  ])
  if file is None:
    return
  filetext = str(text.get(1.0,END)) # to use the text area
  # to use to console window to write to a file instead of the text area
  # filetext = input("Enter some text I guess: ")
  file.write(filetext)
  file.close()

window = Tk()

button = Button(text='save', command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()