# logical operators (and, or, not)

temp = int(input("What is the temperature outside?: "))

# print(type(temp))

if not(temp >= 0 and temp <= 30):
  print("bad weather")
elif not(temp < 0 or temp > 30):
  print("good weather!")