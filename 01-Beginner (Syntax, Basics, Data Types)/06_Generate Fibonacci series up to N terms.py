 # Generate Fibonacci series up to N terms

# creating a function for finding fibonacci number
def Fibonacci(num):
    if num ==0:
        return 0
    elif num==1:
        return 1
    else:
        return Fibonacci(num-1)+Fibonacci(num-2)
    


n=int(input("enter the number: "))
lst=[]

# creating a list carring all the fibonnaci numbers
for i in range(n):
    lst.append(Fibonacci(i))

print(lst)