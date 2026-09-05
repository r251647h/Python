# 3.(I)Dictionary of students and marks
students = {
    "Alice": 85,
    "Benjamin": 92,
    "Tinotenda": 78,
    "Tinashe": 88,
    "Bervaly":  90
}

# This code Display all students and their marks
print("Students and their marks:")
for name, mark in students.items():
    print(f"{name}: {mark}")

# this line of code below is for finding the student with the highest mark
top_student = max(students, key=students.get)
print(f"\nStudent with the highest mark: {top_student} ({students[top_student]})")

#.(II) Create a class called Book with a constructor (__init__) that initializes:Title,Author,Price and
# Write a method that displays the book details.Instantiate two book objects.

# Part 3.ii: Book class
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Price: ${self.price}")

# Instantiate two book objects
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
book2 = Book("1984", "George Orwell", 8.99)

# Display details of the books
print("\nBook 1 details:")
book1.display_details()

print("\nBook 2 details:")
book2.display_details()
