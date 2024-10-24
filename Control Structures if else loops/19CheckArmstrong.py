# 19.	Write a program to find whether a given number is Armstrong or not.
# if you have a number 153, 
# And you want to add the cube root of every digit like,
# Then it will again come the same number
# 1^3+5^3+3^3 == 153
# So, 153 is an Armstrong Number

num = int( input("Enter A Number : ") )
temp = num
total = 0
while(num>0):
    rem = num%10
    total = total+rem*rem*rem
    num = int(num/10)
if(temp==total):
    print("Number is Armstrong")
else:
    print("Number is Not Armstrong")
