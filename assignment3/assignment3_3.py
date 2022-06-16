#3) write a program which accept N numbers from user and store it into list.
#return minimum numbers from that list.
a=[]    
n=int(input("Enter number of elements:"))
for i in range(n):
    a.append(int(input("Enter a element:")))
print(min(a))
