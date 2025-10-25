# Find the largest of three numbers.

def Largest(num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    elif num2>num1 and num2>num3:
        return num2
    elif num3>num1 and num3>num2:
        return num3


n1=int(input("enter first number: "))
n2=int(input("enter second number: "))
n3=int(input("enter third number: "))
largest=Largest(n1,n2,n3)
print(largest)
