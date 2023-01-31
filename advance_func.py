def calculator(operator):
    def addition(a,b):
        return a +b
    def difference(a,b):
        return a-b
    def product(a,b):
        return a*b
    if operator=="+":
        return addition
    elif operator=="-":
        return difference
    elif operator=="*":
        return product

value1=int(input("Enter first number"))
value2=int(input("enter second number"))
check=input("supply the sign for calculation")

a=calculator(check)

print(a(value1,value2))
