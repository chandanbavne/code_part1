#3) write a program which accept one number from user and return its factorial
from math import *
n=int(input("enter a number:"))
print(factorial(n))    
    
 # or

n=int(input("enter a number:"))
fact=1
while(n>0):
    fact=fact*n
    n-=1
print("factorial of n is:",fact)
