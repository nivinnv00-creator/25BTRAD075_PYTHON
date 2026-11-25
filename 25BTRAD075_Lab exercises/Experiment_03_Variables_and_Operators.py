# LAB EXERCISE 3: Variables, Operators, and Input/Output

name = input("Enter Student Name: ")
age = int(input("Enter Age: "))
height = float(input("Enter Height (in meters): "))

# Arithmetic operators
age_in_5_years = age + 5
squared_age = age ** 2

# Relational operator
is_adult = age >= 18

print("\n" + "=" * 30)
print("        STUDENT PROFILE")
print("=" * 30)
print(f"Name               : {name}")
print(f"Current Age        : {age} years")
print(f"Height             : {height:.2f} m")
print(f"Age in 5 Years     : {age_in_5_years}")
print(f"Age Squared        : {squared_age}")
print(f"Eligible Adult     : {is_adult}")
print("=" * 30)
