1.QUESTION: First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of a single line of input, two integers X and Y - the prize for top 10 rankers and the prize for ranks 11 to 100 respectively.
t = int(input())
for i in range(t):
    X, Y = map(int, input().split())
    prize_top10 = 10 * X           
    prize_11to100 = 90 * Y         
    print(prize_top10 + prize_11to100)
  -----------------------------------------------------------------------------------------------------------------------------------------------
2.QUESTION: Write a program that does the following
Accepts the number of inputs / test cases as 't'
The only line of each test case contains 2 integers - declare them as variables a and b
t = int(input())
for i in range(t):
    a, b = map(int,input().split())     
    diff =a-b
    division = a//b
    
    print(diff, division)
  -------------------------------------------------------------------------------------------------------------------------------------------------
3.QUESTION: In this problem you need to write a program which does the following
Accepts the number of inputs / test cases as 't'
Each line of test case contains 2 integers - declare them as variables A and B
t = int(input())
for i in range(t): 
    a, b = map(int, input().split())
    floatDivison = a/b
    integerDivison = a// b
    
    print(floatDivison, integerDivison)
  ----------------------------------------------------------------------------------------------------------------------------------------------------
4.QUESTION: The first line contains a single integer T — the number of test cases. Then the test cases follow.
The first and only line of each test case contains an integer X — the total number of sets of squats that you did.
t = int(input())
for i in range(t):
    X = int(input())
    print(X * 15)
  ------------------------------------------------------------------------------------------------------------------------------------------------------
5.QUESTION: First line will contain T, number of test cases. Then the test cases follow.Each test case contains of a single line of input, two integers X and 
N, the total points for the problem and the number of test cases which pass.
t = int(input())
for i in range(t):
    X, N = map(int, input().split())
    points_per_testcase = X//10
    score = points_per_testcase*N
    print(score)
    
