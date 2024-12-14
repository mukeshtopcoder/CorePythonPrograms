# 52. Write a program to count the number of lines in a text file.
file = open("temp.txt","r")
data = file.readlines()
print("Total Lines in This Text File : ",len(data))
file.close()
