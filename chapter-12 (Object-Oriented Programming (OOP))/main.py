# we will learn classes, objects, self, __init__, inheritance, properties, and composition, with JavaScript comparisons.
# You already know how to store data in dictionaries and write functions. OOP lets us group related data and functions together.

# 1. What is a class?
# A class defines what an object contains and what it can do.
class User:
    def introduce(self):
        print("Hello! I am a user.")
# Here:
# - class defines a class.
# - User is the class name.
# - introduce() is a method—a function defined inside a class.
# By convention, class names use "PascalCase", such as User, BankAccount, and AI​​Agent.    



# 2. What is an object?
# An object, also called an instance, is created from a class.
class User:
    def introduce(self):
        print("Hello! I am a user.")

user1 = User()
user1.introduce()
# Output: Hello! I am a user.
# User() creates an instance. You do not use new in Python.



# 3. Initialize objects with __init__
# Usually, each user needs their own name and email.
# __init__ runs automatically when you create an instance and initializes its data.
# __init__ - It is commonly called a constructor in beginner tutorials.
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

user1 = User("Prem", "prem@example.com")
user2 = User("Amit", "amit@example.com")

user1.introduce()
user2.introduce()
# Output:
        # Hello! My name is Prem.
        # Hello! My name is Amit.



# 4. What is 'self'?
# self is a reference to the current instance. It allows you to access the instance's data and methods.
# Example: user1.introduce()
# In this call, 'self' refers to user1.