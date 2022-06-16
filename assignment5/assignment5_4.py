#4) write a recursive program which accept number from user and return summation of its digits
#i/p=879 and o/p=24
 

n=int(input("Enter a number:")) 
sum=0
while n>0:
    sum=sum+n%10
    n//=10
print("summation of that number is:",sum)    
