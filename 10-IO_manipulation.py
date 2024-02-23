# Extend the Book class definition if necessary
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def describe_book(self):
        return f"Title: {self.title}, Author: {self.author}"


def ask():
    title = input("Enter the book title: ")
    author = input("Enter the book author: ")
    book = Book(title, author)
    return book


# Write a script that takes input and creates an instance of Book

book_1 = ask()
print(book_1.describe_book())
