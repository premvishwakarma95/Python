# Given text = "Python", print its first and last characters.
text = "Python";
print(f"first and character {text[0]} and {text[-1]}")

# Given text = "JavaScript", extract "Script" using slicing.
text = "JavaScript"
print(text[4:])

# Reverse "Prem" using slicing.
text = "Prem"
print(text[::-1])  # merP               (+1 - moves forward, -1 - moves backward)

# Convert "   hello python   " to "HELLO PYTHON".
text = "   hello python   "
print(text.strip().upper())

# Replace "Node" with "Python" in "I am learning Node".
text = "I am learning Node"
print(text.replace("Node", "Python"))

# Ask for a name and print its length.
name = input("Enter your name: ");
print(f"Your name contains {len(name)} characters")

# Check whether "developer" exists in "I am a Python developer".
text = "I am a Python developer"
print(f"is developer exists {"developer" in text}")

# Display price = 99.956 with two decimal places using an f-string.
price = 99.956
print(f"{price:.2f}")