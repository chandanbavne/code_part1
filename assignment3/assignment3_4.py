#04)write a program which accept N numbers from user and store it into list. accept one another
#number from user and return freuency of that number from list.
a=[]
n=int(input("enter a Number of elements:"))
for i in range(n):
    a.append(int(input("Enter a element:")))
key=int(input("enter a element to find freqency:"))
count=0
for i in range(n):
        if(a[i])==key:
            count+=1
print("Frequency=",count)            
