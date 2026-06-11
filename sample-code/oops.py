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
"""
class Animal:
    name = "lion" #class attribute
    
    def __init(self, age):
        self.age = age #instance attribute

    def instance_method(self): #instance method
        print("instance method")
        
