# LAB EXERCISE 4: Simple Calculator and Area Calculations

import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("\n--- Calculator Results ---")
print(f"Addition       = {num1 + num2}")
print(f"Subtraction    = {num1 - num2}")
print(f"Multiplication = {num1 * num2}")

if num2 != 0:
    print(f"Division       = {num1 / num2:.2f}")
    print(f"Floor Division = {num1 // num2}")
    print(f"Modulus        = {num1 % num2}")
else:
    print("Division by zero is not allowed.")

radius = float(input("\nEnter radius of circle: "))
print(f"Area of Circle: {math.pi * radius ** 2:.2f}")

length = float(input("\nEnter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
print(f"Area of Rectangle: {length * width:.2f}")

base = float(input("\nEnter base of triangle: "))
height = float(input("Enter height of triangle: "))
print(f"Area of Triangle: {0.5 * base * height:.2f}")
