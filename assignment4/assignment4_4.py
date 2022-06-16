#4) write a program which contains filter(),map()and reduce() in it. python application which contains one list of numbers.
#list contains the numbers which are accepted from user. filter shoulder filter out all such numbers which 
# are even. map function will calcultae its square. reduce will return addition of all that numbers.
def even(a):
    if(a%2==0):
        return True

def square(a): 
    return(a**2)
def sum(a,b):
    return(a+b)

a=[]
n=int(input("Enter a number of element:"))
for i in range (n):
    a.append(int(input("enter a element:")))
print(a)
print()
r1=list(filter(even,a))    
print("list after filter=",r1)    
print()
r2=list(map(square,r1))
print("square of list is:",r2)
print()
from functools import reduce
r3=(reduce(sum,r2))
print("output of list is:",r3)
