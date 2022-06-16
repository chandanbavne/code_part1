#1)write a program whic contains one function named as Fun().
#that function should display"Hello from fun" on console.
'''
def fun():
    print("hello from fun")

def main():
    fun()

if __name__=="__main__":
    main()

#2)write a program which contain one function named as chkNUm() which accept one parameter as number 
#if number is even then it should display"even number"otherwise
#display "odd number".

def chkNum(n):
    if(n%2==0):
        print("Even number")
    else:
        print("odd number")


n=int(input("Enter a number:"))
chkNum(n)


#3) write a program which contains one function named as Add() which accepts two
# numbers from user and return addition of that two numbers.

def add(a,b):
    c=a+b
    return c


def main():
    n=int(input("Enter First number:"))
    m=int(input("Enter second number:"))
    x=add(n,m)
    print("Addition of two  numbers is:",x)

if __name__=="__main__":  # code starter in python
    main()


# 4) write a program which display 5 time Marvellous on console:
name='marvellous'
i=0
while i<5:
    print(name)
    i+=1

# 5) write a program which display 10 to 1 on screen.
for i in range(10,0,-1):
    print((i))
    
#or

i=10
while i>1:
        print(i,end='\n')
        i-=1

#6) write a program which accept number from user and check whetherthat number is positve or negative or zero

n=int(input("enter a number:"))
if(n>0):
    print("positive number")
elif(n<0):
    print("negative number")
else:
    print("zero")

# 7) write a program which contaian one function that accept one number from user and 
# returns true if number is divisible by 5 otherwise return false.
def fun(a):
    if(a%5==0):
        print("True")
    else:
        print("False")

n=int(input("enter a number:"))
fun(n)

# 8) write a program which accept number from user and print that number of"*"on screen.
n=int(input("enter a number:"))
i=0
while i<n:
    
    print('*',end=' ')
    i+=1

#9) write a program which display first 10 even numbers on screen:
i=2
while i<=20:
    print(i,end=' ')
    i+=2

# 10)write a program which accept name from user and display length of its name:
name=(input("Enter a name of person:"))
n=len(name)
print(n)
'''