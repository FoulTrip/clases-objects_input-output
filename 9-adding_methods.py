# Modify the Book class from Exercise 1 and add the describe_book method


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        return f"Title: {self.title}, Author: {self.author}"


# Call the describe_book method here
new_book = Book("Python Basics", "John Doe")
print(new_book.describe_book())
