# 15.	Write a Python program to print the Fibonacci sequence up to n terms.
a = 0 
b = 1
n = int( input("Enter Range : ") )
for i in range(n):
    c = a+b
    print(c,end=" ")
    a = b
    b = c
