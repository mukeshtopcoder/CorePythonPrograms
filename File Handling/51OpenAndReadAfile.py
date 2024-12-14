# 51. Write a Python program to open a file and read its contents.
file = open("./temp.txt","r")
data = file.read()
print(data)
file.close()
