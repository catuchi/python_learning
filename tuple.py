# tuple = collection which is ordered and unchangeable
#         used to group together related data

student = ("Mikey", 28, "male")

print(student.count("Mikey"))
print(student.index("male"))

print(student[0])

for i in student:
  print(i)

if "Mikey" in student:
  print("Mikey is so cool")