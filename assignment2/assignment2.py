'''from math import *
a=[10,20,30]
print(sum(a))

# 1) create fopue function add(),sub(),mult() and div(). all function accepts two parameters as number
# and perform the operationb. 
def Add(a,b):
    c=a+b
    print("addition of two number is:",c)
print()

def Sub(a,b):
    d=b-a
    print("subtraction of numbers is:",d)
print()

def Mult(a,b):
    e=a*b
    print("Multiplication of two numbers is:",e)
print()

def Div(a,b):
    h=b/a
    print("Division of two numbers is:",h)
print()

def main():
    n=int(input("Enter a number:"))  
    m=int(input("eneter a second number:"))
    Add(n,m)
    Sub(n,m)
    Mult(n,m)
    Div(n,m)

if __name__=="__main__":
    main()

#2) write a program which accept one number and display pattern in that numbers times in rows and column

n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=' ')
    print()    # for new line
print()
# by using while loop
n=int(input("enter a number:"))
i=0
while i<n:
    j=0
    while j<n:
        print("*", end=' ')
        j+=1
    print()
    i+=1

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

# 4)write a p[rogram whcih accept one number from user and return addition of its factor
n=int(input("Enter a nummber:"))
i=1
sum=0
while(i<=n):
        if(n%i==0):
            sum=sum+i
        i+=1
print(sum)        

#write a p[rogram which accept one number and check whethre its is prime or not:
n=int(input("enter a number:"))
for i  in range(n):
    if(n%2==1):
        print(n,"it is prime number")
        break
else:
     print(n,"it is nopt prime number")
# 1to 15 prime numbers
n=int(input("enter a number:"))
m=int(input("enter a number:"))
for num in range(n,m+1):
    if num>1:
        for i  in range(2,num):
            if(num%i==0):
                break
        else:
            print(num,"it is prime number"
# write a program which accept one number and display bellow patter:
n=int(input("enter a number:"))
i=0
while i<n:
        star=i+1
        while star>0:
            print('*',end=" ")
            star=star-1
            
        i=i+1    
        print()

#pattern:
1
12
123
1234
12345'''
'''n=int(input("enter a number of rows:"))
for i in range(n):
    for j in range(i+1):
        print(j+1,end=" ")
    print()    

# 2)pattern:
12345
12345
12345
12345
12345
12345
12345

n=int(input("Enter number of rows:"))
for i in range(n):
    for j in range(n):
        print(j+1,end=" ")
    print()    

n=int(input("enter number of rows:"))
for i in range(n,0,-1):
        for j in range(0,i):
            print("*",end=" ")
        print()    

n=int(input("Enter a number:"))
sum=0
while(n>0):
           sum=sum+n%10 #n=25%10=remainder is 5 and 25//10=2 after decimal points are skips 
           n//=10
print(sum)
'''            