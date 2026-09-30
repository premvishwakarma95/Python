# Your practice task: Ask for someone’s name and age, then print their name, their age next year, and whether they are at least 18.

name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"Your name is {name}.")
print(f"Next year, you will be {age + 1}.")
print(f"You are at least 18: {age >= 18}")

