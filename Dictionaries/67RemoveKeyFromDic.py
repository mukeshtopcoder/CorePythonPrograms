# 67. Write a Python program to remove a key from a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
print("Your Dic : ",dic)
key = input("Enter Any Key To Delete : ")
if(dic.get(key)!=None):
    del dic[key]
    print("Your Updated Dic : ",dic)
else:
    print("Key Not Found!")
