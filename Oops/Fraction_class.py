class Fraction:
    def __init__ (self, num , den):
        self.num = num
        self.den = den

    def __str__(self):
        return str(self.num) + "/" + str(self.den)
        # return f"{self.num}/{self.den}"
        #retrun "{}/{}".format(self.num , self.den)

    def __add__(self , other):
        temp_num = self.num * other.den + self.den * other.num
        temp_den = self.den * other.den
        return Fraction(temp_num , temp_den)
        # return "{}/{}".format(temp_num , temp_den)

    def __mul__ (self, other):
        temp_num = self.num * self.den
        temp_den = self.den * other.den
        return Fraction(temp_num, temp_den)
    
    def __truediv__ (self, other):
        temp_num =self.num * other.den
        temp_den = self.den * other.num
        return Fraction(temp_num, temp_den)


num1 = (Fraction(3,4))
num2 = (Fraction(1,2))



num = num1 + num2
mul = num1 * num2


print(num)
print(mul)
print(type(num))
