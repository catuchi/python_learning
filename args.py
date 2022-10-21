# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments

def add(*args): # can also be displayed as add(*stuff) or add(*jfdf) doesnt matter
  sum = 0
  # we cant change a tuple or reassign it's elements
  # we can change a list and reassign it's elements
  # we can create a list from a tuple
  args = list(args)
  args[0] = 8
  for x in args:
    sum += x
  return sum

print(add(1,2,4,5,6,7))