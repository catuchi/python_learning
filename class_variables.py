from car import Car

car_1 = Car("Chevy","Corvette",2022,"red")
car_2 = Car("Ford", "Mustang", 2021, "black")

# you can the value reassign a class variable
# car_1.wheels = 2

# print(car_1.wheels)
# print(car_2.wheels)

# you dont have to create an object to get the value of a class variable, e.g:
print(Car.wheels)

# if you change the value of a class variable using the class, it will change the value for 
# all instances of the class

Car.wheels = 2

print(car_1.wheels)