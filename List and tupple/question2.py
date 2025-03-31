# write the program to check if a list constains a palindrom of elements

list1 = [1,2,3,2,1]
list2 = list1.copy()
list2.reverse()

if(list1 == list2):
    print("list is palindrom")
else:
    print("list is not palindrom")
    
