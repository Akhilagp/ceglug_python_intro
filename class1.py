#!/usr/bin/python
class Employee:#common base class
    empCount = 0
    
    def __init__(self, name, salary): # Initialization or constructor
        self.name = name
        self.salary = salary
        Employee.empCount += 1 #class variable
        
    def displayCount(self):#class method
        print "Total Employee ", Employee.empCount
        
    def displayEmployee(self):
        print "Name: ",self.name, "Salary: ", self.salary
        
emp1 = Employee("Krishna","2000")#instance object
emp2 = Employee("Dharma","4000")
emp1.displayEmployee()#accessing attributes
emp2.displayEmployee()
emp2.displayCount()
print Employee.empCount
    
