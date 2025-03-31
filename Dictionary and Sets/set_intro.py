# set is the collection of the unoredered elements
# it stores only unique elements
# it is immutable
# it is written with curly brackets
# it is unordered, and does not allow duplicates
# we can store different data types in set but we can not store list and dictionary in set becuase it is mutable

collection = {1,2,3,4,5, "suraj", "kumar"}
print(collection)
print(type(collection))

# collection[1] = "suraj" it will give error because set is unoredered 

emepty_set = set()
print(type(emepty_set))