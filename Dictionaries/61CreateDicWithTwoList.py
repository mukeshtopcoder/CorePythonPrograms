#61. Write a Python program to create a dictionary from two lists.
list1 = ['A','B','C','D','E','F']
list2 = [23,56,86,52,45,48]
dic = dict()
for i in range(0,len(list1)):
    dic.update({list1[i]:list2[i]})
print(dic)
