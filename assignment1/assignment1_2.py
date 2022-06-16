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
