# 33.	Write a Python program to find the frequency of characters in a string.
str1 = "aman is my best friend forever"
print("String : ",str1)
tempList = [ ]
for i in list(str1):
    if(i != " "):
        if i not in tempList:
            print("Occurency of ",i," is : ",str1.count(i))
            tempList.append(i)
