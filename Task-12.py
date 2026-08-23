1.QUESTION: First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line consisting of single integer X.
t = int(input())
for i in range(t):
    X = int(input())
    total_distance=2*X*5
    print(total_distance)
  ------------------------------------------------------------------------------------------------------------------------------------
2.QUESTION: First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    prize_top10 = 10 * X           
    prize_11to100 = 90 * Y         
    print(prize_top10 + prize_11to100) 
---------------------------------------------------------------------------------------------------------------------------------------------
3.QUESTION: Write a program that does the following Accepts the number of inputs / test cases as 't'The only line of each test case contains 2 integers - declare them as variables a and b
t = int(input())
for i in range(t):
    a, b = map(int,input().split())     
    diff =a-b
    division = a//b
    
    print(diff, division)
-------------------------------------------------------------------------------------------------------------------------------------    -----------------------
4.QUESTION: Find the area of a circle given its radius.
radius=float(input("enter the radius:"))
area=math.pi* radius**2
print(area)
---------------------------------------------------------------------------------------------

