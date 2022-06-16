#write a p[rogram which accept one number and check whethre its is prime or not:
n=int(input("enter a number:"))
for i  in range(n):
    if(n%2)==1:
        print(n,"it is prime number")
        break
else:
     print(n,"it is nopt prime number")
