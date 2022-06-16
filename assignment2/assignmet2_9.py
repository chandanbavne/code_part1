#write a program which accept number and addition of that number
#ex:i/p=125; o/p=8
n=int(input("Enter a number:"))
sum=0
while(n>0):
           sum=sum+n%10 #n=25%10=remainder is 5 and 25//10=2 after decimal points are skips 
           n//=10
print(sum)