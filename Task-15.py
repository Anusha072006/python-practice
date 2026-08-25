1.QUESTION: check whether a number is even or odd
x=int(input("enter the number:"))
if x %2==0:
    print("even")
else:
    print("odd")
-----------------------------------------------------------------------------------  ---------------------------------------------------------------------------------------------
2.QUESTION: Find the largest of three numbers
a=int(input("enter the number num1:"))
b=int(input("enter the number num2:"))
c=int(input("enter the number num3:"))
if a>=b and a>=c:
    print("largest:",a)
elif b>=a and b>=c:
    print("largest",b)
else:
    print("largest:",c)
---------------------------------------------------------------------------------------------------------------
3.QUESTION: Print all even numbers from 1 to 50
for i in range(1,51):
    if i%2==0:
        print(i)
---------------------------------------------------------------------------------------------------
4.QUSETION: print number from 1 to 20
for i in range(1,21):
    if i%2==0:
        print(i)
-------------------------------------------------------------------------------------------------------------
5.QUESTION :print the sum of number from 1 to 100
total=0
for num in range(1,101):
    total=total+num
print(total)
