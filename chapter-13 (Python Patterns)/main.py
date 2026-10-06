# In this chapter we’ll learn common ways to write cleaner Python code:
# - Comprehensions
# - Unpacking
# - Sorting
# - Mutability
# - Shallow and deep copying


# 1. List comprehensions
# A list comprehension is a concise way to create a list.
# Example: Create a list of squares of numbers from 0 to 5.
numbers = [1, 2, 3, 4, 5]

squares = [number ** 2 for number in numbers]
print(squares) # [1, 4, 9, 16, 25]

# Filtering with list comprehensions using if/else statements::
numbers = [1, 2, 3, 4, 5, 6]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers) # [2, 4, 6]

# if/else in list comprehensions:
numbers = [1, 2, 3, 4]
labels = [
    "even" if number % 2 == 0 else "odd"
    for number in numbers
]
print(labels) # ['odd', 'even', 'odd', 'even']



# 3. Unpacking - In JS called destructuring
# Unpacking assigns items from an iterable to separate variables.
# the number of items must match the number of variables:
name, age = ("Prem", 22)
print(name)  # Prem
print(age)   # 22

first, second, third = [10, 20, 30]
print(first)   # 10
print(second)  # 20
print(third)   # 30
# Without a starred variable, the number of items must match the number of variables:


# Collecting remaining items with *
first, *remaining = [10, 20, 30, 40]
print(first)      # 10
print(remaining)  # [20, 30, 40]


# Swapping values using unpacking:
a = 5
b = 10
a, b = b, a
print(a)  # 10
print(b)  # 5

# Unpacking inside loops
users = [
    ("Prem", 22),
    ("Amit", 25),
]
for name, age in users:
    print(f"{name} is {age} years old")


# Unpacking into collections - Similar to JS [...rest]
# Use * to expand iterable items:
first = [1, 2]
second = [3, 4]
combined = [*first, *second, 5]
print(combined)     # [1, 2, 3, 4, 5]

# Use ** to expand dictionaries:
defaults = {"theme": "light", "language": "en"}
preferences = {"theme": "dark"}
settings = {**defaults, **preferences}
print(settings)
# {'theme': 'dark', 'language': 'en'}



# 4. Sorting
# Python provides two common ways to sort:
# Feature                                   list.sort()                         sorted()
# Changes the original collection           Yes                                 No
# Return value	                            None	                            A new list
# Works with	                            Lists	                            Any iterable



# 6. Assignment does not copy an object - Same as JS reference assignment
# This is essential when working with lists and dictionaries:
original = [10, 20, 30]
another = original
another.append(40)
print(original)  # [10, 20, 30, 40]
print(another)   # [10, 20, 30, 40]
#Both variables refer to the same list. Silimarly, for dictionaries:
original_dict = {"a": 1, "b": 2}
another_dict = original_dict
another_dict["c"] = 3
print(original_dict)  # {'a': 1, 'b': 2, 'c': 3}
print(another_dict)   # {'a': 1, 'b': 2, 'c': 3}



# Equality versus identity
a = [1,2]
b = [1,2]
c = a
print(a is b) # False
print(a is c) # True    
print(a == b) # True
print(a == c) # True
# Use == to compare values. Use "is" when also want to check identity or reference, commonly with None:



# Shallow and deep copying
# A shallow copy creates a new object but does not create copies of nested objects.
# A deep copy creates a new object and recursively copies all nested objects.
import copy
original = [[1, 2], [3, 4]]
# copied = original.copy()  - This is a shallow copy, but it only works for lists. For other objects, use the copy module:
shallow_copy = copy.copy(original)
deep_copy = copy.deepcopy(original)
shallow_copy[0][0] = 10
print(original)       # [[10, 2], [3, 4]] - original
print(shallow_copy)   # [[10, 2], [3, 4]]
deep_copy[0][0] = 100
print(original)       # [[10, 2], [3, 4]] - original
print(deep_copy)      # [[100, 2], [3, 4]]



# Common pitfall: mutable default arguments
# Python evaluates default argument values once, when the function is defined.
def add_item(item, items=[]):
    items.append(item)
    return items

print(add_item("Python"))
# ['Python']
print(add_item("JavaScript"))
# ['Python', 'JavaScript']


# Use 'None' and create a list inside the function: When we assign default value None to a parameter, it means it would be 'None'
def add_item(item, items=None):
    if items is None:
        items = []

    items.append(item)
    return items
print(add_item("Python"))
# ['Python']
print(add_item("JavaScript"))
# ['JavaScript']



# 10. Common pitfall: repeating nested lists
rows = [[0, 0]] * 3
print(rows)
# [[0, 0], [0, 0], [0, 0]]
rows[0][0] = 99
print(rows)
# [[99, 0], [99, 0], [99, 0]] - this happens because all three rows refer to the same list object or reference. 