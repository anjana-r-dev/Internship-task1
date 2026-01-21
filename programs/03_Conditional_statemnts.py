"""Conditional statements are used to make decisions in a program.
They execute different blocks of code based on whether a condition is True or False."""

#if statement
age=20
if age>=18:
    print("eligible to vote")
#If it is TRUE , the block excutes

#if-else statement
    age = 16

if age >= 18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")
# used for two possible outcomes

#if-elif-else statement
marks = 85

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
else:
    print("Grade C")
"""Checks conditions top to bottom &
Executes the first true condition"""

#nested if statement
age = 20
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
    else:
        print("ID required")

#example 

class student:
    def __init__(self,age,student_id,marks):
        self.age=age
        self.student_id=student_id
        self.marks=marks
student1=student(20,"AXC123",85)
if student1.age >=18:
    print("Eligible")
else:
    print("Not eligible")
