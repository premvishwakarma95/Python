# Variable naming - Use descriptive names with underscores between words:
first_name = "Prem"
is_logged_in = True
total_price = 500



name = "Prem"          # str
age = 22               # int
price = 99.50          # float
is_developer = True    # bool
selected_project = None

# Check type
print(type(name))              # <class 'str'>
print(type(age))               # <class 'int'>
print(type(price))             # <class 'float'>
print(type(is_developer))      # <class 'bool'>
print(type(selected_project))  # <class 'NoneType'>


# data types reference with JS
# Javascript has 7 data types: string, number, boolean, null, undefined, object, and symbol.
# Python has 5 data types: str, int, float, bool, and NoneType.


# Change a vairable's value
age = 22
print(age)  # 22

age = 23
print(age)  # 23


## Chapter 2: Variables and data types
age = 22               # int
age = 22.5             # float
age = "twenty-two"     # str



# Use f-strings - Same as JavaScript's template literals
print(f"My name is {name} and I am {age} years old.")


# Understand boolean conversion
print(bool(0))       # False
print(bool(""))      # False
print(bool(None))    # False
print(bool(10))      # True
print(bool("Prem"))  # True