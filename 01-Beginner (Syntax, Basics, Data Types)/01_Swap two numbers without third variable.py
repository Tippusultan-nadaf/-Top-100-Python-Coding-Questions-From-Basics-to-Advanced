# Write a program to swap two numbers without using a third variable.

a = int(input("enter the first number: "))
b = int(input("enter the second number: "))

a=a+b
b=a-b
a=a-b
print(f"the swaped numbers are :{a} and {b}")