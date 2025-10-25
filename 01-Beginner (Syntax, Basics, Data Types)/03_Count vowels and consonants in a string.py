# Count vowels and consonants in a string
str=input(" enter the string: ")
str=str.replace(" ","")
vowel_count=0
cons_count=0
for char in str:
    if char =="a" or char =="e" or char =="i"or char =="o"or char =="u":
        vowel_count+=1
        
    else:
        cons_count+=1
        

print (f"the vowel count is {vowel_count} and the consonent count is {cons_count}")