#Super keyword is used to call the parent class constructor
#Super keyword is used to call the parent class method
#Super keyword is used to call the parent class variable
#Super keyword is used to call the parent class function

class Phone:
    def __init__(self, brand, price, camera):
        print("Inside the phone Constructor")
        self.brand = brand
        self.price = price
        self.camera = camera
    def buy(self):
        print("Buying a phone") 

class SmartPhone(Phone):
    def __init__(self, brand, price, camera, ram, rom):
        super().__init__(brand, price, camera)
        self.ram = ram
        self.rom = rom
        
    def buy(self):
        print("Buying a smartphone")
        super().buy()

s1 = SmartPhone("Nokia", 10000, "16MP", "4GB", "64GB")
s1.buy()