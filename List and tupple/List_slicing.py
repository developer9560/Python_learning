# Similar to String Slicing
# listName[startIndex:endIndex:stepSize]

# listName[startIndex:endIndex]
# listName[startIndex:]
# listName[:endIndex]
# listName[:]

marks = [14, 20,50, 4, 5]
print(marks[1:4]) # [20, 50, 4]
print(marks[1:]) #[2o,50,4,5]
print(marks[:4])#[14,20,50,4,5]
print(marks[:]) #[14,20,50,4,5]

print(marks[-1]) # 5
print(marks[-2]) # 4

print(marks[-1:2]) # empty list due to index out of range
print(marks[1:-1]) # [20,50,4]