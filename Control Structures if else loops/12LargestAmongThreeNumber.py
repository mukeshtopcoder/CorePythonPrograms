# 12.  Write a program to find the largest among three numbers.
a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
c = int( input("Enter C Number : ") )
if( (a>b) and (a>c) ):
    print(a," is Greater!")
elif( (b>a) and (b>c) ):
    print(b," is Greater!")
else:
    print(c," is Greater!")
