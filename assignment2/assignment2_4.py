# 4)write a p[rogram whcih accept one number from user and return addition of its factor
n=int(input("Enter a nummber:"))
i=1
sum=0
while(i<=n):
        if(n%i==0):
            sum=sum+i
        i+=1
print(sum)        

