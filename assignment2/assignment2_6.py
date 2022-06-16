# 1to 15 prime numbers
n=int(input("enter a number:"))
m=int(input("enter a number:"))
for num in range(n,m+1):
    if num>1:
        for i  in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num,"it is prime number"
