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
