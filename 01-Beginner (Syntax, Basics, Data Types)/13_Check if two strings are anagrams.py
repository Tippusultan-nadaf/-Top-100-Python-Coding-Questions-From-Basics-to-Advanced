# Check if two strings are anagrams.

# function to count the characters
def countchar(str1,str2):
    str1=str1.replace(" ","")
    characters1={}
    for char in set(str1):
        count=0
        for otherchar in str1:
            if char==otherchar:
                count+=1
        characters1[char]=count

    str2=str2.replace(" ","")
    characters2={}
    for char in set(str2):
        count=0
        for otherchar in str2:
            if char==otherchar:
                count+=1
        characters2[char]=count
    

    if characters1==characters2:
        return True
    
    



string1=input("enter first string: ")
string2=input("enter seecond string: ")

anagram=countchar(string1,string2)
print(anagram)

