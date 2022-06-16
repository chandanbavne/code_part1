#1) write a program of divide two numbers
def divide(A,B):
    if(A>B): 
        return(A/B)

n=int(input("Enter a first number:"))
m=int(input("Enter a second number:"))
result=divide(n,m)
print("Division of two number is:",result)
