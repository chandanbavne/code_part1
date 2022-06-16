# 7) write a program which contaian one function that accept one number from user and 
# returns true if number is divisible by 5 otherwise return false.
def fun(a):
    if(a%5==0):
        print("True")
    else:
        print("False")

n=int(input("enter a number:"))
fun(n)
