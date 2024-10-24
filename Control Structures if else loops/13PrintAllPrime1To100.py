# 13.	Write a Python program to print all prime numbers between 1 and 100.
for i in range(2,101):
    count=0
    for j in range(2,i):
        if(i%j==0):
            count=count+1
            break
    if(count==0):
        print(i)