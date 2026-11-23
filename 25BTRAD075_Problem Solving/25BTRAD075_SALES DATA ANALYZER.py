# SALES DATA ANALYZER
# Mini Project - Unit 3

products = {}

def add_product():
    name = input("Enter product name: ")

    if name in products:
        print("Product already exists!")
        return

    try:
        quantity = int(input("Enter quantity sold: "))
        price = float(input("Enter price per unit: "))

        if quantity < 0 or price < 0:
            print("Values cannot be negative!")
            return

        products[name] = {
            "quantity": quantity,
            "price": price
        }

        print("Product added successfully!")

    except ValueError:
        print("Enter valid numerical values!")

def update_product():
    name = input("Enter product name: ")

    if name not in products:
        print("Product not found!")
        return

    try:
        quantity = int(input("Enter updated quantity sold: "))
        price = float(input("Enter updated price: "))

        if quantity < 0 or price < 0:
            print("Values cannot be negative!")
            return

        products[name]["quantity"] = quantity
        products[name]["price"] = price

        print("Product updated successfully!")

    except ValueError:
        print("Enter valid numerical values!")

def display_products():
    print("\n========== SALES RECORDS ==========")

    if not products:
        print("No products available!")
        return

    for name, details in products.items():
        revenue = details["quantity"] * details["price"]

        print(f"\nProduct: {name}")
        print(f"Quantity Sold: {details['quantity']}")
        print(f"Price: Rs.{details['price']:.2f}")
        print(f"Revenue: Rs.{revenue:.2f}")

def calculate_total_sales():
    total = 0

    for details in products.values():
        total += details["quantity"] * details["price"]

    print(f"\nTotal Sales Revenue: Rs.{total:.2f}")

def highest_selling_product():
    if not products:
        print("No sales records available!")
        return

    highest = max(products, key=lambda x: products[x]["quantity"])

    print("\n========== TOP SELLING PRODUCT ==========")
    print(f"Product: {highest}")
    print(f"Quantity Sold: {products[highest]['quantity']}")

def compare_products():
    if not products:
        print("No products available!")
        return

    print("\n======= PRODUCT PERFORMANCE =======")

    sorted_products = sorted(
        products.items(),
        key=lambda x: x[1]["quantity"] * x[1]["price"],
        reverse=True
    )

    for name, details in sorted_products:
        revenue = details["quantity"] * details["price"]

        print(f"{name} - Revenue: Rs.{revenue:.2f}")

def main():
    while True:
        print("\n====== SALES DATA ANALYZER ======")
        print("1. Add Product")
        print("2. Update Product")
        print("3. Display Sales Records")
        print("4. Calculate Total Sales")
        print("5. Highest Selling Product")
        print("6. Compare Product Performance")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            add_product()
        elif choice == "2":
            update_product()
        elif choice == "3":
            display_products()
        elif choice == "4":
            calculate_total_sales()
        elif choice == "5":
            highest_selling_product()
        elif choice == "6":
            compare_products()
        elif choice == "7":
            print("Thank you for using Sales Data Analyzer!")
            break
        else:
            print("Invalid choice!")

main()