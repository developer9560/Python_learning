""" 
    object oriented programing concpepst :
    1. object : it is a real world entity ,it is a instance of a class
    2. class : it is a blueprint for creating objects
    3. polymorphism : it is a ability of objects to take multiple forms
    4. inheritance : it is a ability of objects to inherit properties and methods from parent class
    5. encapsulation : it is a ability of objects to hide its properties and methods
    6. abstraction : it is a ability of objects to hide its properties and methods

"""
"""
  class: blueprint for creating objects
    1. Data or Property of class
    2. Function or Method of class
"""

class Atm:
    counter = 1 # this is static / class variable 

    def __init__(self): #this is a constructor , it is special method that is called when an object is created
        self.__pin= ""
        self.__balance=0 
        self.counter = Atm.counter
        Atm.counter += 1
        self.menu()
    
    def menu(self):
        user_input = input("""
        Hello, how would you like to proceed?
        1. Enter 1 to create pin
        2. Enter 2 to deposit
        3. Enter 3 to withdraw
        4. Enter 4 to check balance
        5. Enter 5 to exit
        """) 

        if user_input == "1":
            self.create___pin()
        elif user_input == "2":
            self.deposit()
        elif user_input == "3":
            self.withdraw()
        elif user_input == "4":
            self.check___balance()
        elif user_input == "5":
            
            print("bye")
            return
        else:
            print("Invalid input")
    
    def create___pin(self):
        self.__pin = input("Enter your pin: ")
        print("pin created successfully")
        self.menu()

    def deposit(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            self.__balance += amount
            print("Deposit successful")
            self.menu()  
        else:
            print("Invalid pin")  
            self.menu()

    def withdraw(self):
        temp = input("Enter you pin: ")
        if temp == self.__pin:
            amount = int(input("Enter the amount: "))
            if amount <= self.__balance:
                self.__balance -= amount
                print("Withdraw successful")
                self.menu()
            else:
                print("Insufficient balance")
                self.menu()
        else:
            print("Invalid pin")
            self.menu()
    
    def check___balance(self):
        temp = input("Enter your pin : ")
        if(temp == self.__pin):
            print("total balance : ",self.__balance)
            self.menu()
        else:
            print("Invalid pin")
            self.menu()
    
    def get___pin(self):
        return self.__pin

    def set___pin(self, new___pin):
        self.__pin = new___pin
        print("pin changed successfully")
        self.menu() 

    @staticmethod
    def get_counter():
        return Atm.counter

    @staticmethod
    def set_counter(new_counter):
        Atm.counter = new_counter

sib=Atm()
print(id(sib))
