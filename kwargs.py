# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword arguments

# def hello(first, last):
#   print("Hello "+last+" "+first)

# hello(first="Luffy", middle="D.", last="Monkey")

def hello(**kwargs):  # also you don't have to call it **kwargs you can name it anything like **names
  # print("Hello "+kwargs["last"]+" "+kwargs["first"]) # will still work
  # another way
  print("Hello", end=" ")
  for key,value in kwargs.items():
    print(value, end=" ")

hello(first="Luffy", middle="D.", last="Monkey")