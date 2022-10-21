# keyword arguments = arguments preceded by an identifier when we pass them to a function
#                     The order of the arguments doesn't matter, unlike positional arguments
#                     Python knows the names of the arguments that our function receives

def greeting(first, middle, last):
  print("Hello "+last+" "+middle+" "+first)

greeting(middle="D.", last="Monkey", first="Luffy")