#4. Accept one number and check whether is is divisible by 5 or not. 
def divisible(A):
    if(A%5==0):
        return True
    else:   
        return False

n=int(input("Enter a number:"))
result=divisible(n)
print(result)
