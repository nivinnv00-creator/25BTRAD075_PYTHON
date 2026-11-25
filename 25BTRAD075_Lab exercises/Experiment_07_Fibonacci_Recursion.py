# LAB EXERCISE 7: Fibonacci Series Using Recursion

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

terms = int(input("Enter the number of terms: "))

if terms <= 0:
    print("Please enter a positive number of terms.")
else:
    print("Fibonacci Series:")
    for i in range(terms):
        print(fibonacci(i), end=" ")
    print()
