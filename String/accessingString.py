msg = "Hello"
a = msg[0] # Accessing the first character of the string
print(a) # H
b = msg[4] # yields o
c = msg[-0] # yields H -0 is same as 0
d = msg[-1] # yields o -1 is same as 4
e = msg[-2] # yields l 
f = msg[-5]  #yields H

print(b,c,d,e,f) # o H o l H


# note: Using too large an indes reposts an error, but using too large index while slicing is handled elegantly

str = ' Ragting'
print(str[3:100]) # ting
print(str[3:]) # ting
print(str[:3]) # Ra
print(str[-0:]) # Ragting
print(str[-3:]) # ting
print(str[:-3]) # Rag


# wheater one string is part of another can be found out using in .
print('e' in 'Hello') # True
print('lo' in 'Hello') # True
print('z' in "hello") # False



