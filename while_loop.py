# name = ""
name = None

# while len(name) == 0:
#   name = input("Enter your name:")

while not name:
  name = input("Enter your name: ")

print("Hello " + name)