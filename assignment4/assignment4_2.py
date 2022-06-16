#2)write a program which contains one lamda function which accepts two parameters and return
#its multiplication
n=int(input("enter a first number:"))
m=int(input("enter a second number:"))

mult=(lambda x,y:x*y)
product=mult(n,m)
print("Multiplication of two number is:",product)
