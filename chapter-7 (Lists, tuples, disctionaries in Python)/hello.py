# 1. Lists in Python
# A list stores multiple values in one variable.
# Since you know JavaScript, a Python list is similar to a JavaScript array.
# Lists:
        # Keep items in order.
        # Allow duplicate values.
        # Can contain different data types.
        # Can be changed after creation.
names = ["Prem", "Rahul", "Amit"]
print(names)
# 1. Creating a list    
names = ["Prem", "Rahul", "Amit"]
numbers = [10, 20, 30, 40]
mixed = ["Prem", 22, True, 5.5]
empty = []

# Methods ---
# Use len():
names = ["Prem", "Rahul", "Amit"]
print(len(names))  # 3

# Adding items - append() — add one item at the end
names = ["Prem", "Rahul"]
names.append("Amit")
print(names)  # ['Prem', 'Rahul', 'Amit']

# insert() — add an item at a specific index and other items would be forwarded to the right side
names = ["Prem", "Amit"]
names.insert(1, "Rahul")
print(names)  # ['Prem', 'Rahul', 'Amit']   

# extend() — add multiple items
numbers = [10, 20]
numbers.extend([30, 40])
print(numbers)  # [10, 20, 30, 40]

# Removing items
# items.remove(value)	--    Removes the first matching value
# items.pop(index)	    --    Removes and returns the item at an index
# items.pop()	        --    Removes and returns the last item
# del items[index]	    --    Deletes the item at an index
# items.clear()	        --    Removes all items

# Checking whether an item exists
# Use in or not in:
names = ["Prem", "Rahul", "Amit"]
print("Prem" in names)      # True
print("Ravi" not in names)  # True

# Looping through a list
names = ["Prem", "Rahul", "Amit"]
for name in names:
    print(name)

# To get both the index and the value, use enumerate():
for index, name in enumerate(names):
    print(index, name)

# Slicing a list
numbers = [10, 20, 30, 40, 50]
print(numbers[1:4])   # [20, 30, 40]
print(numbers[:3])    # [10, 20, 30]
print(numbers[2:])    # [30, 40, 50]
print(numbers[::2])   # [10, 30, 50]
print(numbers[::-1])  # [50, 40, 30, 20, 10]

# Useful list operations
numbers = [30, 10, 20, 10]
print(numbers.count(10))  # 2
print(numbers.index(20))  # 2
print(sum(numbers))      # 70
print(min(numbers))      # 10
print(max(numbers))      # 30

# Sorting - sort() changes the original list. sorted() returns a new sorted list:
numbers = [30, 10, 20]
numbers.sort()
print(numbers)  # [10, 20, 30]
numbers.sort(reverse=True)
print(numbers)  # [30, 20, 10]
# sorted()
numbers = [30, 10, 20]
sorted_numbers = sorted(numbers)
print(numbers)         # [30, 10, 20]
print(sorted_numbers)  # [10, 20, 30]

# Reversing
numbers = [10, 20, 30]
numbers.reverse()
print(numbers)  # [30, 20, 10]

# Copying a list
# Assignment does not create a separate list: Both variables refer to the same list.
original = [10, 20, 30]
another = original
another.append(40)
print(original)  # [10, 20, 30, 40]
# To create a separate copy, use the copy() method or list slicing:
original = [10, 20, 30]
another = original.copy()
another.append(40)
print(original)  # [10, 20, 30]
print(another)   # [10, 20, 30, 40]








# 2. Tuples
# A tuple stores multiple values, but its items cannot be replaced, added, or removed after creation.
# Create a tuple using parentheses ():
names = ("Prem", "Rahul", "Amit")
print(names)
print(type(names))  # <class 'tuple'>

# Accessing items - Indexing and slicing work like lists:
print(names[0])    # Prem
print(names[-1])   # Amit
print(names[:2])   # ('Prem', 'Rahul')

# Tuples are immutable
names[0] = "Ravi"
# TypeError: 'tuple' object does not support item assignment
# Tuples do not have methods such as append(), remove(), or pop().

# A tuple with one item needs a comma
value = ("Prem")
print(type(value))  # <class 'str'>
value = ("Prem",)
print(type(value))  # <class 'tuple'>

# Useful tuple operations
numbers = (10, 20, 10, 30)
print(len(numbers))       # 4
print(numbers.count(10))  # 2
print(numbers.index(30))  # 3
print(20 in numbers)      # True

# Unpack it's value or destrure
person = ("Prem", 22)
name, age = person
print(name)  # Prem
print(age)   # 22





# 3. Dictionaries
# A dictionary stores key-value pairs.
# It is similar to a JavaScript object:
# Python
person = {
    "name": "Prem",
    "age": 22,
    "role": "Developer"
}

# Accessing values
# Use the key inside square brackets:
print(person["name"])  # Prem
print(person["age"])   # 22
# Python dictionaries do not use JavaScript-style property access:
# person.name  # Does not access the "name" key
# A missing key raises KeyError:
print(person["city"])  # KeyError

# To avoid KeyError, use the get() method:
print(person.get("city"))  # None
print(person.get("city", "Not Found"))  # Not Found
print(person.get("name"))  # Prem

# Adding and updating values
person["city"] = "Indore"  # Adds a new key
person["age"] = 23        # Updates an existing key
print(person)

# Update multiple values using update():
person.update({
    "age": 24,
    "role": "AI Developer"
})

# Removing values
# Use del or pop():
del person["city"]  # Removes the "city" key
age = person.pop("age")  # Removes and returns the "age" key
print(person)  # {'name': 'Prem', 'role': 'AI Developer'}
person.clear()  # Removes all key-value pairs
print(person)  # {}

# Checking whether a key exists
# in checks dictionary keys by default.
person = {"name": "Prem", "age": 22}
print("name" in person)  # True
print("Prem" in person)  # False
# To check values:
print("Prem" in person.values())  # True

# Looping through dictionaries
for key in person:
    print(key)

# Loop through values:
for value in person.values():
    print(value)

# Loop through key-value pairs:
for key, value in person.items():
    print(key, value)

# Lists, tuples, and dictionaries compared - See in the Readme file.