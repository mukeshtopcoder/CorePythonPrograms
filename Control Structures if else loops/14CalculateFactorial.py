# 14.	Write a Python program to calculate the factorial of a number.
num = int( input("Enter A Number : ") )
fact = 1
for i in range(1,num+1):
    fact=fact*i
print("Factorial : ",fact)