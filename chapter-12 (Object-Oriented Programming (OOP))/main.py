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
class User:
    def __init__(self, name):
        self.name = name

    def change_name(self, new_name):
        self.name = new_name


user = User("Prem")
user.change_name("Prem Vishwakarma")

print(user.name) # Output: Prem Vishwakarma



# 5. Instance attributes versus class attributes
# Instance attributes belong to each object. Class attributes are defined on the class and can provide shared values.
class Developer:
    profession = "Software Developer"  # Class attribute

    def __init__(self, name):
        self.name = name              # Instance attribute

dev1 = Developer("Prem")
dev2 = Developer("Amit")

print(dev1.name)        # Prem
print(dev2.name)        # Amit

print(dev1.profession)  # Software Developer
print(dev2.profession)  # Software Developer



# 6. Inheritance: reuse a parent class
# Inheritance allows a class to inherit attributes and methods from another class.
class User:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"My name is {self.name}.")

class Admin(User): # Admin(User) means that Admin inherits from User.
    def delete_user(self):
        print(f"{self.name} deleted a user.")

admin = Admin("Prem")

admin.introduce()
admin.delete_user()                               

# Output:
# My name is Prem.
# Prem deleted a user.

# If the child class needs additional initialization, use super():
# super() calls the parent class's __init__ method. If you don't call super(), the parent class's __init__ won't run, and the child class won't have the parent's attributes.
class User:
    def __init__(self, name):
        self.name = name

class Admin(User):
    def __init__(self, name, permissions):
        super().__init__(name)
        self.permissions = permissions


admin = Admin("Prem", ["view", "delete"])

print(admin.name)         # Prem
print(admin.permissions)  # ['view', 'delete']



# 7. Method overriding
# Method overriding means defining a method in a child class with the same name as a method in its parent class. This lets the child provide its own behavior.
class User:
    def introduce(self):
        print("I am a regular user")

class Admin(User):
    def introduce(self):
        print("I am an admin")

user = User()
admin = Admin()

user.introduce()   # I am a regular user
admin.introduce()  # I am an admin
# Both objects support the same method call, but their behavior differs. This is a simple example of polymorphism.