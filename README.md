# Checkpoint Cohort 22

## Topics

- classes and objects
- Input and Output

## Requirements

- The usage of any external help is not allowed, wich include: others help, any LLM such as chatGPT, copilot, etc.
- The concepts are the topics covered in past 2 weeks
- You can use google but you can not look for the exact solution for the proposed problem
- Clone this repository and create a branch with your name
- Conceptial questions: Save the answer in a file with the name `checkpoint-01-concept`
  format:
  ```
  1. c.
  2. b.
  ...
  ```
- Practical questions: Save the answer in a file with the name `pointNumber-title.py`
  example:
  ```
  8-basic_class.py
  9-adding_methods.py
  10-IO_manipulation.py
  11-IO_clases.py
  ```

## Questions

1. What is a class in Python?

   a. A function that creates objects

   b. A blueprint for creating objects

   c. A specific instance of an object

   d. A module for storing functions

2. Which of the following is the correct way to define a class in Python?

   a. `class MyClass()`

   b. `def MyClass:`

   c. `class MyClass:`

   d. `MyClass class:`

3. What is an instance variable in Python?

   a. A variable that is shared across all instances of a class

   b. A variable that is defined outside of a class

   c. A variable that is unique to each instance of a class

   d. A variable that cannot be changed

4. What does the `__init__` method do in a class?

   a. Initializes the server connection

   b. Acts as the constructor for a class

   c. Defines a finalizer for when an object is garbage collected

   d. Initializes static variables

5. Which of the following is true about class variables in Python?

   a. They are variables defined within a method

   b. They are unique to each instance

   c. They are shared among all instances of a class

   d. They cannot be modified

6. How do you access a class variable from inside the class?

   a. `self.variable_name`

   b. `cls.variable_name`
  
   c. `class.variable_name`

   d. `Both A and B are correct`

7. What is the purpose of the `self` keyword in Python classes?

   a. To refer to the class itself

   b. To initialize variables
   
   c. To refer to the instance of the class

   d. To declare static methods

---

8. Basic Class Definition and Instantiation

Define a class named Book with an `__init__` method that initializes two attributes: `title` and `author`. Then, create an instance of `Book` with the title "Python Basics" and the author "John Doe".

---

9. Adding Methods to a Class

Copy the last solution. Add a method `describe_book` to the `Book` class that prints out a description of the book in the format: `"Title: [title], Author: [author]"`. Call this method on the instance you created in Exercise 1.

---

10. Input/Output Manipulation

Write a Python script that asks the user to enter a book title and author, creates an instance of the `Book` class with these values, and then calls the `describe_book` method to print the book's details.

---

11. File Input/Output with Classes
    Create a class named `FileManager` that has the following methods:

- `__init__(self, filename)`: Accepts a filename to work with.
- `write_content(self, content)`: Writes the given content to the file specified during initialization.
- `read_content(self)`: Reads the content of the file and returns it.

Demonstrate using this class to write some content to a file and then read it back.
