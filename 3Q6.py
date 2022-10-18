class Person:
    def __init__(self,name):
        self.name=name
    def setAge(self,age):
        if(age>=1 and age<=130):
            self.__age=age
        else:
            self.__age="None"

    def getAge(self):
        return self.__age

    def setWeight(self,weight):
        if(weight>=15 and weight<=150):
            self.__weight=weight
        else:
            self.__weight="None"

    def getWeight(self):
        return self.__weight
    

    def display(self):
        print("Name:",self.name)
        print("Age:",self.getAge())
        print("weight:",self.getWeight())
    
p=Person("Sayan")
p.setAge(23)
p.setWeight(65)
p.display()

p1=Person("Sunny")
p1.setAge(144)
p1.setWeight(165)
p1.display()
