# Object oreinted programming
# Class and Object: 
# Encapsulation:
# inheritance:
# polymorphism:
# Abstraction:

class Projector:
    def __init__(self,color,year,model):
        self.color=color
        self.year=year
        self.model=model

    def visualise(self):
        print(f"the color  {self.color} is visulization")
    def lightining(self):
        print("lightining")
    def description(self):
        print(f"The color {self.color} is visualizing")
        print(f"the year {self.year} is visualizing")
        print(f"the model {self.model} is visualizing")
    def __str__(self) -> str:# it returns the string of object 
        return self.color
        
    def __repr__(self) -> str:# it return the object
        return self.model

object=Projector("white",2020,"NEC")
""" print(object.color)
print(object.model)
print(object.year)
print(object.visualise())
print(object.lightining()) """

p=Projector("red",2023,"ACER")
p2=Projector("yellow",2024,"sony")
#p.visualise()
#p2.description()
print(p.__dict__) # it displays trhe form of directory 

projectors=[]
for i in range(3):
    color=input("Enter the color")
    year=input("Enter the year")
    model=input("Enter the model")
p3=Projector(color,year,model)
projectors.append(p3)
print(list(projectors)) 




