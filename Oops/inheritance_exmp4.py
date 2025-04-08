class Parent:
    def __init__(self, num):
        self.__num = num
        
    def get_num(self):
        return self.__num

"""if child have own constructor then it will override the parent constructor and don't call parent constructor"""
class Child(Parent):
    def __init__(self, num, val):
        self.__val = val
        
    def get_val(self):
        return self.__val

son = Child(10, 20)
print("Parents num: ",son.get_num())
print("Children num: ",son.get_val())