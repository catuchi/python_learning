# str.format() = optional method that gives users more control when displaying output

animal = "cow"
item = "moon"

# print("The "+animal+" jumped over the "+item)
# print("The {} jumped over the {}".format("cow", "moon"))
# print("The {} jumped over the {}".format(animal, item))
# print("The {0} jumped over the {1}".format(animal, item)) # positional argument
# print("The {animal} jumped over the {item}".format(animal="cat", item="stream")) # keyword argument

# text = "The {} jumped over the {}"
# print(text.format(animal, item))

name = "Mikey"

print("Hello, my name is {}".format(name))
# add padding to string (in this example adding 10 spaces after name) (this example is left aligned)
print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name)) # left aligned

# to right align
print("Hello, my name is {:>10}. Nice to meet you".format(name)) # left aligned
# to center
print("Hello, my name is {:^10}. Nice to meet you".format(name)) # left aligned

# to add postional or keyword argument while adding padding, add argument before :
# {0:10} positional
# {name:10} keyword

number = 3.14159

print("The number of pi is {}".format(number))
# to display to two decimal places
print("The number of pi is {:.2f}".format(number))

num = 1000

# display number with comma 
print("The number is {:,}".format(num))
# in binary
print("The number is {:b}".format(num))
# in oct
print("The number is {:o}".format(num))
# in hex with lower case
print("The number is {:x}".format(num))
# in hex with upper case
print("The number is {:X}".format(num))
# in scientific notation with lower case
print("The number is {:e}".format(num))
# in scientific notation with upper case
print("The number is {:E}".format(num))

