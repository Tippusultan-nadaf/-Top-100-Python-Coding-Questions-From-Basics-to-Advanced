# Find the second largest element in a list.
lst=input("enter the numbers of list: ").split()
lst=[int(x) for x in lst]

print(f"your entered list is : {lst}")

for i in range(len(lst)):
    for j in range(0,len(lst)-1-i):
        if lst[j]>lst[j+1]:
            lst[j],lst[j+1]=lst[j+1],lst[j]
print(lst)
print(f"second largest number in the string is: {lst[len(lst)-2]}")