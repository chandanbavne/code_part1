
#5) write a recursive program which accept number from user and return its factorial:
#i/p=5,o/p=120

n=int(input("Enter a number:"))
fact=1
while n>0:
    fact=fact*n
    n-=1
print("Factorial of that number is:",fact)    

