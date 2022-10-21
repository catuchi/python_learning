# dictionary = A changeable, unordered collection of unique key:value pairs
#              Fast because they use hashing, allow us to access a value quickly

capitals = {
  "Canada": "Ottawa",
  "USA": "Washington DC",
  "India": "New Dehli",
  "China": "Beijing",
  "Russia": "Moscow"
}

capitals.update({"Germany": "Berlin"})
capitals.update({"USA": "Las Vegas"})
capitals.pop('China')
capitals.clear()

# print(capitals["Canada"])

# if key does not exist, this will throw an error
# print(capitals["Germany"])
# but this won't
# print(capitals.get('Germany'))

# print(capitals.keys())
# print(capitals.values())

# print(capitals)
# print(capitals.items())

for key,value in capitals.items():
  print(key, value)