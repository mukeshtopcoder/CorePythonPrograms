# 18.	Write a Python program to print the sum of all numbers in a given range.
start = int( input("Enter Start Range : ") )
end = int( input("Enter End Range : ") )
add = 0
for i in range(start,end+1):
    add=add+i
print("Sum of All Natural Number : ",add)
