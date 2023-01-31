""" # 5! for the 1 is base condition
def factorial(num):
    if num==1:
        return 1

    return num*factorial(num-1)
value=int(input("Enter the value if you want to factorial----"))
print(factorial(value)) """
# not return base** power.

def exponent(base,power):
    if power==0:
        return 1
    return base * exponent(base,power-1)
a=int(input("Enter the base"))
b=int(input("Enter the power")
    )
print(exponent(a,b))


    