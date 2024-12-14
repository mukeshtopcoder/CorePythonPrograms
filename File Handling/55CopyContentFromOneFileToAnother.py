# 55. Write a program to copy the contents of one file to another.
file1 = open("temp.txt","r")
file2 = open("copy.txt","w")
data = file1.read()
file2.write(data)
print("Content Copied Successfully!")
file1.close()
file2.close()
