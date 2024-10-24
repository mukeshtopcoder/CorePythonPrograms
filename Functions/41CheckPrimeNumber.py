# 41.	Write a Python function to check if a number is prime.
def checkPrime(num):
    for i in range(2,int(num/2)):
        if(num%i==0):
            return False
    return True
num = int( input("Enter A Number : ") )
if(checkPrime(num)):
    print("Number is Prime!")
else:
    print("Number is Nor Prime!")
