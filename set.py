# set = collection which is unordered, unindexed. No duplicate values

from re import U


utensils = {"fork", "knife", "spoon"}
dishes = {"bowl", "plate", "cup", "knife"}

# good_set = {"fork", "knife", "spoon"}
# bad_set = {"fork", "knife", "spoon", "spoon", "fork"}

# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# dishes.update(utensils)
# dinner_table = dishes.union(utensils)

# for x in dinner_table:
#   print(x)

# print(utensils.difference(dishes))
print(utensils.intersection(dishes))