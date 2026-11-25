# LAB EXERCISE 13: CSV-Based Payroll Management System
# Keep employees.csv in the same folder as this Python file.

import csv

with open("employees.csv", "r", newline="") as f:
    reader = csv.DictReader(f)

    for row in reader:
        gross = float(row["Basic"]) + float(row["Allowance"])
        net = gross - float(row["Deduction"])

        print("Employee:", row["Name"])
        print("Gross Salary:", gross)
        print("Net Salary:", net)
        print()
