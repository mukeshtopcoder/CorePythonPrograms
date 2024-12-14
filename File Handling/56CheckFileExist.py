import os
file = "temp.txt"
if(os.path.exists(file)):
    print("File Exist")
else:
    print("File Doesn't Exist")
