class Student:
    studCount = 0#variable
    
    def __init__(self,rollnumber,name):
        self.rollnumber = rollnumber
        self.name = name
        Student.studCount += 1
        
    def totalCount(self):
        print "Total number of students ", Student.studCount
    
    def student(self):
        print "Roll number ", self.rollnumber, "Name: ", self.name
        
    
stud1 = Student(20074141,"Ram")
stud1.student()
stud1.totalCount()
stud2 = Student(20083245,"Krishna")
stud3 = Student(1000,"Akhila")

#stud1. student()
#stud1.totalCount()
stud2.student()
stud3.student()
stud3.totalCount()
print Student.studCount
