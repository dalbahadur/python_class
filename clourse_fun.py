""" # clourse function: it is used to store the value 
def increment(num):
    def factor(valu):
        return num+valu
    return factor
increase_by=increment(10)
print(increase_by(10))
print(increase_by(30)) """

def welcome(name):
    print("welcome {name}")
def bye_bye(name):
    print(f"Bye_bye {name}")
def greet(func):
    func("Ram")
greet(bye_bye)

# we can call the function with in function using the clourse method.
# the main motive is that if we want to pass the function parameter in the function name is 
# used the  method for example def ram() the we pass the ram functio as paraneter to next 
#function 

