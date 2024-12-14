# 57. Write a program to write a list of numbers to a text file.
file = open("57.txt","w")
st = ""
for a in range(1,101):
    st=st+str(a)+"\n"
file.write(st)
print("File Written Succesfully!")
file.close()