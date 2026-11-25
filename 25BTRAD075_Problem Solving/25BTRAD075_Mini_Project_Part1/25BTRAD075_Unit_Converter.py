# Mini Project - Part 1, Option A: Unit Converter

print("1. Celsius to Fahrenheit")
print("2. Kilometers to Miles")
print("3. Kilograms to Pounds")

choice = int(input("Enter choice: "))
value = float(input("Enter value: "))

if choice == 1:
    print(f"Result: {(value * 9 / 5) + 32:.2f} °F")
elif choice == 2:
    print(f"Result: {value * 0.621371:.2f} miles")
elif choice == 3:
    print(f"Result: {value * 2.20462:.2f} pounds")
else:
    print("Invalid choice")
