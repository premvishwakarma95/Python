# we will learn
# if, elif, and else
# Indentation
# Comparison operators
# and, or, and not
# Truthy and falsy values

age = int(input("Enter your age: "));

if age>18:
    print('you are eligible')
else:
    print('you are not eligible')

# age > 18 is the condition.
# : starts the block.
# The four spaces before print() put it inside the block.
# Python uses indentation to group code. In JavaScript, you use braces:



# The elif statement
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")



# Combine conditions with and, or, and not
# AND condition
age = 22
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter")
else:
    print("Entry denied")

# OR condition
day = "Sunday"
if day == "Saturday" or day == "Sunday":
    print("It is the weekend")
else:
    print("It is a weekday")

# NOT condition
is_logged_in = False
if not is_logged_in:
    print("Please log in")



# Indentation controls what runs
age = 16

if age >= 18:
    print("You are eligible")
    print("You can continue")

print("Program finished")



# Truthy and falsy values
# A condition doesn’t have to contain a comparison:
name = "Prem"

if name:
    print("Name is provided")
else:
    print("Name is empty")

# Falsy values are - False, 0, 0.0, "", None, [], {}, ()