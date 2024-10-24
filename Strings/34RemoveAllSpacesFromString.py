# 34.	Write a python program to remove all spaces from a string.
str1 = "We Are Learning Python"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i
print("Removed All Spaces : ",str2)
