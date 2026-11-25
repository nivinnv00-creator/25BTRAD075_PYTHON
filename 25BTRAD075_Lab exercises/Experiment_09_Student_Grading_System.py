# LAB EXERCISE 9: Student Grading System

students = {}

n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter name: ")
    mark = int(input("Enter marks: "))
    students[name] = mark

for name, mark in students.items():
    if mark >= 90:
        grade = "A"
    elif mark >= 75:
        grade = "B"
    elif mark >= 50:
        grade = "C"
    else:
        grade = "F"

    print(name, mark, grade)
