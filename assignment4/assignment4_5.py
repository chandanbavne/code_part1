#5) write a program which contains filter(),map()and reduce() in it. python application which contains one list of numbers.
#list contains the numbers which are accepted from user. filter should filter out all odd numbers. 
# are  map function will multiply each number by 2. reduce will return multiplication numbers from that numbers.
def odd(a):
    
        for i in range(2,a):
            return(a%i==1)
           
def mult(b):    
        return(b*2)


def maxmi(n,m):
    return(n*m)
    
a=[]
n=int(input("Enter a number of elements:"))
for i in range (n):
   a.append(int(input("Enter a element:")))
print(a)
print()
b=list(filter(odd,a))
print("odd number from  elements is:",b)
print()
c=list(map(mult,b))
print("list after map=",c)
print()

from functools import reduce
d=reduce(maxmi,c)
print("output of reduce:",d)