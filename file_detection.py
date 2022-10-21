from genericpath import isdir, isfile
import os

path = "/Users/catuchi/Desktop/test_text.txt"
path2 = "/Users/catuchi/Desktop/test_folder"

if os.path.exists(path2):
  print("Location exists")
  if os.path.isfile(path2):
    print("That is a file")
  elif os.path.isdir(path2):
    print("That is a directory")
else:
  print("Location does not exist")