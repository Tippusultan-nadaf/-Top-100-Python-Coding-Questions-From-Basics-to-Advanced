# Find common elements between two lists.

lst1=[25,58,"tippu",85.5,"sultan",48]
lst2=[25,"tippu",85.5,"nadaf",76]
lst3=[]

for i in range(len(lst1)):
    for j in range(len(lst2)):
        if lst1[i]==lst2[j]:
            lst3.append(lst1[i])
print(f"the elements in list 1 are: {lst1}")
print(f"the elements in list 2 are: {lst2}")
print(f"the list which are same in both lists are : {lst3}")
            