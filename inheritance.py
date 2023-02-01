""" # inheritance: to inherit any behaviour from parent to child .
#child class " is A " parent class relation
# Dog "is a " person this is incorrect statement due to behaviour of both activities.
# inheritace is used to similar activites of behaviour 
class Person:
    def __init__(self,name,address) -> None:
        self.name=name
        self.address=address
    def walk(self):
        print(f"{self.name} is walking")
    
class Tearcher(Person):
    def __init__(self, name, address,designation) -> None:
        super().__init__(name, address)
        self.designation=designation
        print(f"{self.designation} is printing")
    def teach(self):
        print(f"{self.name} is taching")

t1=Tearcher("prem","kathmandu","manager")
print(t1.teach())
print(t1.walk())
t2=Tearcher("hemanta","kathmandu","mathteacher")

t2.walk()
t2.teach()

class Student(Person):
    def __init__(self, name, address,roll_number) -> None:
        super().__init__(name, address)
        self.roll=roll_number
    def walk(self):
        print(f"{self.name} is running")
t=Tearcher("ram","ktm","lecture")
t.walk()
t.teach()
s=Student("prem","pokhara","professor")
s.walk()

 """

 class User:
    def __init__(self,username,password) -> None:
      self.username=username
      self.password=password
    
class Person(User):
    def __init__(self, username, password,name,address) -> None:
       super().__init__(username, password)
       self.name=name
       self.address=address
    def profile(self):
        print(f"{self.username}")
        print(f"{self.password}")
        print(f"{self.name}")
        print(f"{self.address}")

class Student(Person):
    def __init__(self, username, password, name, address,rollno) -> None:
       super().__init__(username, password, name, address)
       self.roll_number=rollno
    def profile(self):
        super().profile()
        print(f"{self.roll_number} this is roll number")
    
class Teacher(Person):
    def __init__(self, username, password, name, address,designation) -> None:
       super().__init__(username, password, name, address)
       self.designation=designation
    def profile(self):
        super().profile()
        print(f"{self.designation} is the designation")


t=Teacher("prem@gmail.com","1254","prem","ktm","professor")
t.profile()



class ProdcutError(Exception):
    pass

class Product:
    def __init__(self,name,price) -> None:
        
        self.name=name
        self.__price=price
    @property
    def Price(self):
        return self.__price
    @Price.setter
    def Price(self,price):
        if price<=0:
            raise ProcessLookupError("price cannot be less than zero")
            self.__price=price
tshirt=Product("Tshirt",500)
try:
    tshirt.Price=100
    print(f"without exception{tshirt.Price}")
except ProdcutError as msg:
    print(msg)
    print(f"after exception:{tshirt.Price}")
    



class Country:
    def __init__(self,people,land) -> None:
        self.people=people
        self.land=land
        
        