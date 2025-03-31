# class Customer:
#     def __init__(self, name , gender):
#         self.name = name
#         self.gender = gender


# def greet(customer):
#     if customer.gender =="Male":
#         print("Hello",customer.name, "sir")
#     else:
#         print("Hello", customer.name, "ma'am")
    

# cust = Customer("suraj kumar", "Male")
# greet(cust)
class Customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age


def greet(customer):
   print("Hello", customer.name, "and i am ", customer.age, "years old\n")
  

    
c1 = Customer("suraj kumar", 20)
c2 = Customer("Prince",18)
c3 = Customer("Pankaj", 25)
L = [c1,c2,c3]

for i in L:
    greet(i)