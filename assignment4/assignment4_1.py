#1) write a program which contains one lamda function which accept one parameter and return power of two

n=int(input("enter a number:"))
a=(lambda x:2**x)
power=a(n)
print("power of two is:",power)
