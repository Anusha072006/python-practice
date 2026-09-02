#LAMBDA FUNCTION:
1.QUESTION:create the example for lambda  function using map()  
numbers=[1,2,3,4]
squares=list(map(lambda x:x**2,numbers))
print(squares)
---------------------------------------------------------------------------------------------------------------------------------
2.QUESTION: Create the example for lambda function using filter()
numbers=[1,2,3,4,8,7,5,9]
even=list(filter(lambda x:x%2==0,numbers))
print(even)
-------------------------------------------------------------------------------------------------------------------------------------
3.QUESTION: create the example for lambda function using sort()
numbers=[(2,10,),(1,20),(3,5)]
sort=sorted(numbers,key=lambda x:x[0])
print(sort)
------------------------------------------------------------------------------------------------------------------------------------------
4.QUESTION: Create a lambda function that returns the square of a number.
numbers=[5]
square=list(map(lambda x: x*5,numbers))
print(square)
------------------------------------------------------------------------------------------------------------------------------------------------
5.QUESTION: Create a lambda function that returns the cube of a number.
numbers=[3]
cube=list(map(lambda x:x**3,numbers))
print(cube)
--------------------------------------------------------------------------------------------------------------------------------------------------
6.QUESTION: Create a lambda function that adds two numbers.
add=lambda a,b:a+b
print(add(10,20))
-------------------------------------------------------------------------------------------------------------------------------------
7.QUESTION: Create a lambda function that returns the larger of two numbers.
largestnumber=lambda a,b:a if a>=b else b
print(largestnumber(10,20))
-----------------------------------------------------------------------------------------------------------------------------------------
8.QUESTION: Create a lambda function that returns "Even" if the number is even, otherwise "Odd".
numbers=[2,3,4,6,5,7,9]
check=lambda x:"even"if x%2==0 else"odd"
for num in numbers:
    print(check(num))
  ---------------------------------------------------------------------------------------------------------------------------------------
9.QUESTION: Create a lambda function that treturns "Positive" or "negative"
numbers=[2,3,4,6,7,8]
check=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
for  num in numbers:
    print(check(num))
  --------------------------------------------------------------------------------------------------------------------------------------------
10.QUESTION: Create a lambda function that returns conditions is above or 40  "pass"or "Fail"
numbers=[30,45,50]
check =lambda x:"pass" if x>=40 else "Fail" 
for num in numbers:
    print(check(num))
  -----------------------------------------------------------------------------------------------------------------------------------------------
11.QUESTION: Find the smallest of two numbers
numbers=[10,5]
smallestnumber=lambda  a,b:a if a<=b else b
print(smallestnumber(10,5))
----------------------------------------------------------------------------------------------------------------------------------------------------
12.QUESTION: Check voting eligibility
age=13
vote=lambda x:"eligible" if age>=18 else "not eligible"
print(vote(age))
