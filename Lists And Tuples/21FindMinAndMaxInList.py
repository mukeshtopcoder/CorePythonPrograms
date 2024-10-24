# 21.	Write a program to find the maximum and minimum numbers in a list.
list1 = [ 3,45,67,8,67,43,23,4,56,78,98,56,43,23,21,23 ]
min = list1[0]
max = list1[0]
for i in list1:
    if(i<min):
        min=i
    if(i>max):
        max=i
print("List : ",list1)
print("Minium Value : ",min)
print("Maximum Value : ",max)
