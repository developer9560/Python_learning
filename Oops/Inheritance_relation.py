

class User:
    def login(self):
        print("logged in")
    def register(self):
        print("registered")

class Student(User):
    def enroll(self):
        print("enrolled")
    def review(self):
        print("reviewed")

s1 = Student()
s1.register()
s1.login()
s1.enroll()
s1.review()