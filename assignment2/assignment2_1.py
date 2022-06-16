
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
