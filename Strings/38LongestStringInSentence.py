# 38.	Write a program to find the longest word in a sentence.
str1 = "We Are Learning Programming in Python"
print("String : ",str1)
strList = str1.split(" ")
maxStr = ""
for i in strList:
    if(len(maxStr)<len(i)):
        maxStr=i
print("Longest String : ",maxStr)
