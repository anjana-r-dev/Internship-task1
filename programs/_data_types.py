""" Built-in data types/predefined data types
Demonstrate using simple student details example"""
#parameters name=Manjula,age=20,cgpa=9.5,marks=80,85,90

#------------
# str(String)
#-------------
student_name="Manjula" #stores text inside quotes

#------------
#int(Integer)
#------------
student_age=20 # stores whole numbers

#----------------------
#float(Decimal numbers)
#----------------------
student_cgpa=9.5

#-------------
#bool(Boolean)
#-------------
is_student=True #Boolean value is either True or False

#List(list)
marks=[80,85,90]
# stores multiple value in same variable and it can be changed

#------
#Tuple
#------
coordinates = (10, 20)
# stored data can not be changed

#-----
#set
#-----
roll_numbers={1,2,3}
#stores unique values only

#----------
#Dictionary
#----------
student={
    "student_name":"Manjula",
    "student_age":20
} 
#stores data as key-value pairs

# User-defined Data type
class Student:
    """
    This class represents a Student.
    It is a user-defined data type created to store student information.
    """

    def __init__(self, name, age):
        """
        Constructor method.
        It initializes the student object with name and age.

        Parameters:
        name (str): Name of the student
        age (int): Age of the student
        """

        self.name = name    # Stores student name
        self.age = age      # Stores student age
student1=Student("Manjula",20)
student2=Student("Taneesha",22)
print(student1.name)    #prints name of student1
print(student2.age)     #prints age of student2

#example for User defined data types

class Employee:
    def __init__(self,name,age,department):
        self.name=name
        self.age=age
        self.department=department
employee1=Employee("Manjula",20,"IT")
employee2=Employee("Taneesha",22,"HR")
print(employee1.name)
print(employee2.name)