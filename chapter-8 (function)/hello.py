# 1. What is a function?
# A function is a reusable block of code that performs a task.

def greet():
    print("Hello, Prem!")
    print("Welcome to Python.")

greet()

# Output:
# Hello, Prem!
# Welcome to Python.



# 2. Parameters and arguments
def greet(name):
    print(f"Hello, {name}")

greet('prem')

# Parameter: name, the variable in the definition.
# Argument: "Prem", the value passed when calling it.



# 3. Returning a value - return also ends the function immediately:
def add(a, b):
    return a + b

result = add(10, 20)
print(result)  # 30



# 4. Variable scope 
# Scope determines where a variable can be accessed.
# A local variable is created inside a function:
def show_name():
    name = "Prem"
    print(name)
show_name()
# print(name)  # NameError: name is local to show_name()

# A global variable is defined outside functions:
name = "Prem"
def show_name():
    print(name)
show_name()  # Prem



# 5. *args — multiple positional arguments
# Use *args when the function should accept any number of positional arguments:
# Inside the function, args is a tuple:
def add_numbers(*args):
    print(args)          # (10, 20)
    return sum(args)     # Here sum is built in function and it works like this sum([10, 20]) so sum can take lists and tuple

print(add_numbers(10, 20))      # 30
print(add_numbers(10, 20, 30))  # 60



# 6. **kwargs — multiple keyword arguments
# Use **kwargs to accept any number of keyword arguments:
# Inside the function, kwargs is a dictionary:
def show_details(**kwargs):
    print(kwargs)

show_details(name="Prem", role="Developer")
# {'name': 'Prem', 'role': 'Developer'}



# 10. Lambda functions
# A lambda is a small function written using a single expression:
# A Python lambda returns its expression automatically.
double = lambda number: number * 2

print(double(5))  # 10