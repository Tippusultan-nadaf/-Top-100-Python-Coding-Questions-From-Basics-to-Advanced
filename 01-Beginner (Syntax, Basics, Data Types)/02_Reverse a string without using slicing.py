# Reverse a string without using slicing

Str = input("enter the string : ")
reversed_str = ""
for char in Str:
    reversed_str=char + reversed_str

print(reversed_str)