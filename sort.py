# sort() method   = used with lists
# sort() function = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs"]

# students.sort()
# students.sort(reverse=True) # to reverse the sort order

# for i in students:
#   print(i)

# for things other than lists e.g tuple
# students = ("Squidward", "Sandy", "Patrick", "Spongebob", "Mr.Krabs")

# sorted_students = sorted(students)    # note sorted() returns a list
# reversed_sorted_students = sorted(students, reverse=True)    # to reverse

# # print(sorted_students)

# for i in reversed_sorted_students:
#   print(i)

# students = [
#   ("Squidward", "F", 60),
#   ("Sandy", "A", 33),
#   ("Patrick", "D", 36),
#   ("Spongebob", "B", 20),
#   ("Mr.Krabs", "C", 78)
# ]

# students.sort()       # default sort which is also sorting by the first column (in this case the names)

# for i in students:
#   print(i)

# to sort the students based on grades
# grade = lambda grades:grades[1]
# students.sort(key=grade)

# for i in students:
#   print(i)

students = (
  ("Squidward", "F", 60),
  ("Sandy", "A", 33),
  ("Patrick", "D", 36),
  ("Spongebob", "B", 20),
  ("Mr.Krabs", "C", 78)
)

grade = lambda grades:grades[1]
sorted_students = sorted(students, key=grade)

for i in sorted_students:
  print(i)

# note the sorted() can also be used to sort a list