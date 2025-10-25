#Find factorial of a number (loop + recursion)

def Factorial(n):
    if n==1 or n==0:
         return 1
    factorial=n*Factorial(n-1)
    return factorial


num=int(input("enter the number: "))
fac=Factorial(num)
print(fac)

