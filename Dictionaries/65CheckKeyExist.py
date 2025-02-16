# 65. Write a program to check if a key exists in a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
key = input("Enter Any Key To Find : ")
if(dic.get(key)!=None):
    print("Found!")
else:
    print("Not Found!")
