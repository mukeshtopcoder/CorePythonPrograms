# 66. Write a Python program to update the value of a key in a dictionary.
dic = {'A':46,'B':89,'C':37,'D':26}
print("Your Dic : ",dic)
key = input("Enter Any Key To Find : ")
if(dic.get(key)!=None):
    value = input("Enter Value To Update : ")
    dic.update({key:value})
    print("Your Updated Dic : ",dic)
else:
    print("Key Not Found!")
