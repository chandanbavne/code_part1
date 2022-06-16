#3)write a program which contains filter(),map() and reduce()in it. python application which contains one list of numbers.
#list contains the numbers which are accepted from user. filter should filter out of all such numbers which greate than
# or equal to 70 and less than or wqual to 90. map function will increase each number by 10
#Reduce will return product of all that numbers.

a=[]
n=int(input("enter number of element"))
for i in range(n):
    a.append(int(input("Enter element:")))
print(a)

print()
print("list after filter")
a=list(filter(lambda n:n>=70 and n<=90,a))
print(a)    

print()
b=list(map(lambda n:n+10,a))    
print("list after map=",b)

print()

from functools import reduce
c=(reduce(lambda n,m:n*m,a))
print("output of reduce=",c)
