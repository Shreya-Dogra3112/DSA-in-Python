#syntax
def greet():
    print("Hello")


greet()

# 2 types

#built in functions
print("hello")
len("Python")

#user defined functions
def add():
    a=20
    b=10
    print("sum=",a+b)
add()

#parameters and arguments

def add(a,b): #arguments
    print("Sum:",a+b)
add(10,40) #parameters


#positional arguments

def Student(name , age):
    print("name",name)
    print("age",age)
Student("Shreya",19)

#keyword arguments

def Student(name , age):
    print("name",name)
    print("age",age)
Student( age =20,name="Rahul")


def greet(name = "Shreya"):
    print("HEllo",name)
greet("Priya")
greet()

#return function

def add(a,b):
    return a+b
result = add(10,40)
print("Sum",result)

def square(a):
    return a*a
result = square(2)
print("Square is",result)


#local variable and global variable

def display():
    x=10
    print("LOcal variable:",x)
display()

x=20
def display():
   
    print("Global variable:",x)
display()
print("outside function:",x)