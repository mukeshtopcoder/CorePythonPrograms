# 35.	Write a Python program to check if two strings are anagrams.
# HINT : If all the characters are same in both string even occurency.
# so, pair of this strings are Anagram
str1 = "LISTEN"
str2 = "SILENT"
list1 = list(str1)
list2 = list(str2)
if(len(list1)==len(list2)):
    count = 0
    for i in list1:
        if(i in list2):
            count=count+1
            list2.remove(i)
    if(count==len(list1)):
        print("Strings Are Anagram!")
    else:
        print("Strings Are Not Anagram!")
else:
    print("Strings Are Not Anagram!")
