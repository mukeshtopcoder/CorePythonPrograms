# 59. Write a Python program to count the occurrences of a word in a text file.
myFile = open("temp.txt","r")
target = "file"
data = myFile.read()
data = data.lower()
target = target.lower()
count = data.split().count(target)
print(f"{target} is exist {count} times in This file!")
myFile.close()