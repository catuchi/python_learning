# slicing = create a substring by extracting elements from another string
#           indexing[] or slice()
#           [start:stop:step]

name = "Ichigo Kurosaki"

first_name = name[0:6]
# or
# first_name = name[:6]

index = 7
last_name = name[index:len(name)]
# or
# last_name = name[index:]

# funky_name = name[:15:2]
# or
funky_name = name[::2]

reversed_name = name[::-1]

# print(reversed_name)

# slice
website = "http://facebook.com"
website1 = "http://google.com"

slice = slice(7,-4)

print(website[slice])
print(website1[slice])