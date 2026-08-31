# FUNCTION: TYPES OF ARGUMENTS
1.QUESTION: Create a function add(a,b)and call it with 10 and 20
def add(a,b):
    return a + b
print(add(10,20))
-------------------------------------------------------------------------------------------
2.QUESTION:  Create a function student(name, age) that prints the name and age. Call it with your own values.
def function(name,age):
    return name,age
print(function("anu",21))
---------------------------------------------------------------------------------------------------------------
3.QUESTION:  Create a function employee(name, salary, department) and call it using positional arguments.
def function(name,salary,department):
    return name,salary,department
print(function("anu",24000,'CSE'))
----------------------------------------------------------------------------------------------------------------------
4.QUESTION: Create a function multiply(a, b, c) and calculate the multiplication of three numbers.
def multiply(a,b,c):
    return a*b*c
print(multiply(10,20,30))
----------------------------------------------------------------------------------------------------------------------------------
5.QUESTION: Create a function details(name, age, city) that prints all three details.
def function(name,age,city):
    return name,age,city
print("usha",21,"nellore")
----------------------------------------------------------------------------------------------------------------------------
6.QUESTION: Create student(name, age, course) and call it using keyword arguments.
def student(name,age,course):
    return name,age,course
print(student(name="anusha",age=21,course="Java"))
-----------------------------------------------------------------------------------------------------------------------------
7.QUESTION: Create employee(name, salary, department) and call it using keyword arguments in a different order.
def employee(name,salary,department):
    return name,salary,department
print(employee(name="gopi",salary=21,department="CSE"))
----------------------------------------------------------------------------------------------------------------------------------------
8.QUESTION: Create product(name, price, quantity) and call it using keyword arguments.
def product(name,price,quantity):
    return name,price,quantity
print(product(name="ice cream",price=21,quantity=10))
-------------------------------------------------------------------------------------------------------------------------
9.QUESTION: Create address(city, state, pincode) and call it using keyword arguments.
def address(city,state,pincode):
    return city,state,pincode
print(address(city="Nellore",state="Andhra Pradesh",pincode="524003"))
------------------------------------------------------------------------------------------------------------------------------------
10.QUESTION:  Create calculate(a, b, operation) and call it using keyword arguments.
def calculate(a,b,operation):
    return a,b,operation
print(calculate(a=10,b=20,operation="opertors"))
-----------------------------------------------------------------------------------------------------------------
11.QUESTION:  Create greet(name="Anu") that prints:
def greet(name="anu"):
   print("Hello",name)
greet()
-----------------------------------------------------------------------------------------------------------------------
12.QUESTION: Call the same function with another name.
def greet(name="karthik"):
   print("Hello",name)
greet()
------------------------------------------------------------------------------------------------------------
13.QUESTION:  Call it with only the name.
def student(name,course="python"):
    print(name,course) 
student("gopi")
------------------------------------------------------------------------------------------------------------------------
14.QUESTION:  employee(name, department="IT")
def employee(name,department="IT"):
    print(name,department) 
employee("anusha")
-----------------------------------------------------------------------------------------------------------------
15.QUESTION: Call the function in 3 different ways.
def employee(name,age=22,department="IT"):
    return (age,name,department)
print(employee("anu"))

def employee(name,age=22,department="IT"):
    return (age,name,department)
print(employee(age=22,name='anu',department='IT'))

def employee(name,age=22,department="IT"):
    return (age,name,department)
print(employee("gopi"))
