"""
Abstraction : it is a ability of objects to hide its properties and methods
Inheritance : it is a ability of objects to inherit properties and methods from parent class
Polymorphism : it is a ability of objects to take multiple forms

RelationShip between classes

1. Aggregation : (Has A) it is a relationship between two classes where one class is a part of another class
2. Composition : it is a relationship between two classes where one class is a whole of another class
3. Inheritance : (Is A) it is a relationship between two classes where one class is a child of another class

"""

class Customer:
    def __init__ (self, name, age , address):
        self.name = name
        self.age = age
        self.address = address
        self.menu()

    def menu(self):
            user_input = input("""

            Hello, how would you like to proceed?
            1. Enter 1 to view profile
            2. Enter 2 to edit profile
            3. Enter 3 to exit
            """) 

            if user_input == "1":
                self.view_profile()
            elif user_input == "2":
                self.edit_profile()
            elif user_input == "3":
                
                print("bye")
                return
            else:
                print("Invalid input")

    def view_profile(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"City: {self.address.city}")
        print(f"State: {self.address.state}")
        print(f"Pincode: {self.address.pincode}")
        self.menu()

    def edit_profile(self):
        new_name = input("Enter new name: ")
        self.name = new_name
        new_age = input("Enter new age: ")
        self.age = new_age
        new_city = input("Enter new city: ")
        new_state = input("Enter new state: ")
        new_pincode = input("Enter new pincode: ") 
        self.address = Address(new_city, new_state, new_pincode)
        self.menu()

class Address:
    def __init__ (self, city, state, pincode):
        self.city = city
        self.state = state
        self.pincode = pincode


    def change_address(self, new_city, new_state, new_pincode):
        self.pincode = new_pincode
        self.state = new_state
        self.city = new_city
    
add = Address("Delhi", "Delhi", 110001)
cust = Customer("suraj kumar", "10", add)
