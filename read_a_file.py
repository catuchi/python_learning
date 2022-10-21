with open("test.txt") as file:
  print(file.read())

# with exception handling
try:
  with open("text.tx") as file:
    print(file.read())
except FileNotFoundError:
  print("That file was not found :( ")