# LAB EXERCISE 11: Log File Reader Program

try:
    file_name = input("Enter log file name: ")
    with open(file_name, "r") as f:
        data = f.read()

    if not data:
        print("File is empty")
    else:
        print("ERROR:", data.count("ERROR"))
        print("WARNING:", data.count("WARNING"))
        print("INFO:", data.count("INFO"))

except FileNotFoundError:
    print("File not found")
