#2) write a program which accept N numbers from user and store it into list.
#return maxmimum numbers from that list.
#from math import *
a=[]    
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(int(input("Enter a element:")))
print(max(a))
