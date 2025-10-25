import re
str=input("enter the string: ")
# reducing the space between all the words and converting them into lower case
str=str.replace(" ","").lower()

# removing all the special characters if any
clean_str= re.sub(r'[^a-zA-Z]+',"",str)

rev_str=""
# creating a reverse string
for char in clean_str:
    rev_str= char+ rev_str

# comparing reverse and original string
if rev_str==clean_str:
    print("the string is palindrome")
else:
    print("the string is not a palindrome")