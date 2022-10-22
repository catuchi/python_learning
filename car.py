# create a class
class Car:

  # class variables are declared inside the class but outside the constructor
  wheels = 4        # class variable

  def __init__(self, make, model, year, color):         # this is the constructor
    self.make = make          # variables declared in the constructors are instance variables (e.g self.make)
    self.model = model        # instance variable
    self.year = year
    self.color = color

  def drive(self):
    print("This {} is driving".format(self.model))

  def stop(self):
    print("This {} is stopped".format(self.model))