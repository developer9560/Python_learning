class Phone:
    def __init__(self, brand, price, camera):
        self.brand = brand
        self.price = price
        self.camera = camera
    def buy(self):
        print("Buying a phone")


class SmartPhone(Phone):
    def buy(self): #overriding , method and parent class have same name
        print("Buying a smartphone")


s1 = SmartPhone("Nokia", 10000, "16MP")
s1.buy()

"""
Method Overriding --> Polymorphism : it is a ability of objects to take multiple forms
Method Overloading 
Operator Overloading --> 
"""