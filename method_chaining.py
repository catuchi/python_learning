# method chaining = calling multiple methods sequentially
#                   each call performs an action on the same object and returns self

class Car:

  def turn_on(self):
    print("You start the engine")
    return self

  def drive(self):
    print("You drive the car")
    return self

  def brake(self):
    print("You step on the brakes")
    return self

  def turn_off(self):
    print("You turn off the engine")
    return self

car = Car()

# when using method chaining, each method has to return something (in the above example class, we will
# add a return self to each method)

# car.turn_on().drive()
# car.brake().turn_off()
# car.turn_on().drive().brake().turn_off()

car.turn_on()\
  .drive()\
  .brake()\
  .turn_off()
