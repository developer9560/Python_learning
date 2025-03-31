f = open("test.txt", "w+")
f.write("hello world")
f.close()

f = open("test.txt", "a")
f.write(" this is apend text")

f.close()