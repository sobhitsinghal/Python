# import cv2
# import math

# This is a comment
# print("Hello world")
# print(math.gcd(3,6))
'''
This is a multi line comment

'''
# This is also a comment
# print(5+8)
# if(age<18):
#     print("hello")


a = 34
b = "Anuj"
c = 45.32
d = 3

# print(a  + d)
# print(a - d)
# print(a * d)
# Wrong syntax
# anuj project = 45
# print(a / d)
# Rules for creating variables
# 1. variable should start with a letter or an underscore
# 2. variable cannot start with a number
# 3. It can only contain alpha numeric characters
# 4. Variable names are case sensitive. Harry and harry are two different variables

# typeA = type(a)
# typeB = type(b)
# print(typeB)
# e = "31"
# e = float(e)
# e = str(455)
# e = int("34")
# e = 3.14
# print(type(e))
# print(e+2)


name = "Deepak, Shubham, rohit"
name = "Henry"
# print(name[2:5])
# print(name)
# print(name.strip())
# print(len(name))
var = name.lower()
var = name.upper()
var = name.replace("nr", "t")
var = name.replace(",", '\n')
# print(var)

stri = "This is a "
name1 = "Harry"
name2 = "Harsh"
stri2 = "This is not a"
# print(stri + name)
# temp = "This is a {1} and he is a good boy named {0}".format(name1, name2 )
temp = f"This is a {name2} and he is a good boy {name1}"
# print(temp)

'''
Python Collections:
1. List
2. Tuples
3. Set 
4. Dictionary

'''

# List
lst = [61, 2, 3, 4, 6, 41]
# var = type(list)
# lst[2] = 45
# var = lst[2]
# lst.append(100)
# lst.insert(1,100)
# lst.remove
# lst.pop()
# del lst[3]
# del lst[3]
lst.clear()
var = lst
# var = len(1st)
# var = lst[1:4]
print(var)

# Tuple
a = ("harry", "shubh", "Rohan")
var = a
var = list(a)
var = type(a)

# Cannot do this
# a[0] = "Vikram"
# print(var)

# Set
s1 = {23, 2, 2, 2, 2, 2, 7, 3, 2, 1, 2, 2, 12, 6, 3, 12, }
# s1.add(44444)
# s1.update([12,12,423,3423,634,123,432,23])
print(len(s1))
# s1.remove(1666)
# Like list you can use: .pop, .clear, del
# and.. intersection, union
# s1.discard(1666)
print(s1)
subhDict = {
    "name": "Subham",
    "Class": "4th",
    "Marks": 34.34,
    "Hours In School": 6
}
subhDict["Marks"] = 34
print(subhDict["Marks"])
subhDict.pop("Marks")
# del, clear, pop, update
# print(subhDict)

# age = 34
age = input("Enter Your Age\n")
age = int(age)


# print(type(age))
# if(age>18):
#    print("You can drive a car")
# elif(age==18):
#    print("You are an awesome teen")

# else:
#    print("You cannot drive")

# Loops:
# Scenario: you have to print numbers between 1 to 1000
# for i in range(0, 1000):
#    print(i)
# li = [1, 432, "this"]
# for item in li:
#    print(item)
# Quiz: Use for loop to iterate dictionary, set and tuples
# i = 0
# while(i<100):
#    i = i + 1
#    if i == 78:
#        continue
#    print(i + 1)

# Functions
# def greet():
#    print("Good morning sir")
#    print("Good morning mam")
#    print("Good morning Uncle")

# greet()
# def sum(a = 65, b):
#    print("Running sum")
#    c = a + b
#    return c
# d = sum(34, 45)
# print(d)

class Employee:
    def __init__(self, gname, gsalary):
        self.name = gname
        self.salary - gsalary


subham = Employee("subham", 34)
print(subham.name)
print(subham.salary)





















