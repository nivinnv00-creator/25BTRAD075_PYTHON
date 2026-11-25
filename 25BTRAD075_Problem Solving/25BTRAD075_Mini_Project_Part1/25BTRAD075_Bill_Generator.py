# Mini Project - Part 1, Option B: Bill Generator

name = input("Customer name: ")
item = input("Item name: ")
price = float(input("Price: "))
quantity = int(input("Quantity: "))

total = price * quantity

print("\n----- BILL -----")
print("Customer:", name)
print("Item:", item)
print("Quantity:", quantity)
print(f"Total: Rs. {total:.2f}")
