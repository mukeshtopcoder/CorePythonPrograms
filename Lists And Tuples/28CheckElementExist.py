# 28.	Write a Python program to check if an element exists in a list.
list1 = [ 32,5,78,6,4,32,43,65,78,67,34,23,45 ]
print("List : ",list1)
num = int( input("Enter A Number : ") )
if(num in list1):
    print("Item Exists!")
else:
    print("Item is not exist in List!")
