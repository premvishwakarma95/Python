name = "Prem"
language = 'Python'
message = "I'm learning Python"
print(type(name))  # <class 'str'>


#Triple quotes allow text across multiple lines:
message = """Hello Prem!
Welcome to Python.
Let's learn strings."""

print(message)


# 2. String indexing
language = "Python";
# | Character | P | y | t | h | o | n |
# |---|---|---|---|---|---|---|
# | Positive index | 0 | 1 | 2 | 3 | 4 | 5 |
# | Negative index | -6 | -5 | -4 | -3 | -2 | -1 |
print(language[1])  # y
print(language[-1]) # n


# 3. String slicing - Slicing extracts part of a string.
language = "Python"
# text[start:stop:step]
# start: where to begin, included.
# stop: where to end, excluded.
# step: how far to move each time; defaults to 1.
print(language[0:3])  # Pyt — indexes 0, 1, 2
print(language[2:5])  # tho — indexes 2, 3, 4
print(language[:3])   # Pyt — from the beginning
print(language[3:])   # hon — through the end
print(language[:])    # Python — whole string
print(language[-3:])  # hon — last three characters
print(language[::2])  # Pto — indexes 0, 2, 4


# 4. String length
name = "Prem"
print(len(name))  # 4
message = "Hello Prem"
print(len(message))  # 10


# 5. Strings are immutable
# Immutable means you cannot change individual characters in an existing string.
name = "Prem"
name[0] = "B"  # TypeError
name = "Prem"
# You can create a new string and assign it to the same variable:
name = "B" + name[1:]
print(name)  # Brem


# 6. Common string methods
text = "hello prem"

print(text.upper())       # HELLO PREM
print(text.lower())       # hello prem
print(text.capitalize())  # Hello prem
print(text.title())       # Hello Prem

name = "prem"
print(name.upper())  # PREM
print(name)          # prem


# Removing surrounding whitespace
text = "   Hello Prem   "
print(text.strip())   # "Hello Prem"
print(text.lstrip())  # "Hello Prem   "
print(text.rstrip())  # "   Hello Prem"


# Replacing text
message = "I love JavaScript"
print(message.replace("JavaScript", "Python"))
# I love Python
text = "hello hello hello"
print(text.replace("hello", "hi"))
# hi hi hi
print(text.replace("hello", "hi", 1))
# hi hello hello


# Splitting text
skills = "React,Node,Python"
print(skills.split(","))
# ['React', 'Node', 'Python']
# Without an argument, it splits on whitespace:
message = "Hello   Prem"
print(message.split())
# ['Hello', 'Prem']


# Joining strings
words = ["Hello", "Prem"]
print(" ".join(words))  # Hello Prem
print("-".join(words))  # Hello-Prem


# Finding text
message = "Hello Prem"
print(message.find("Prem"))   # 6
print(message.find("Python")) # -1 — not found
# find() returns the starting index of the first match, or -1 when there is no match.


# Checking the beginning or end
filename = "chapter4.py"
print(filename.startswith("chapter"))  # True
print(filename.endswith(".py"))        # True


# Counting occurrences
text = "banana"
print(text.count("a"))  # 3


# 7. Checking whether text exists
message = "I am learning Python"
print("Python" in message)      # True
print("JavaScript" in message)  # False
print("JavaScript" not in message)  # True
# String comparisons and searches are case-sensitive:
print("python" in message)  # False
# For a simple case-insensitive search:
print("python" in message.lower())  # True


# 8. Combining and repeating strings
# Use + to combine strings:
first_name = "Prem"
last_name = "Vishwakarma"
full_name = first_name + " " + last_name
print(full_name)  # Prem Vishwakarma


# Python does not automatically convert a number when adding it to a string:
age = 22
# print("Age: " + age)  # TypeError
print("Age: " + str(age))  # Age: 22
# Use * to repeat a string:
print("Hi! " * 3)  # Hi! Hi! Hi!
print("-" * 10)   # ----------



# 9. F-strings
# An f-string lets you place variables or expressions inside text.
# Put f before the opening quote and use {} for expressions.
name = "Prem"
age = 22
print(f"My name is {name}, and I am {age} years old.")
# My name is Prem, and I am 22 years old.
print(f"Next year, I will be {age + 1}.")  # Next year, I will be 23.
print(f"Uppercase name: {name.upper()}")   # Uppercase name: PREM


# Formatting decimal numbers
price = 49.9876
print(f"Price: {price:.2f}")  # Price: 49.99
# .2f displays the number with two digits after the decimal point. It does not change the original value.