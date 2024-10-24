# 11.	Write a Python program to check whether a number is positive, negative, or zero.
num = int( input("Enter A Number : ") )
if(num>0):
    print("Positive")
else:
    if(num<0):
        print("Negative")
    else:
        print("Zero")
