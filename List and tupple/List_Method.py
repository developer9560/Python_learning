# methods is a function that is defined inside a class
# list methods
# 1. append()      it will add an element at the end
# 2. insert(index, element)    it will add an element at the specified index
# 3. remove()    it will remove first an element but it will give error if the element is not present
# 4. pop()      it will remove an element but it will give error if the index is not present
# 5. clear()     it will remove all the elements
# 6. count()     it will count the number of elements
# 7. sort()     it will sort the list it sort in assending order
# 8. reverse() it wil reverse the list
list = [1,2,3,4,5,7]
list.append(6)
print(list)

list.insert(4,7)
print(list)

list.remove(5)
print(list)  

list.pop(2)
print(list)

print(list.count(7))

list.sort()
print(list)

list.sort(reverse=True)
print(list)

list.reverse()
print(list)

list.clear()
print(list)