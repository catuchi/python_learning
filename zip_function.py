# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                   creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

# users = zip(usernames, passwords)           # users is a zip object
# to convert users to a list
# users = list(users)
# to convert users to a dictionary
# users = dict(users)
# print(users)

# for i in users:
#   print(i)

# for key,value in users.items():
#   print(key+" : "+value)

users = zip(usernames, passwords, login_date)

for i in users:
  print(i)