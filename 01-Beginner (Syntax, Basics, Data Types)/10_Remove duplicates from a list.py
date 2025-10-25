# Remove duplicates from a list.
lst=input("enter the numbers in ur list : ").split()
# lst=[int(x) for x in lst]
lst=[int(x) for x in lst]

unique=[]

for i in lst:
    if i not in unique:
        unique.append(i)

print(unique)


        