
#2) write a program which accept one number and display pattern in that numbers times in rows and column

n=int(input("enter a number:"))
for i in range(1,n+1):
    for j in range(1,n+1):
        print("*",end=' ')
    print()    # for new line
print()
# by using while loop
n=int(input("enter a number:"))
i=0
while i<n:
    j=0
    while j<n:
        print("*", end=' ')
        j+=1
    print()
    i+=1
