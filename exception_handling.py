# exception = events detected during execution that interrupts the flow of a program

# try:
#   numerator = int(input("Enter a number to divide: "))
#   denominator = int(input("Enter a number to divide by: "))
#   result = numerator / denominator
#   print(result)
# except Exception:
#   print("something went wrong :(")

# note it is not good practice to have general exception like in line 8
# instead write an exception to handle a certain error.
# e.g

# try:
#   numerator = int(input("Enter a number to divide: "))
#   denominator = int(input("Enter a number to divide by: "))
#   result = numerator / denominator
#   print(result)
# except ZeroDivisionError:
#   print("You can't divide by zero")
# except NameError:
#   print("Enter only numbers please")
# except ValueError:
#   print("Enter only numbers please")
  # you can add the last except to cover all bases
# except Exception:
#   print("something went wrong :( ")

# you can choose to print the error
# try:
#   numerator = int(input("Enter a number to divide: "))
#   denominator = int(input("Enter a number to divide by: "))
#   result = numerator / denominator
#   print(result)
# except ZeroDivisionError as e:
#   print(e)
#   print("You can't divide by zero")
# except NameError as e:
#   print(e)
#   print("Enter only numbers please")
# except ValueError as e:
#   print(e)
#   print("Enter only numbers please")

# you can add an else statement that will run if there are no errors
# try:
#   numerator = int(input("Enter a number to divide: "))
#   denominator = int(input("Enter a number to divide by: "))
#   result = numerator / denominator
#   # print(result)
# except ZeroDivisionError as e:
#   print(e)
#   print("You can't divide by zero")
# except NameError as e:
#   print(e)
#   print("Enter only numbers please")
# except ValueError as e:
#   print(e)
#   print("Enter only numbers please")
# else:
#   print(result)

# you can add a finally which will always run if there are errors or not
try:
  numerator = int(input("Enter a number to divide: "))
  denominator = int(input("Enter a number to divide by: "))
  result = numerator / denominator
  # print(result)
except ZeroDivisionError as e:
  print(e)
  print("You can't divide by zero")
except NameError as e:
  print(e)
  print("Enter only numbers please")
except ValueError as e:
  print(e)
  print("Enter only numbers please")
else:
  print(result)
finally:
  print("This will always run")