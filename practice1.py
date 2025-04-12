class Student:
    #pass
    def setStuDetails(self,name,age,subject,education,marks,grade):
        self.name = name
        self.age = age
        self.subject = subject
        self.education = education
        self.marks = marks
        self.grade = grade
    def getStuDetais(self):
        print(f"{self.name}:{self.age}:{self.subject}:{self.education}:{self.marks}:{self.grade}")
ab=Student()
ab.setStuDetails("mona",23,"science","matric",80,"A grade")
ab.getStuDetais()