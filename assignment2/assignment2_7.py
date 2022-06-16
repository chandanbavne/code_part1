# write a program which accept one number and display bellow patter:

#pattern:
#1
#12
#123
#1234
#12345




n=int(input("enter a number:"))
i=0
while i<n:
        star=i+1
        while star>0:
            print('*',end=" ")
            star=star-1
            
        i=i+1    
        print()

