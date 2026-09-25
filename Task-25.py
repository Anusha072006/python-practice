#Lambda Functions

numbers=[1,2,3,4]
squares=list(map(lambda x:x**2,numbers))
print(squares)

numbers=[1,2,3,4,8,7,5,9]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

numbers=[(2,10,),(1,20),(3,5)]
sort=sorted(numbers,key=lambda x:x[0])
print(sort)


#Create a lambda function that returns the square of a number.
numbers=[5]
square=list(map(lambda x: x*5,numbers))
print(square)

# Create a lambda function that returns the cube of a number.
numbers=[3]
cube=list(map(lambda x:x**3,numbers))
print(cube)

# Create a lambda function that adds two numbers.
add=lambda a,b:a+b
print(add(10,20))

# Create a lambda function that returns the larger of two numbers.
largestnumber=lambda a,b:a if a>=b else b
print(largestnumber(10,20))

# Create a lambda function that returns "Even" if the number is even, otherwise "Odd".
numbers=[2,3,4,6,5,7,9]
check=lambda x:"even"if x%2==0 else"odd"
for num in numbers:
    print(check(num))

numbers=[2,3,4,6,7,8]
check=lambda x: "positive" if x>0 else "negative" if x<0 else "zero"
for  num in numbers:
    print(check(num))

numbers=[30,45,50]
check =lambda x:"pass" if x>=40 else "Fail" 
for num in numbers:
    print(check(num))

# Find the smallest of two numbers
numbers=[10,5]
smallestnumber=lambda  a,b:a if a<=b else b
print(smallestnumber(10,5))

# Check voting eligibility
age=13
vote=lambda x:"eligible" if age>=18 else "not eligible"
print(vote(age))

numbers=[1,2,3,4,5]
even=list(map(lambda x: x*x,numbers))
print(even)

# Multiply every number by 3.
numbers=[2,4,6,8,10]
even=list(map(lambda x: x*3,numbers))
print(even)

# Find the square of every number.
numbers=[3,5,7,9]
square=list(map(lambda x: x*x,numbers ))
print(square)

# Add 10 to every number.
numbers=[10,20,30,40,50]
even=list(map(lambda x:x%2==0,numbers))
print(even)

# Convert these names to uppercase.
names=["anu","ravi","priya","sita"]
uppercase=list(map(lambda x:x.upper(),names))
print(uppercase)
# Find the length of every name.
names = ["Anu", "Ravi", "Priya", "Samantha"]
lengths=list(map(lambda x:len(x),names))
print(lengths)
# Get only even numbers.
numbers=[11,12,15,18,19,21,24,27,30]
even=list(filter(lambda x:x%2==0,numbers))
print(even)

# Get only odd numbers
numbers=[10,13,16,19,22,25,28]
odd=list(filter(lambda x:x%2!=0,numbers)) 
print(odd)

# Get numbers greater than 25.
numbers=[10,30,15,40,25,50,20]
num=list(filter(lambda x:x>25,numbers))
print(num)

#Get numbers less than 50.
numbers = [20, 55, 35, 70, 45, 80]
num=list(filter(lambda x:x<50,numbers))
print(num)

# Get names whose length is greater than 5.
names = ["Anu", "Ravi", "Priya", "Arun", "Samantha", "Kiran"]
lengths=list(filter(lambda x:len(x)>5,names))
print(lengths) 

# Get even numbers and then square them.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even=filter(lambda x: x%2==0,numbers)
square=list(map(lambda x : x**2,even))
print(square)
