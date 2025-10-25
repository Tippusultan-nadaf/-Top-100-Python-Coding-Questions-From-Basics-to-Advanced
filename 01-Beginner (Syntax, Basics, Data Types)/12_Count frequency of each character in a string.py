# Count frequency of each character in a string.

str=input("enter your string : ")
str=str.replace(" ","")
# loop to find the number of letters repeated
for char in set(str):
    count=0
    for otherchar in str:
        if char==otherchar:
            count+=1
    print(f"the letter {char} came {count} number of times in given string")

            
