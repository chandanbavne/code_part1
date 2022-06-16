# write a program which accept N number from user and store it into list.
#return addition of all prime numbers from that list.main python file accept n numbers from user and pass each number to chkprime()
#function which is part of user defined module named as
#marvellous. name name of the function from main python file should be listprime()

def chkprime(a):
    add=0
    for i in a:
        if(i%2)==1:
            add+=i
    return add        
          

a=[]
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(int(input("Enter a element:")))
b=chkprime(a)    
print("addition of prime number is:",b) 