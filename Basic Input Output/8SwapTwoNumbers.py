# rite a Python program to swap two variables without using a temporary variable.
a = int( input("Enter A Number : ") )
b = int( input("Enter B Number : ") )
a = a+b
b = a-b
a = a-b
print("A = ",a)
print("B = ",b)
