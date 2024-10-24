# 37.	Write a Python program to reverse the words in a given sentence.
str1 = "We Are Leaning Python Programming"
print("String : ",str1)
strList = str1.split(" ")
revStr = ""
for i in strList:
    i=list(i)
    i.reverse()
    for j in i:
        revStr = revStr+j
    revStr=revStr+" "
print("Reversed String : ",revStr)
