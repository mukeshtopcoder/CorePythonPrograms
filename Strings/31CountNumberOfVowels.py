# 31.	Write a Python program to count the number of vowels in a string.
str1 = input("Enter A String/Sentence : ")
print("Your String : ",str1)
count = 0
for i in str1:
    if(i in "aeiouAEIOU"):
        count=count+1
print("Occurences of Vowel is : ",count)
