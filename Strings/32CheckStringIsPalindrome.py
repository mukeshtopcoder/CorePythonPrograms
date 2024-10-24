# 32.	Write a program to check if a string is a palindrome.
# HINT : An Sgring is Palindrome if any string is same if it is in its reverse form
# Example : MADAM , MADAM (Reverse) (Palindrome)
# Example : MOHAN , NAHOM (Reverse) (Not Palindrome)
str1 = input("Enter A String : ")
start = 0
end = len(str1)-1
flag = 1
while(start<end):
    if(str1[start]!=str1[end]):
        flag = 0
        break
    start=start+1
    end=end-1
if(flag==1):
    print("It's A Palindrome String!")
else:
    print("It's Not A Palindrome String!")
