# 29.	Write a program to find the intersection of two lists.
# HINT : common elements in both List
list1 = [ 2,4,6,4,7,3,2,4,4,7,3,2 ]
list2 = [ 2,5,7,9,6,3,6,8,6,4,3,7 ]
print("List1 : ",list1)
print("List2 : ",list2)
list3 = [  ]
for i in list1:
    for j in list2:
        if(i==j):
            list3.append(j)
            list2.remove(j)
            break
print("List3 : ",list3)
