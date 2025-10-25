# Find the GCD and LCM of two numbers. 

# GCD or HCF
def Gcd(a,b):
    while b!=0:
        a,b=b,a%b
        return a

a= int(input("enter the first number :"))
b=int(input("enter the second number :"))

print(f"the greatest common divisor of number {a} and {b} is {Gcd(a,b)}")

# LCM
# lcm x gcd = a x b

lcm=(a*b)/Gcd(a,b)
print(f"the least common multiple of number {a} and {b} is {lcm}")

