# 60. Write a program to merge two text files into one.
file1 = open("57.txt","r")
file2 = open("temp.txt","r")
file3 = open("mergedFile.txt","a")
file3.write(file1.read()+"\n")
file3.write(file2.read())
print("File Merged Successfully!")
file1.close()
file2.close()
file3.close()