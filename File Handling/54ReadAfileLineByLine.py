# 54. Write a Python program to read a file line by line.
file = open("temp.txt","r")
for line in file.readlines():
    print(line)
file.close()