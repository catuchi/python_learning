# an object is an instance of a class
# we can use programming to mimic real world objects by assigning a combination of
# attributes (what an object is or has (e.g name, age, height)) and
# methods (what an object can do (e.g eat, sleep, sing))

# in order to create an object, we need to create a class
# a class serves as the blueprint that describes what attributes and methods our
# distinct object will have
# you can create your class in the same module or you can create a dedicated to your class

# import class
from car import Car

car_1 = Car("Chevy","Corvette",2022,"red")
car_2 = Car("Ford", "Mustang", 2021, "black")

car_1.drive()
car_2.stop()