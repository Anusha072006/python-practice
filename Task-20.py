# FUNCTION: *args and **args
1.QUESTION: Create add(*args) that returns the sum of all numbers.
def add(*args):
    total = 0
for num in args:
        total += num

return total
print(add(10, 20, 30, 40))
----------------------------------------------------------------------------------------------------------------------------
2.QUESTION: Create multiply(*args) that returns the multiplication of all numbers.
def mul(*args):
    total=0
    for num in args:
        total*=num
    return total
print(mul(10,20,30))
-----------------------------------------------------------------------------------------------------------------------------------
3.QUESTION:  Create largest(*args) that returns the largest number.
def largest(*args):
    total=0
    for num in args:
        total=num
    return total
print(largest(3,4,56))
--------------------------------------------------------------------------------------------------------------------------------------------------
4.QUESTION: Create smallest(*args) that returns the smallest number.
def smallest(*args):
    smallest_num=args[0]
    for num in args:
        if num in args:
            smallest_num=num
        return smallest_num
print(smallest(2,4,6,7))
---------------------------------------------------------------------------------------------------------------------------------------------------
5.QUESTION: Create count_even(*args) that counts how many numbers are even.
def count_even(*args):
    count=0
    for num in args:
        if num%2==0:
            count+=1
    return count
print(count_even(2,3,4,5,6))
