""" #decorate function calling

def decorate_function(func):
    def wrapper():
        print("Hello everyone")
        func()
        print("Bye everyone")

        return wrapper
@decorate_function
def welcome():
    print(f"welcome to everyone!")

welcome()
# the syntax is @<function Name>
# the main movite of the decorate function is to be used in the parent function calling all the detail
 """

def smart_division(func):
    def wrapper(a,b):
        if b==0:
            return "could not divide"
        else:
            return func(a,b)
@smart_division

def division(a,b):
    return a/b
    print(division(20,3))