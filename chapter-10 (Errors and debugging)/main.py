# In this chapter you’ll learn how to understand Python errors, handle exceptions, and find problems in your code.
# We’ll cover:
# - Common Python errors
# - Common error types.
# - try and except.
# - Handling multiple exceptions.
# - else and finally.
# - Raising exceptions with raise.
# - Reading tracebacks and debugging.



# 1. Types of errors
# Category              Meaning                                         Example
# Syntax error	        Code breaks Python’s grammar	                Missing : after if
# Runtime error	        Code fails while running	                    Dividing by zero
# Logical error	        Code runs but produces the wrong result	        Using + when you meant *

# Syntax error - The colon is missing. Correct code:
# if age >= 18
#    print("Adult")

# Runtime error: - ZeroDivisionError
print(10 / 0)

# Logical error:
length = 10
width = 5
area = length + width
print(area)  # 15, but the correct area is 50


# 2. Common exceptions - See in Readm.md file
# An exception is an error detected during execution.
int("20.5") # ValueError: invalid literal for int() with base 10: '20.5', Correct code: int(float("20.5"))  # 20



# 3. Handling errors with try and except - it is same as try/catch in JS
# Without exception handling:
age = int(input("Enter your age: ")) # if enter a string, it will raise ValueError
print("Your age:", age)
# With exception handling:
try:
    age = int(input("Enter your age: "))
    print("Your age:", age)
except ValueError:
    print("Please enter a valid whole number.")
print("Program continues.")
# How this works:
# - 1. Python executes the code inside try.
# - 2. If a ValueError occurs, Python skips the remaining code in that try block.
# - 3. It executes the matching except block.
# - 4. Execution continues after the blocks.
# If no exception occurs, Python skips except.  



# 4. Handling different exceptions
try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator/denominator
    print(result)
except ValueError:
    print("please enter whole number")
except ZeroDivisionError:
    print("the denominator cannot be zero")

# You can also handle multiple exception types together when they need the same response:
try:
    result = int(input("Enter a number: ")) / 2
except (ValueError, TypeError):
    print("Invalid input.")



# 5. Getting the exception message
# Use `as` to access the exception object:
try:
    number = int("hello")
except ValueError as error:
    print("Error:", error) # it will print - Error: invalid literal for int() with base 10: 'hello'
# error is a variable name. You can also use err or e.



# 6. Using else
# The `else` block runs when the `try` block finishes without an exception.
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Invalid age.")
else:
    print("Your age is:", age)



# 7. Using finally
# The `finally` block runs no matter what, even if an exception occurs.
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered:", number)
finally:
    print("Input attempt finished.")



# 8. Raising your own exception - JS uses throw new Error("Age cannot be negative."), Python uses raise ValueError("Age cannot be negative.")
# Use raise when your code detects an invalid situation:
def check_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    return age
# Handle it when calling the function:
try:
    checked_age = check_age(-5)
except ValueError as error:
    print("Error:", error)
# Output: Age cannot be negative.



# 9. Reading tracebacks
def divide(a, b):
    return a / b
print(divide(10, 0))
# The error output looks like:
# Traceback (most recent call last):
#   File "practice.py", line 4, in <module>
#     print(divide(10, 0))
#   File "practice.py", line 2, in divide
#     return a / b
# ZeroDivisionError: division by zero

# Read it from the bottom:
# 1. Exception: ZeroDivisionError.
# 2. Message: division by zero.
# 3. Failing line: return a / b.
# 4. Caller: divide(10, 0).



# 10. Basic debugging
# Debugging means finding and fixing the cause of a problem.