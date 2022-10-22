class Animal:

  def eat(self):
    print("This animal is eating")

# without method overriding
# class Rabbit(Animal):
#   pass

# rabbit = Rabbit()
# rabbit.eat()

# with method overriding
class Rabbit(Animal):

  def eat(self):
    print("This rabbit is eating a carrot")

rabbit = Rabbit()
rabbit.eat()