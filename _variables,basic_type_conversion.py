#demonstates the use of differnet variable using un python using simple employee record example

#----------------
#string Variables
# ---------------  
employee_name="Arun" 
department="Engineering"
employee_id="AXC123"  
# stored as string because it has letters, alphabets


#-------------------
# Interger Variables 
#-------------------
employee_age=22
years_of_experience=5 
# stored as whole numbers

#----------------
# Float Variables
#----------------
monthly_salary=20000.75
performance_rating=4.5
#stored as float because it is decimal value

# -------------------------------
# Boolean Variables (True / False)
# -------------------------------
is_full_time = True
has_completed_training = False

# -------------------------------
# Derived Variables (Using Logic)
# -------------------------------
# Check eligibility for bonus based on experience and performance
is_bonus_eligible = (years_of_experience >= 1) and (performance_rating >= 4.5)

# -------------------------------
# Output Section
# -------------------------------

print("Employee Details")
print("-----------------")
print("Name:", employee_name)
print("Employee ID:", employee_id)
print("Department:", department)
print("Age:", employee_age)
print("Experience (Years):", years_of_experience)
print("Monthly Salary:", monthly_salary)
print("Performance Rating:", performance_rating)
print("Full-Time Employee:", is_full_time)
print("Training Completed:", has_completed_training)
print("Eligible for Bonus:", is_bonus_eligible)

#Type conversion


# -----------------------------------
# Original Variables (Already Defined)
# -----------------------------------
age = 22                       # Integer variable
years_of_experience = 5        # Integer variable

# -----------------------------------
# Type Conversion Examples
# -----------------------------------

# 1. Integer to String Conversion
# Used when numeric data needs to be displayed as text
age_str = str(age)

print("Employee Age (string):", age_str)
print("Type:", type(age_str))

# 2. String to Integer Conversion
# Experience value received as text from user or file
experience_str = "2"
experience_int = int(experience_str)

print("Experience (integer):", experience_int)
print("Type:", type(experience_int))