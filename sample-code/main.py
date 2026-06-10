# this is a comment
"""
ignore this


print('abhinav')

# variable definition
student = "abhinav"

StudentName = "Rahul" # pascal case

studentName = "Vikash" # camel case

student_name = "Abhishek" # snake case

a = 12
print(type(a))

b = 56.8
print(type(b))

c = 12/3
print(type(c))

v = 34j
print(type(v))

st = "abhinav 12345 *&^%#@"
print(type(st))

b = True
print(type(b))

c = False
print(type(c))

d = "A"
print(ord(d))

a = 65
print(chr(a))

a = "SHER"
print(a[1])
print(a[-1])
print(a[3], a[-1])

a = "SHER CODER"
print(a[0:4:1])
print(a[5::1])

a = 12
a = str(12)
print(type(a))

name = "abhinav"
age = 37
print(name, age)
print("hello my name is ", name, " and age is ", age)
print(f"my name is {name} and age is {age}")

age = print("what is your age?")
print(age)

a = 20
b = 5
print(a + b)
print(a - b)
print(a/b)
print(a//b)

# power: 5^2
print(5**2)
print(5**100)
print(32%6)

a = 20
#a = a + 20
a += 20
print(a)

#a = a + 40
a += 40
print(a)

a = 12
b = 12
print(a == b)
print(a != b)

a = 10
if a > 10:
    print("task A")
elif a == 10:
    print("task B")
else:
    print("task C")

a = range(1,21,1)
for i in a:
    print(i)


for i in range(21):
    print(i)

a = "ABHINAV"

for i in range(len(a)):
    print(a[i])

for char in a:
    print(char)

for i in range(1, 10):
    if i == 5:
        break
    else:
        print(i)

for i in range(1, 10):
    if i == 54:
        print("break statement is executed")
        break
    print(i)
else:
    print("break statement is not executed")

# print sum of n numbers

n = 10
sum = 0

for i in range(1, n+1):
    sum += i

print(f"sum of {n} numbers is {sum}")

a = 1

while a <= 30:
    print(a)
    a = a + 1

import random

num = random.randint(1, 11)
print(f"num is {num}")

def hello():
    print("this is hello function")

hello()

#default parameter
def sum(a, b=9):
    print(f"sum is {a + b}")

sum(1, 2)
sum(4, 4)
#default argument
sum(4)

def profile(name,age):
    print(f"name is {name}, age is {age}")

#keyword argument
profile(age=22, name="abhinav")

def ispalindrome(str):
    rev = ""

    for i in range(len(str)-1, -1, -1):
        rev += str[i]

    if rev == str:
        print(f"{str} is a palindrome")
    else:
        print(f"{str} is not is palindrome")

ispalindrome("NAMAN")
ispalindrome("ABHINAV")

list = [1,2,3,4,5]
print(list)
list.append(6)
list.append(7)
print(list)

list = [1,3,4,5]
print(list)
list.insert(1,2)
print(list)
list.extend([7,8])
print(list)

# tuple
a = (1,2,3,3)
print(type(a))

# list
# a = [4]
# print(type(a))

for i in a:
    print(i)

for i in range(len(a)):
    print(a[i])

print(f"index of 3 is {a.index(3)}")
print(f"count of 3 is {a.count(3)}")

a = (4,2)
print(type(a))

# dict
a = {1:"abhi", 2:4}
print(type(a))
print(a[1])
print(a[2])

a.update({50:500})
print(a)

a[1] = "das"
a[3] = True
print(a)
del a[1]

print(a)

a = 0

try:
    print(10/a)
except Exception as err:
    print(f"exception is {err}")
else:
    print("there is no exception")
finally:
    print("i will run no matter what")
print("finally came here")
"""

a = 15

try:
    if a < 10 or a > 20:
        raise ValueError("values should be in between 10 and 20")
    else:
        print(f"value of a is {a}")
except Exception as err:
    print(f"error raised is {err}")

print("finally")
