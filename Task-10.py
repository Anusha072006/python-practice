1.QUESTION: Accept an integer input from the console and store it in the variable N
Accept a string input from the console and store it in the variable S
Output the integer first and then string on the same line.
N=int(input())
s=input()
print(N,s)
---------------------------------------------------------------------------------------------------
2.QUESTION: Let us take the next small step and learn about test cases.
For a lot of problems in CodeChef, you will have to solve the task for multiple test cases.
Example: Consider 5 test cases or 5 inputs
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
print(A)
print(B)
print(C)
print(D)
print(E)
---------------------------------------------------------------------------------------------------------------------------------
3.QUESTION: What will we do if we expect 100 inputs or test cases?
What about 100,000 inputs or test cases?
t = int(input())
for i in range(t):     
    N = int(input())      
    print(N)
  ---------------------------------------------------------------------------------------------------------------------------------
4.QUESTION: Lets write a program in the IDE which performs the following The 1st line of input contains t - the count of testcases
Each testcase consists of the following 2 lines of input
The 1st line of the testcase contains 2 integers - accept them as variables A and B
The 2nd line of the testcase contains 1 string - accept it as a variable C
t = int(input())
for i in range(t):
A, B =map(int,input().split()) 
C = input()
print(A, B, C)
--------------------------------------------------------------------------------------------------------------------------------------
5.QUESTION: Replace the Custom inputs with Sample test case 2 and click Run to check the result.
You can click the Copy icon at the top-right of the sample testcases to copy easily.
Replace the Custom inputs with your own created inputs and click Run to check the result.
You can experiment a few more options.
Once done, click on Submit to test your code against the Private test files
Note - Do not forget that the  1st integer in the custom inputs has to be t - the number of test cases 
t = int(input())
for i in range(t):
    n = int(input())
    print(n+1)
  --------------------------------------------------------------------------------------------------------------------------------------
6.QUESTION: Accepts the count of test cases - t - in the 1st lineFirst line of each test case consists of a string S
You need to perform the following operation Create a variable X which contains the string 
S concatenated with the string S
Output X for each test case
t = int(input())
for i in range(t):
    s=input()
    x=s+s
    print(x)
  -----------------------------------------------------------------------------------------------------------------------------------------


