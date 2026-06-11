"""
class Factory:
    a = 12 #attribute

    def hello(self): #method
        print("how are you?")

    print("i am getting initialized")

print(Factory().a)
Factory().hello()

obj = Factory()
print(obj.a)
obj.hello()

class Factory:

    def __init__(self, material, zips, pockets):
        self.material = material
        self.zips = zips
        self.pockets = pockets

    def show(self):
        print(f"object details are {self.material}, {self.zips}, {self.pockets}")

reebok = Factory("leather", 3, 2)

campus = Factory("nylon", 3, 3)

print(campus.pockets)
print(campus.show())

class Animal:
    
    name = "lion" #class attribute
    
    def __init__(self, age):
        self.age = age #instance attribute

    def instance_method(self): #instance method
        print(f"instance method your age is {self.age}")

    @classmethod
    def hello(cls): #class method
        print("inside class method")

    @staticmethod
    def static_method(): #static method
        print("inside static method")

obj = Animal(12)
obj.instance_method()
obj.hello()
obj.static_method()
"""
class Parent: #parent class / super class
    a = 12
    def show(self):
        print("inside the show method")

class Child(Parent): #child class / sub class
    pass

obj = Parent()
print(obj.a)
obj1 = Child()
obj1.show()
