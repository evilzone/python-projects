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


#inheritance
class Animal:

    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"hello your name is {self.name}")

class Human(Animal):

    def __init__(self, name, age):
        super().__init__(name)
        self.age = age
    
    def show(self):
        print(f"hello your name is {self.name} age is {self.age}")

animal = Animal("lion")
human = Human("abhinav",12)

animal.show()
human.show()


#multiple inheritance
class Animal:

    def __init__(self, name):
        pass

class Human:

    def __init__(self, name, age):
        pass

class Robot(Human, Animal):
    name = "charlie"

obj = Robot("abhi", 12)


#multi-level inheritance
class Factory:

    def __init__(self, material, zips):
        self.material = material
        self.zips = zips

class BhopalFactory(Factory):

    def __init__(self, material, zips, color):
        self.material = material
        self.zips = zips
        self.color = color

class PuneFactory(BhopalFactory):

    def __init__(self, material, zips, color, pockets):
        self.material = material
        self.zips = zips
        self.color = color
        self.pockets = pockets



#polymorphism
#method overriding
class Animal:
    
    def show(self):
        print("this is Animal class show method")

class Human(Animal):

    def show(self):
        print("this is Human class show method")

obj = Human()
obj.show()


class Factory:
    a = "test"

    def show(self):
        print("inside show method")

class Bhopal(Factory):

    def show2(self):
        print(super().a)

obj = Bhopal()
obj.show2()


#abstract class and abstract method
from abc import ABC, abstractmethod

class abstract(ABC):

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Square(abstract):

    def __init__(self, side):
        self.side = side

    def area(self):
        print("this is area method")

    def perimeter(self):
        print("this is perimeter method")

class Circle(abstract):

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("this is area method")

    def perimeter(self):
        print("this is perimeter method")

obj = Square(4)



# dunder methods
class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"name of the animal is {self.name}"

    def __add__(self, other):
        sum = 0

        for i in other:
            sum += i.age

        return f"sum of ages is {self.age + sum}"

obj = Animal("lion", 12)
obj2 = Animal("dolphin", 13)
obj3 = Animal("Shark", 12)

print(obj)
print(obj2)

print(obj+(obj2,obj3))


class Animal:

    @property
    def show(self):
        print("inside show method")

obj = Animal()
obj.show


#decorator
def decorate(func):
    def wrapper(a, b):
        print("before addition")
        func(a, b)
        print("after addition")
    return wrapper

@decorate
def addition(a, b):
    print(f"addition of a and b is {a+b}")

addition(12,13)


def addition(*args):
    sum = 0
    for i in args:
        sum += i

    print(f"sum of args elements is {sum}")

addition(1,2,3,4,5,6,2,3)

"""

def information(**kwargs):
    print("your information is: \n\n")

    for i in kwargs:
        print(f"{i} : {kwargs[i]}")

information(name="abhinav", age=12, job="AI/ML")

l = [i for i in range(1, 21) if i % 2 == 0]
print(l)

dict = {i : i*i for i in range(1,10)}
print(dict)

unique_even_squares = {i*i for i in range(10) if i%2==0}
print(unique_even_squares)

addition = lambda a,b : a+b

print(addition(12,12))

ans = lambda a : "even" if a%2==0 else "odd"

print(ans(2))

a = [1,2,3,4]

result = map(lambda x : x*2, a)
print(list(result))

def even(x):
    if x%2==0:
        return True
    else:
        return False

a = [1,2,3,4,5,6,7,8,9,10]
#result = filter(even,a)
result = filter(lambda x : True if x%2==0 else False, a)
print(list(result))
