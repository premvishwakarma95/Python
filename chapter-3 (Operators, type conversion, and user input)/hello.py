# 1. Arithmetic operators

a = 10
b = 3

print(a + b)   # 13 — addition
print(a - b)   # 7 — subtraction
print(a * b)   # 30 — multiplication
print(a / b)   # 3.3333333333333335 — division
print(a // b)  # 3 — floor division
print(a % b)   # 1 — remainder
print(a ** b)  # 1000 — power: 10 × 10 × 10


# 2. Assignment operators

score = 10

score += 5   # Same as: score = score + 5
print(score) # 15

score -= 3
print(score) # 12

score *= 2
print(score) # 24


# 3. Comparison operators   
a = 10
b = 5

print(a == b)  # False — equal to
print(a != b)  # True — not equal to
print(a > b)   # True — greater than
print(a < b)   # False — less than
print(a >= b)  # True — greater than or equal to
print(a <= b)  # False — less than or equal to


# 4. Logical operators -- Python evaluates not, then and, then or.
age = 22
has_id = True

print(age >= 18 and has_id)  # True
print(age < 18 or has_id)    # True
print(not has_id)           # False


# 5. User input with input()

name = input("Enter your name: ")
print(f"Hello, {name}!")

# input() always returns a string that's why we use Type conversion.
age = input("Enter your age: ")
age = int(age)
age = int(input("Enter your age: "))
price = float(input("Enter a price: "))
print(f"Next year, you will be {age + 1}.")


# Type conversion functions:
# int() - converts a value to an integer 
# float() - converts a value to a floating-point number 
# str() - converts a value to a string
# In JavaScript, we use Number(), parseInt(), parseFloat(), and String() for type conversion.


# Conversion things
int("10")       # 10
float("10.5")   # 10.5

int("10.5")     # ValueError
int(10.5)       # 10



# Python supports chained comparisons
age = 22
print(18 <= age <= 60)  # True
print(age >= 18 and age <= 60) # This means the same as: