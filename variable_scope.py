# scope = The region that a variable is recognized
#         A variable is only available from inside the region it is created
#         A global and locally scoped versions of a variable can be created

name = "Ichigo" # global scope

def display_name():
  name = "Kurosaki" # local scope
  print(name)

display_name()
print(name)