# 26.	Write a Python program to remove duplicates from a list.
list1 = [ 2,5,7,5,4,2,5,7,4,2,4,6,3,1,4,6,4 ]
print("List : ",list1)

# 1st Way
# for i in range(0,len(list1)):
#     j = i+1
#     while(j<len(list1)):
#         if(list1[i]==list1[j]):
#             list1.pop(j)
#         j=j+1

# 2nd Way
# list1 = list(set(list1))

# 3rd Way
uniqueList = [ ]
for i in list1:
    if i not in uniqueList:
        uniqueList.append(i)
print("Removed Duplicate Values List : ",uniqueList)
