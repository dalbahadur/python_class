# exception handling
""" try:
    # block of code
except Exception:
    # block of code
except ValueError:
    # block of code
except TypeError:
    # block of code
else:
    # block of code
finally:
    # block of code
     """
try:
    a=int(input("Enter first number"))
    b=int(input("Enter second number"))
    
except ValueError:
    print("can not convert the value")
else:
    #c=a+b
    #print("the sum of the numbe is ",c)
    print(f"summ of {a} and {b} is {(a+b)}")
name=input("Enter the name")
print("The name is",name)
