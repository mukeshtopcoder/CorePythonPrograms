# 27.	Write a Python program to find the second largest number in a list.
list1 = [ 2,6,78,43,23,56,85,90,56,23,2,6,3 ]
print("List : ",list1)
if(len(list1)>1):
    list1.sort(reverse=True)
    print("Second Largest Value : ",list1[1])
else:
    print("List has less than 2 elements only!")