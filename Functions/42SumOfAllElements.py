# 42.	Write a Python function to calculate the sum of all elements in a list.
def sumOfList(list1):
    total = 0
    for i in list1:
        total=total+i
    return total
list1 = [ 23,4,67,34,3,3]
print("List : ",list1)
print("Sum of All Elements : ",sumOfList(list1))
