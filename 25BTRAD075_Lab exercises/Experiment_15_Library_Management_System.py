# LAB EXERCISE 15: Library Management System

class Book:
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued")
        else:
            print("Book not available")

    def return_book(self):
        if not self.available:
            self.available = True
            print("Book returned")
        else:
            print("Book was not issued")

    def display(self):
        print(self.title, "Available:", self.available)


b = Book("Python Basics")
b.issue()
b.display()
b.return_book()
b.display()
