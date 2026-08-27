1.QUESTION: Create a list of 10 numbers and print the list. 
number=[1,2,5,3,4,7,6,8,9,76]
print(number)
-----------------------------------------------------------------------------------------------
2.QUESTION: Find the largest number in a list.
number=[1,2,5,3,4,7,6,8,9,76]
largest=number[0]
for num in number:
    if num > largest:
      largest=num
print("largest number:",largest)
--------------------------------------------------------------------------------------------------
3.QUESTION: Find the smallest number in a list.
number=[1,2,3,5,6,78,89,90]
smallest=number[0]
for num in number:
    if  num<smallest:
        smallest=num
print("smallest number:",smallest)
------------------------------------------------------------------------------------------------------------
4.QUESTION: Find the sum of all numbers in a list.
list=[23,45,67,89,2,1,4,5]
total=0
for list in number:
    total=total+num
    print(total)
---------------------------------------------------------------------------------------------------
5.QUESTION: Count how many even numbers are in a list.
numbers=[2,4,6,7,8,1,5,9]
count=0
for num in numbers:
    if num % 2==0:
        count+=1
print(count)
------------------------------------------------------------------------------------------------------
6.QUESTION: Count how many odd numbers are in a list.
numbers=[2,3,5,7,8]
count=0
for num in numbers:
    if num%2!=0:
        count+=1
print(count)
---------------------------------------------------------------------------------------------------------------
7.QUESTION: Remove duplicate values from a list.
numbers=[1,2,2,3,1,4]
unique=[]
for num in numbers:
    if num not in unique:
        unique.append(num)
print('unique values:',unique)
-------------------------------------------------------------------------------------------------------
8.QUESTION:  Reverse a list without using reverse().
numbers=[2,3,4,5,6,7,8]
reversed_list=[]
for num in numbers[::-1]:
      reversed_list.append(num)
print('reversed list',reversed_list)
----------------------------------------------------------------------------------------------------------------

