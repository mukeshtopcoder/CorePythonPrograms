# 36.	Write a program to capitalize the first letter of each word in a string.
str1 = "we are learning python programming"
print("String : ",str1)
strList = str1.split(" ")
str2 = ""
for i in strList:
    str2=str2+i[0].upper()+i[1:]+" "
print("New String : ",str2)
