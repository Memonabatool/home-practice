# oops metod in python-------------
# inheritance------
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
        
#class Animal:
       #pass
    #def __init__ (self,name):
         #self.name = name
    #def Sound(self):
         #print(f"hello{self.name} your sound is nothing")
#class Cat(Animal):
    #def __init__ (self,name):
         #self.name = name
    #def Sound(self):
         #print(f"hello{self.name} your sound is meauo")
#class Dog(Animal):
    #def __init__(self,name):
         #self.name = name
    #def Sound(self):
         #print(f"{self.name} your sound is whaao")
#ab =Cat("cat")
#ac =Dog("dog")
#ad =Animal("animal")
#ab.Sound()
#ac.Sound()
#ad.Sound()

#multiple inheritance-------------
  
#class Father:
    #def ft(self):
        #print("father classes")
#class Mother:
    #def mt(self):
        #print("mother classes")
#class Child(Father,Mother):
         #pass
#ab = Child()
#ab.ft()
#ab.mt()

#Grand parent child---
#class Father:
    #def ft (self):
        #print("father classes")
#class Child(Father):
    #pass
#ab =Child()
#ab.ft()
#class Mother:
    #def mt(self):
        #print("mother classes")
#class Child(Mother):
    #pass
#ab = Child()
#ab.mt()
# Multi level inheritance-----------
#class Grandpa:
    #def gp(self):
        #print("grandpa class")
#class Parent(Grandpa):
    #def prnt(self):
        #print("parent class")
#class Child(Parent):
    #pass
#ab = Child()
#ab.gp()
#class GrandChild:
    #def cld(self):
        #print("grand child")
#class GrandChild(GrandChild):
    #pass
#ab = GrandChild()
#ab.cld()

#class Parent:
    #def prnt(self):
        #print("hello world this is parent class")
#class Child1(Parent):
    #pass
#class Child2(Parent):
    #pass
#ab = Child1()
#ab.prnt()
#ab = Child2()
#ab.prnt()

# use of super method-----
class Parent:
    def __init__ (self,name,age):
     self.name = name
     self.age = age
    def smt(self):
        print(f"{self.name}:{self.age}")
class Child(Parent):
       def __init__(self,name,age):
        super().__init__(name,age)
ab=Child("ali",23)
ab.smt()
class Child(Parent):
    def __init__(self,name,age,education):
        self.education = education
        super().__init__(name,age)
    def mt(self):
        print(f"{self.education}")
ab = Child("amna",23,12)
ab.smt()
ab.mt()