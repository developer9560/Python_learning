# loops are use for sequential traversal. Fro traversing list, string, tuples etc.


list = [1,2,3,4,5]
for i in list:
    print(i)

for i in "suraj":
    print(i)

for i in (1,2,3,4,5):
    print(i)
else:
    print("out of loop")

# range() : range fucntions return a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.\
# range(start, stop, step)

for i in range(5):
    print(i)

for i in range(2,5):
    print(i)

for i in range(2,10,2):
    print(i)