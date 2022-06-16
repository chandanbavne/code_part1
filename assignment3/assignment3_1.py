# 1) write  program which accept N numbers from user and store it into list. return addition
#of all elements from that list:
from math import *
a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(int(input("Enter a element:")))
sum=0
for i in a:
    if(i%2==0 or i%2==1):
        sum=sum+i
print(sum)    

