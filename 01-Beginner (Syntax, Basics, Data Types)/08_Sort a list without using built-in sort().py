# Sort a list without using built-in sort()

lst=input("enter the list of numbers: ").split()
lst=[int(x) for x in lst]
print(f"ur list of numbers are : {lst}")
for i in range(len(lst)):
    for j in range(0,len(lst)-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]

print(lst)
