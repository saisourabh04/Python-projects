#object oriented programming
#defining a class
class Person:
    def __init__(self,first_name,last_name,age=None):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.address=None
        self.phone=None
        self.email=None

        print('hi')
    def show_info(self):
        print(f"{self.first_name} {self.last_name} {self.age}")

    def add_info(self):
        print(f'Hi,{self.first_name},enter your communication details ')
        self.address=input('enter your address: ')
        self.phone=input('enter your Phone: ')
        self.email=input('enter your e-mail: ')




#creating an object from a person class
x=Person('jim','jon',33)
y=Person('jimmy','jonny')
x.show_info()
x.add_info()
y.add_info()
# x=5
# y=2.1
# z='hello'
# a=[]
# print(type(john))
# print(type(x))
# print(type(y))
# print(type(z))
# print(type(a))

#inheritance
