# 24.	Write a Python program to count the number of occurrences of an element in a list.
list1 = [2,4,6,3,2,3,5,5,4,3,2,4,5,3,3,3,2,4,3,2]
print("List : ",list1)
num = int( input("Enter Element To Find Occurence : ") )
count = 0
for i in list1:
    if(i==num):
        count=count+1
print("Occurences : ",count)
