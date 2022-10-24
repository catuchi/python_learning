# prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

# abstract class = a class which contains one or more abstract methods
# abstract methods = a method that has a declaration but does not have an implementation

from abc import ABC, abstractmethod # to create an abstract class and abtract method

class Vehicle(ABC):

  @abstractmethod
  def go(self):
    pass

class Car(Vehicle):

  def go(self):
    print("You drive the car")

class Motorcycle(Vehicle):

  def go(self):
    print("You ride the motorcycle")

vehicle = Vehicle()
car = Car()
motorcycle = Motorcycle()

vehicle.go()
car.go()
motorcycle.go()

