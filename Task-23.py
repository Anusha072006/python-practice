# SORTED  LAMBDA FUNCTION
#  sorted
numbers=[(2,10,),(1,20),(3,5)]
sort=sorted(numbers,key=lambda x:x[1])
print(sort)
--------------------------------------------------------------------------------------------------------------------------------------
numbers=[(2,3),(1,4),(5,6)]
sort=sorted(numbers,key=lambda x:x[0])
print(sort)
-----------------------------------------------------------------------------------------------------------------------------------------
# Sort the numbers in ascending order.
numbers=[45,12,78,23,9,56]
sort=sorted(numbers)
print(sort)
---------------------------------------------------------------------------------------------------------------------------------------
# Sort the numbers in descending order.
numbers=[34,67,12,89,25,43]
sort=sorted(numbers,reverse=True)
print(sort)
-----------------------------------------------------------------------------------------------------------------------------------------
#  Descending + Lambda
name=["anu","gopi","suma","karthik"]
sort=sorted(name,key=lambda x:len(x),reverse=True)
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------------
#Sorting Strings
name=["anu","gopi","suma","karthik"]
print(sorted(name))
------------------------------------------------------------------------------------------------------------------------------------------------
# sorted() with key
name=["Anu", "Ravi", "Priya", "Samantha"]
result=sorted(name,key=len)
print(result)
--------------------------------------------------------------------------------------------------------------------------------------------------
# Sort these names alphabetically.
names=["Ravi","Anu","Kiran","Sita","priya"]
sort=sorted(names,key=lambda x: x.lower())
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------
# Sort these names in reverse alphabetical order.
names=["Arun","Samantha","Ravi","Anu","Priya"]
sort=sorted(names,reverse=True)
print(sort)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort the names based on their length.
names=["Raj","Anusha","Ram","Priyanka","Sita"]
sort=sorted(names,key=lambda x:len(x))
print(sort)
--------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort the names from longest to shortest.
names=["Ram","Anusha","Ravi","Samantha","Priya"]
sort=sorted(names,key=lambda x: len(x),reverse=True)
print(sort)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort the numbers based on their last digit.
numbers=[24,17,32,45,61,28]
sort=sorted(numbers,key=lambda x:x%10)
print(sort)
--------------------------------------------------------------------------------------------------------------------------------------------------
# Sort the numbers based on their absolute value.
numbers=[-15,5,-2,20,-8,10]
sort=sorted(numbers,key=lambda x: abs(x))
print(sort)
-------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort employees based on salary from lowest to highest.
employees = [
    ("Anu", 45000),
    ("Ravi", 55000),
    ("Sita", 40000),
    ("Arun", 60000)
]
sort=sorted(employees,key=lambda x: x[1])
print(sort)
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort employees based on salary from highest to lowest.

employees = [
    ("Anu", 45000),
    ("Ravi", 55000),
    ("Sita", 40000),
    ("Arun", 60000)
]
sort=sorted(employees,key=lambda x: x[1],reverse=True)
print(sort)
---------------------------------------------------------------------------------------------------------------------------------------------------
# Sort employees based on name length.
employees = [
    ("Anu", 45000),
    ("Ravi", 55000),
    ("Priyanka", 40000),
    ("Sita", 60000)
]
sort=sorted(employees,key=lambda x:len(x[0]))
print(sort)
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort students based on their marks.
students = [
    ("Anu", 85),
    ("Ravi", 72),
    ("Kiran", 90),
    ("Sita", 65)
]
sort=sorted(students,key=lambda x:x[1])
print(sort)
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort students based on marks from highest to lowest.
students = [
    ("Anu", 85),
    ("Ravi", 72),
    ("Kiran", 90),
    ("Sita", 65)
]
sort=sorted(students,key=lambda x: x[1],reverse=True)
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort products based on price.
products = [
    ("Laptop", 50000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]
sort=sorted(products,key=lambda x:x[1])
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort products based on name length.
products = [
    ("Laptop", 50000),
    ("Mouse", 800),
    ("Keyboard", 1500),
    ("Monitor", 12000)
]
sort=sorted(products,key= lambda x:len(x[0]))
print(sort)
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort tuples based on their second value.
numbers=[(2,8),(5,3),(1,9),(4,2)]
sort=sorted(numbers,key=lambda x: x[1])
print(sort)
-------------------------------------------------------------------------------------------------------------------------------------------------
# Sort names based on length from longest to shortest.
numbers=[(2,8),(5,3),(1,9),(4,2)]
sort=sorted(numbers,key=lambda x: len(x),reverse=True)
print(sort)
---------------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort numbers based on their last digit.
numbers=[(2,8),(5,3),(1,9),(4,2)]
sort=sorted(numbers,key=lambda x:x[1])
print(sort)
-----------------------------------------------------------------------------------------------------------------------------------------------------------
# Sort employees based on department name.
employees = [
    ("Anu", "IT"),
    ("Ravi", "HR"),
    ("Sita", "Finance"),
    ("Kiran", "IT")
]

sort=sorted(employees,key=lambda x: x[1])
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------------
# Sort these words based on their length, longest first.
words = ["cat", "elephant", "dog", "tiger", "butterfly"]
sort=sorted(words,key=lambda x: len(x),reverse=True)
print(sort)
----------------------------------------------------------------------------------------------------------------------------------------
# Sort employees based on salary from lowest to highest.
employees = [
    ("Anu", 45000),
    ("Ravi", 55000),
    ("Sita", 40000),
    ("Arun", 60000)
]
sort=sorted(employees,key=len)
print(sort)
