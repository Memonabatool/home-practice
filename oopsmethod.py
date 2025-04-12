# oops metod in python-------------
#class Student:
    #pass
    #def setStuDetails(self,name,age,subject,education,marks,grade):
        #self.name = name
        #self.age = age
        #self.subject = subject
        #self.education = education
        #self.marks = marks
        #self.grade = grade
    #def getStuDetais(self):
        #print(f"{self.name}:{self.age}:{self.subject}:{self.education}:{self.marks}:{self.grade}")
#ab=Student()
#ab.setStuDetails("mona",23,"science","matric",80,"A grade")
#ab.getStuDetais() 


# constructed method---------------
#class Student:
    #pass
        #def __init__ (self,name,age,subject,education,marks,grade):
         #self.name = name
         #self.age = age
         #self.subject = subject
         #self.education = education
         #self.marks = marks
         #self.grade = grade
        #def  getStu(self):
             #print(f"{self.name}:{self.age}:{self.subject}:{self.education}:{self.marks}:{self.grade}")
#ab = Student("haider",23,"english",9,70,"B Grade")
#ab.getStu()

# polymarphizam----------
#class Car:
    
        #def __init__ (self,name,model):
            #self.name = name
            #self.model = model
        #def fun(self):
            #print(f"{self.name}:{self.model}")
#class Bus:
        #def __init__ (self,name):
            #self.name = name
        #def fun(self):
            #print(f"{self.name}")
#ab= Car("kia",2022)
#ac=Bus("daewo")
#ab.fun()
#ac.fun()
        
class Animal:
       #pass
    def __init__ (self,name):
         self.name = name
    def Sound(self):
         print(f"hello{self.name} your sound is nothing")
class Cat(Animal):
    def __init__ (self,name):
         self.name = name
    def Sound(self):
         print(f"hello{self.name} your sound is meauo")
class Dog(Animal):
    def __init__(self,name):
         self.name = name
    def Sound(self):
         print(f"{self.name} your sound is whaao")
ab =Cat("cat")
ac =Dog("dog")
ad =Animal("animal")
ab.Sound()
ac.Sound()
ad.Sound()