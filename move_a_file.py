import os

# move file
source = "/Users/catuchi/Desktop/test_text.txt"
destination = "/Users/catuchi/lighthouse/python/tutorial/test_text.txt"

# try:
#   if os.path.exists(destination):
#     print("There is already a file there")
#   else:
#     os.replace(source, destination)
#     print(source+" was moved")
# except FileNotFoundError:
#   print("{} was not found".format(source))

# move directory
source1 = "/Users/catuchi/Desktop/test_folder"
destination1 = "/Users/catuchi/lighthouse/python/tutorial/test_folder"

try:
  if os.path.exists(destination1):
    print("There is already a folder there")
  else:
    os.replace(source1, destination1)
    print(source1+" was moved")
except FileNotFoundError:
  print("{0} was not found".format(source1))